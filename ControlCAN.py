from CANstruct import *

CANdll = WinDLL("ControlCAN.dll")
devtype = 3
devindex = 0
canindex = 0
Time0 = 0x01
Time1 = 0x1C
initconfig = VCI_INIT_CONFIG(0x00000000, 0xFFFFFFFF, 0, 0, Time0, Time1, 0)
errinfo = VCI_ERR_INFO()
receivebuf = (VCI_CAN_OBJ * 50)()
sendbuf = (VCI_CAN_OBJ * 10)()
boardinfo = VCI_BOARD_INFO()


def Opendevice():
    respond = CANdll.VCI_OpenDevice(devtype, devindex, 0)
    if respond == 1:
        print('打开成功')
    else:
        print('打开失败')
    return respond


def Closedevice():
    respond = CANdll.VCI_CloseDevice(devtype, devindex)
    if respond == 1:
        print('关闭成功')
    else:
        print('关闭失败')
    return respond


def Initcan():
    CANdll.VCI_InitCAN.argtypes = [DWORD, DWORD, DWORD, POINTER(VCI_INIT_CONFIG)]
    CANdll.VCI_InitCAN.restype = c_int
    respond = CANdll.VCI_InitCAN(devtype, devindex, canindex, byref(initconfig))
    if respond == 1:
        print('初始化成功')
    else:
        print('初始化失败')
    return respond


def Startcan():
    respond = CANdll.VCI_StartCAN(devtype, devindex, canindex)
    if respond == 1:
        print('启动成功')
    else:
        print('启动失败')
    return respond


def Resetcan():
    respond = CANdll.VCI_ResetCAN(devtype, devindex, canindex)
    if respond == 1:
        print('复位成功')
    else:
        print('复位失败')
    return respond


def Readboardinfo():
    respond = CANdll.VCI_ReadBoardInfo(devtype, devindex, byref(boardinfo))
    if respond == 1:
        print('获取设备信息成功')
    else:
        print('获取设备信息失败')
    return respond


def Receive():
    rnum = CANdll.VCI_Receive(devtype, devindex, canindex, byref(receivebuf), 50, 200)
    if rnum == 0xFFFFFFFF:
        print('读取数据失败')
        CANdll.VCI_ReadErrInfo(devtype, devindex, canindex, byref(errinfo))
    elif rnum == 0:
        print('无数据')
        pass
    elif rnum > 0:
        for i in range(rnum):
            print(receivebuf[i])
    return rnum


def Transmit():
    respond = CANdll.VCI_Transmit(devtype, devindex, canindex, byref(sendbuf), 1)
    if respond == 1:
        print('发送成功')
    else:
        print('发送失败')
    return respond


def Readerrinfo():
    respond = CANdll.VCI_ReadErrInfo(devtype, devindex, canindex, byref(errinfo))
    if respond == 1:
        print('读取错误成功')
    else:
        print('读取错误失败')
    return respond


def Getreceivenum():
    respond = CANdll.VCI_GetReceiveNum(devtype, devindex, canindex)
    return respond


def Setreference():
    pData = DWORD(0x1C0008)
    respond = CANdll.VCI_SetReference(devtype, devindex, canindex, 0, byref(pData))
    if respond == 1:
        print('设定波特率成功')
    else:
        print('设定波特率失败')
    return respond
