import binascii
import base64
from base_function import compute_rt_pv
import math
from base_function import compute_rt_pi
from base_function import compute_ft_pv
from base_function import compute_ftb_pv





filename = "/Users/icedragonliu/Desktop/Python/01.txt"

f = open(filename,'r')
str_b64 = f.read()
str_hex = binascii.hexlify(base64.b64decode(str_b64))
str_tt = str(str_hex)

str_01 = bin(int(str_hex,16))
print(str_01)
pi = compute_rt_pi(str_01[2:])
print(pi)
pv = compute_ftb_pv(str_01[2:],120)
print(pv)