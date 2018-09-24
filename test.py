from AES import AES_encrypt,AES_decrypt
import random
import string
import os
file_name = '/Users/liuziyang/Desktop/Python/plaintext.txt'
file_key_name = "/Users/liuziyang/Desktop/Python/key.txt"




# try:
#     f = open(file_name)
# except FileExistsError:
#     print("The file doesn't exist")
# else:
#     text = f.read(1024)
#     crypto_text = AES_encrypt(key,text)
#     print(crypto_text)
#     plain_text = AES_decrypt(key,crypto_text)
#     print(plain_text)
print("~~~~~~~~~~~~~~~~~~~~~")
try:
    f_obj = open(file_key_name,'w')
except FileExistsError:
    print("The file doesn't exist!")
    f_obj.write('')
else:
    for i in range(0,1000):
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 21))
        f_obj.write(ran_str+'\n')
f_obj.close()

project_path = '/Users/liuziyang/Desktop/Python'
os.chdir(project_path)
plain_text_path = project_path + '/plaintext.txt'
cypto_text_path = project_path +'/crypto'
# file_key_obj = open(file_key_name,'r')
# str_key = file_key_obj.readline(2)
# f_obj = open(plain_text_path,'r')
# str_plain = f_obj.read(1440)
# print(str_plain)
# print(len(str_plain))
# str_plain = str(str_plain)
# str_cypto = AES_encrypt(str_key,str_plain)
# print(str_cypto)
# plain_text = AES_decrypt(str_key,str_cypto)
# print(plain_text)





index = 0
with open(plain_text_path,'r') as f_plain_obj:
    while True:
        plain_text_simple = f_plain_obj.read(10240)
        # plain_text_simple = str(plain_text_simple)
        print(len(plain_text_simple))
        # print("++++++++new plaintext ======"+plain_text_simple)
        if not plain_text_simple:
            break
        else:
            file_key_obj = open(file_key_name,'r',encoding='utf-8')
            ran_key = file_key_obj.readline(random.randint(0,1000))
            print(ran_key)
            cypto_text = AES_encrypt(ran_key,plain_text_simple)
            file_key_obj.close()
            file_cypto_obj = open(cypto_text_path +'/cryptotext%d.txt' % index,'w')
            file_cypto_obj.write(cypto_text)
            index +=1
            file_cypto_obj.close()


