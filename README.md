# PyPISS (v0.1)
#### **Py**thon **P**acket parser generator **I**n **S**imple **S**tructured format
-----
# Intro

 PyPISS is a simple packet parser generator framework inspired by [P4 Lang](http://p4.org)
 If you tired about making every packet formats or,
 If you want to make your own packet format (such as researching, game socket io, etc...)
 This framework may be helpful for creating packet builder/parser.
 
-----
# Specification
* Support bit,byte,short,int,string,list and so on ...
* Declare packet's structure and setting each fields default value or action easily (such as CRC, Flag)
* Creating packet by declared packet's structure
* Automatic validity check from packet's structure
* Creating new packet structure by compositing another packet's structure

## Supporting types

### 1. primitives
|    name   |    c-style type name   | size(bytes) | note                        |
|:----------|:-----------------------|:------------|-----------------------------|
| bool      | bool (not same size)   | **1bit**    | True / False                |
| char      | signed char            | 1           |                             |
| byte      | unsigned char          | 1           |                             |
| short     | signed short           | 2           |                             |
| u_short   | unsigned short         | 2           |                             |
| int       | signed long int        | 4           |                             |
| u_int     | unsigned long int      | 4           |                             |
| long      | signed long long int   | 8           |                             |
| u_long    | unsigned long long int | 8           |                             |
| float     | float                  | 4           |                             |
| double    | double                 | 8           |                             |

### 2. iteratives

|    name   |    c-style type name   | size(bytes) | note                        |
|:----------|:-----------------------|:------------|-----------------------------|
| str(size) | char[]                 | vary        | return in python string     |
| bytes(size)| unsigned char[]       | vary        | return in byte array        |
| arr(size) | array of type          | vary        | return in list, must use with type |

### 3. structures

|    name   |    c-style type name   | size(bytes) | note                        |
|:----------|:-----------------------|:------------|-----------------------------|
| ipv4      | byte[4]                | 4           | return in IPv4 python class |
| ipv6      | short[8]               | 16          | return in IPv6 python class |
| hmac      | byte[6]                | 6           | return in HMAC python class |

## Supporting operators
* {typename}(bits=0) : set field's type, if bits is 0 then using default bit size.
* val(val) : set default value for {val} when build
* val(lambda) : set default value by lambda function when build
* check(lambda) : check value by lambda function when parse


-----
# Installation
* Python 2.x : `pip install pypiss`
* Python 3.x : `pip3 install pypiss`

-----
# Example

## IPv4 with Custom Packets
```[python]
import enum.Enum
from pypiss.PacketStructure import *
from pypiss.PacketUtil import CRC32

class EtherType(Enum):
    IPV4 = 0x0800,
    ARP = 0x0806

class EthernetFrame(PacketHeader):
    _field = [
        field("dst").hmac(),
        field("src").hmac(),
        field("ether_type").u_short().enum(EtherType),
        field("payload").bytes(),   # if skip to define size, auto calculated from rest bytes
        field("crc").int().val(CRC32.make(['payload'])).check() # if skip to define check function, use same logic from make
    ]
    
class IPv4Frame(PacketHeader):
    _field = [
        field("src").ipv4(),
        field("dst").ipv4(),
        ...,
        field("len").u_short(),
        ...,
        field("payload").bytes()
    ]
    
    def parse(self, data):
        self.
        # In this function, all fields except payload should be assigned
    
class PingPongFrame(PacketHeader):
    _field = [
        field(type).byte(bits=3),
        payload()
    ]
    
```

-----
# Roadmap
See in 'Issues'
1. make converter p4 lang to piss python structure

-----
# Contribution
I always need your helps.
don't be shy, don't hesitate, just fork & pull request thx!

If you have any suggestion (feature request, etc...), feel free to contact me!
