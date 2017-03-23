# encoding; utf-8

from piss.types import HMAC, IPv4

__author__ = "BetaS"


def calc_crc(args):
    from piss.PacketUtil import calc_crc32
    return lambda a: calc_crc32(bytearray(reduce(lambda x, y: x+y, map(lambda x: a[x], args))))


class field_type:
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
        return self

    def byte(self):
        self._type = field_type.byte
        return self

    def short(self):
        self._type = field_type.short
        return self

    def u_short(self):
        self._type = field_type.u_short
        return self

    def int(self):
        self._type = field_type.int
        return self

    def u_int(self):
        self._type = field_type.u_int
        return self

    def long(self):
        self._type = field_type.long
        return self

    def u_long(self):
        self._type = field_type.u_long
        return self

    def float(self):
        self._type = field_type.float
        return self

    def double(self):
        self._type = field_type.double
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
        return self

    def ipv4(self):
        self._type = field_type.ipv4
        return self

    def val(self, val):
        self._val = val
        return self


class PacketHeader:
    _fields = []

    def __init__(self, data):
        cls = self.__class__
        #for f in self.__class__._fields:

        print(self._fields)
        print(cls._fields)

        pass

    def build(self):
        pass

    def check_validity(self):
        pass


class Packet:
    def __init__(self, data):
        pass

    def build(self):
        pass
