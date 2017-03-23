# encoding; utf-8

from enum import Enum
from piss.types import HMAC, IPv4

__author__ = "BetaS"


def calc_crc(args):
    from piss.PacketUtil import calc_crc32
    return lambda a: calc_crc32(bytearray(reduce(lambda x, y: x+y, map(lambda x: a[x], args))))


class field_type(Enum):
    bit     = {"struct":"?", "bits":1, "type": bool}
    char    = {"struct":"c", "bits":8, "type": bytes}
    byte    = {"struct":"B", "bits":8, "type": int}
    short   = {"struct":"h", "bits":16, "type": int}
    u_short = {"struct":"H", "bits":16, "type": int}
    int     = {"struct":"i", "bits":32, "type": int}
    u_int   = {"struct":"I", "bits":32, "type": int}
    long    = {"struct":"q", "bits":64, "type": int}
    u_long  = {"struct":"Q", "bits":64, "type": int}
    float   = {"struct":"f", "bits":32, "type": float}
    double  = {"struct":"d", "bits":64, "type": float}
    bytes   = {"struct":"p", "bits":8, "type": bytearray}
    str     = {"struct":"str", "bits":8, "type": str}
    ipv4    = {"struct":"4B", "bits":32, "type": IPv4}
    hmac    = {"struct":"6B", "bits":48, "type": HMAC}


class field:
    def __init__(self, name):
        self._name = name
        self._type = None
        self._size = 1
        self._val = None
        self._filter = None

    def bit(self):
        self._type = field_type.bit
        self._val = False
        return self

    def byte(self):
        self._type = field_type.byte
        self._val = 0
        return self

    def short(self):
        self._type = field_type.short
        self._val = 0
        return self

    def u_short(self):
        self._type = field_type.u_short
        self._val = 0
        return self

    def int(self):
        self._type = field_type.int
        self._val = 0
        return self

    def u_int(self):
        self._type = field_type.u_int
        self._val = 0
        return self

    def long(self):
        self._type = field_type.long
        self._val = 0
        return self

    def u_long(self):
        self._type = field_type.u_long
        self._val = 0
        return self

    def float(self):
        self._type = field_type.float
        self._val = 0.0
        return self

    def double(self):
        self._type = field_type.double
        self._val = 0.0
        return self

    def bits(self, size=0):
        self._type = field_type.bit
        self._size = size
        return self

    def bytes(self, size=0):
        self._type = field_type.byte
        self._size = size
        return self

    def str(self, size=0):
        self._type = field_type.str
        self._size = size
        return self

    def arr(self, size=0):
        self._size = size
        return self

    def struct(self, type):
        pass

    def hmac(self):
        self._type = field_type.hmac
        self._val = 0.0
        return self

    def ipv4(self):
        self._type = field_type.ipv4
        return self

    def val(self, val):
        self._val = val
        return self

    def __str__(self):
        return {"name": self._name, "type": self._type}


class PacketHeader:
    _fields = []

    def __init__(self, data):
        cls = self.__class__

        for f in cls._fields:
            val = data[f._name] if f._name in data else f._val
            exec("self."+f._name+" = val")

        pass

    def build(self):
        pass

    def check_validity(self):
        pass

    def __str__(self):
        cls = self.__class__
        val = {}
        for f in cls._fields:
            exec("val['"+f._name+"'] = self."+f._name)

        return str(val)


class Packet:
    def __init__(self, data):
        pass

    def build(self):
        pass
