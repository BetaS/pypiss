# encoding; utf-8

__author__ = "BetaS"


class field:
    def __init__(self, name):
        self.name = name
        self.type = ""
        self.val = 0
        self.filter = None

    def short(self, val=0):
        self.type = ">h"
        self.val = val

    def u_short(self, val=0):
        self.type = ">H"
        self.val = val

    def int(self, val=0):
        self.type = ">i"
        self.val = val

    def uint(self, val=0):
        self.type = ">I"
        self.val = val

    def str(self, size=0, var='', val=''):
        if size == 0:
            pass
        else:
            self.type = "%ds" % size
            self.val = val

    def filter(self, func):
        self.filter = func


class PacketStructure:
    _structure = []

    def __init__(self):
        print(self._structure)
        pass

    @classmethod
    def build(cls, data):
        pass

    def check_validity(self):
        pass
