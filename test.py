# encoding: utf-8

from piss.PacketStructure import field, calc_crc, PacketHeader, Packet
from piss.PacketUtil import hmac

__author__ = 'BetaS'


class EthernetHeader(PacketHeader):
    _fields = [
        field("dst").hmac(),
        field("src").hmac(),
        field("ether_type").u_short().val(0x0800),
        field("payload").bytes(),   # if len is 0 -> obtain rest of bytes
        field("crc").int().val(calc_crc(["payload"]))
    ]


class IPV4Header(PacketHeader):
    _fields = [
        field("version").bits(4),
        field("ihl").bits(4),
        field("dscp").bits(6),
        field("ecn").bits(2),
        field("length").u_short(),
        field("id").u_short(),
        field("flag").bits(3),
        field("offset").bits(5),
        field("ttl").byte(),
        field("protocol").byte(),
        field("checksum").u_short(),
        field("src").ipv4(),
        field("dst").ipv4(),
        field("payload").bytes()
    ]


class IPV4Packet(Packet):
    @classmethod
    def parse(cls, data):
        self = cls()

        self.eth = EthernetHeader(data)
        self.ipv4 = IPV4Header(self.eth.payload)
        return self

    def __init__(self, mac_src, mac_dst, ip_src, ip_dst, payload):
        self.eth = EthernetHeader({"dst": mac_dst, "src": mac_src})
        self.ipv4 = IPV4Header({"src": ip_src, "dst": ip_dst, "payload": payload})

    def build(self):
        self.eth.payload = self.ipv4.build()
        return self.eth.build()


if __name__ == "__main__":
    #EthernetFrame(data="")
    print(IPV4Packet(hmac("ff:ff:ff:ff:ff:ff"), hmac("ff:ff:ff:ff:ff:ff"), "172.31.0.1", "172.31.0.2", "Hello Piss!").build())