import binascii
import base64
from base_function import run_test_pv
from base_function import frequency_test_pv
from base_function import frequency_test_block


filename = '/Users/icedragonliu/Desktop/Python/01.txt'

pv =  frequency_test_block(filename,20)
print(pv)
