# encoding; utf-8

__author__ = "BetaS"


class IPv4(object):
    def __init__(self, val):
        self.__val = val

    @classmethod
    def parse(cls, str=""):
        data = IPv4(0)
        s = str.split(".")

        if len(s) != 4:
            raise ValueError("invalid ip address format")

        for i in s:
            i = int(i)
            if not 0 <= i <= 255:
                raise ValueError("invalid octet for %d" % i)
            data.__val <<= 8
            data.__val += i

        return data

    def __str__(self):
        a = (self.__val>>24)&0xFF
        b = (self.__val>>16)&0xFF
        c = (self.__val>>8)&0xFF
        d = self.__val&0xFF

        return "%d.%d.%d.%d"%(a,b,c,d)

    def __int__(self):
        return self.__val
    
