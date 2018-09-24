import math
import base64
from scipy.special import gammaincc
from scipy.special import gamma
import binascii
import os
import random
import string

# compute function related to rt
# compute rt
def compute_rt(str):
    rt = 1
    str_len = len(str)-1
    for i in range(0,str_len):
        if str[i] == str[i+1]:
            rt = rt
        else:
            rt +=1
    return rt

def compute_rt_pi(str):
    str_len = len(str)
    number1_len = str.count('1')
    rt_pi = 1.0*number1_len/str_len
    return rt_pi

def compute_rt_pv(str):
    str_len = len(str)
    rt = compute_rt(str)
    rt_pi = compute_rt_pi(str)
    temp_up = abs(rt - 2*str_len*rt_pi*(1-rt_pi))
    temp_down = 2*math.sqrt(2*str_len)*rt_pi*(1-rt_pi)

    rt_pv = math.erfc(1.0*temp_up/temp_down)
    return rt_pv


# compute function related to ft

def compute_ft_sn(str):
    number_1 = str.count('1')
    number_0 = str.count('0')
    sn = number_1 - number_0
    return sn
def compute_ft_pv(str):
    str_len = len(str)
    s_obs = abs(1.0*compute_ft_sn(str))/math.sqrt(str_len)
    ft_pv = math.erfc(1.0*s_obs/math.sqrt(2))
    return ft_pv

# compute function related to ftb

def compute_ftb_pi(str,M):
    str_len = len(str)
    N = int(str_len/M)
    ftb_pi = []
    str_block = []
    for i in range(0,N):
        str_block.append(str[i*M:(i+1)*M])
    for str_simple in str_block:
        number_1 = str_simple.count('1')
        pi_block = 1.0*number_1/M
        ftb_pi.append(pi_block)
    return ftb_pi

def compute_ftb_xx_obs(str,M):
    ftb_pi = compute_ftb_pi(str,M)
    print(ftb_pi)
    sum = 0
    for pi in ftb_pi:
        sum +=(pi-0.5)*(pi-0.5)
    ftb_xx_obs = 4*M*sum
    return ftb_xx_obs
def compute_ftb_pv(str1,M):
    str_len = len(str1)
    N = int(str_len/M)
    # print("N = " + str(N))
    ftb_xx_obs = compute_ftb_xx_obs(str1,M)
    # print("ftb_xx_obs = " + str(ftb_xx_obs))
    ftb_pv = gammaincc(1.0*N/2,1.0*ftb_xx_obs/2)
    return ftb_pv

# sample read

def run_test_pv(filename):
    block_size = 16
    empty_str = ''
    rt_count = 0
    number_1 = 0
    str_01_len = 0
    char_between =''
    f_ob = open(filename,'r')
    str_block = f_ob.read(block_size)
    while str_block != empty_str:
        str_block_len = len(str_block)
        str_hex = binascii.hexlify(base64.b64decode(str_block))
        str_temp = str(bin(int(str_hex,16)))
        str_temp = str_temp[2:]
        str_temp_len = len(str_temp)
        if str_block_len*6 - str_temp_len == 0:
            str_01 = str_temp
        else:
            str_01 = '0'*(str_block_len*6-str_temp_len) + str_temp

        # print(str_temp)
        # str_hh = str(str_hex)
        # print(str_hh)
        # print(str_hh[2])
        # str_2 = str_hh[2]
        # first_number = int(str_2,16)
        # if first_number >= 8:# if the first char <8, we have to padding the first hex
        #     str_01 = str_temp[2:]
        # elif first_number >= 4:
        #     padding = '0'
        #     str_01 = padding + str_temp[2:]
        # elif first_number >= 2:
        #     padding = '00'
        #     str_01 = padding + str_temp[2:]
        # elif first_number == 1:
        #     padding = '000'
        #     str_01 = padding + str_temp[2:]
        # else:
        #     padding = '0000'
        #     str_01 = padding + str_temp[2:]
        rt_count += compute_rt(str_01)
        # print(str_hex)
        # print(str_block_len*6)
        # print(str_temp_len)
        # print("!!!!!!!")
        # print(str_01)

        number_1 += str_01.count('1')
        #print(number_1)
        str_01_len += len(str_01)
        #print(str_01_len)


        char_between += str_01[0]
        char_between += str_01[-1]
        str_block = f_ob.read(block_size)
    f_ob.close()

    rt_pi = 1.0 * number_1 / str_01_len
    # print(rt_pi)
    # print(str_01_len)



    char_between = char_between[1:]# if the first block's final char is the same as the second block's first char, the rt counted twince
    char_between_length = len(char_between)
    lens = int(char_between_length/2)
    for i in range(0,lens):
        if char_between[2*i] == char_between[2*i+1]:
            rt_count -=1
        else:
            rt_count += 0

    temp_up = abs(rt_count-2*str_01_len*rt_pi*(1-rt_pi))
    temp_down = 2*math.sqrt(2*str_01_len)*rt_pi*(1-rt_pi)

    rt_pv = math.erfc(1.0*temp_up/temp_down)
    return rt_pv

def frequency_test_pv(filename):
    block_size = 16
    empty_str = ''
    str_01_len = 0
    sn = 0
    try:
        f_ob = open(filename,'r')
    except FileNotFoundError:
        print("The file doesn't exist!!")
    else:
        str_block = f_ob.read(block_size)
        while str_block != empty_str:
            str_block_len = len(str_block)
            str_hex = binascii.hexlify(base64.b64decode(str_block))
            str_temp = str(bin(int(str_hex,16)))
            str_temp = str_temp[2:]
            str_temp_len = len(str_temp)
            if str_block_len*6 - str_temp_len == 0:
                str_01 = str_temp
            else:
                str_01 = '0'*(str_block_len*6 - str_temp_len) + str_temp

            str_01_len += len(str_01)
            sn += compute_ft_sn(str_01)
            str_block = f_ob.read(block_size)
        f_ob.close()
        s_obs = 1.0*abs(sn)/math.sqrt(str_01_len)
        ft_pv = math.erfc(1.0*s_obs/math.sqrt(2))

        return ft_pv
def frequency_test_block(filename,M):# WARNING M is the base64 size, if you want to use bit size, bit_size = M*6
    pi = []
    N = 0
    sum = 0.0
    try:
        f_ob = open(filename,'r')
    except FileNotFoundError:
        print("The file doesn't exist!!")
    else:
        block_size = M
        str_block = f_ob.read(block_size)
        while len(str_block) == block_size:
            str_hex = binascii.hexlify(base64.b64decode(str_block))
            str_temp = str(bin(int(str_hex,16)))
            str_temp = str_temp[2:]
            str_temp_len = len(str_temp)
            if block_size*6 == str_temp_len:
                str_01 = str_temp
            else:
                str_01 = '0'*(block_size*6-str_temp_len) + str_temp
            # print(str_01)
            number_1 = str_01.count('1')
            ftb_pi = 1.0*number_1/len(str_01)
            pi.append(ftb_pi)
            N += 1
            # print(pi)
            # print(N)
            str_block = f_ob.read(block_size)
        f_ob.close()
        for p in pi:
            # print(p)
            sum += (p-0.5)*(p-0.5)
        x_obs = 4*M*6*sum
        # print("x_obs = " + str(x_obs))
        ftb_pv = gammaincc(1.0*N/2,1.0*x_obs/2)
        return ftb_pv
# mass produce keys

def create_key(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
    os.chdir(path)
    keytext_path = path + '/key.txt'
    keytext_folder = os.path.exists(keytext_path)
    if not keytext_folder:
        print("fuck")
        f_obj = open('key.txt','w')
        for i in range(0, 1000):
            ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 21))
            f_obj.write(ran_str + '\n')
        f_obj.close()
    else:
        print("The file is already exist!")
# read big txt in to small txt

def read_big_to_small(filename,size):
    try:
        f = open(filename)
    except FileExistsError:
        print("The file doesn't exist!!")
    else:
        while True:
            chunk_data = f.read(size)
            if not chunk_data:
                break
            yield chunk_data













