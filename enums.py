from enum import Enum

class DeviceType(Enum):
    ANDROID = "ANDROID"
    CHROMIUM = "CHROMIUM"
    FIREFOX = "FIREFOX"
    IOS = "IOS"
    LINUX = "LINUX"
    MACOS = "MACOS"
    WEB = "WEB"
    WINDOWS = "WINDOWS"

class ServerProtocol(Enum):
    WIREGUARD = "WIREGUARD"
    OPENVPN = "OPENVPN"
    SHADOWSOCKS = "SHADOWSOCKS"
    SOCKS5 = "SOCKS5"

class ServerType(Enum):
    FREE = "FREE"
    PAID = "PAID"