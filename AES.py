import base64
from Crypto.Cipher import AES

def padding(value):
    value = bytes(value,encoding='utf-8')
    while len(value) % 16 != 0:
        value += b'\x00'
    value = str(value,encoding='utf-8')
    return str.encode(value)
def AES_encrypt(key,plain_text):
    aes = AES.new(padding(key),AES.MODE_ECB)
    #plain_text = base64.encodebytes(padding(plain_text))

    crypto_text_temp = aes.encrypt(padding(plain_text))
    print(len(padding(plain_text)))
    crypto_text = str(base64.encodebytes(crypto_text_temp),encoding='utf-8')
    print(len(crypto_text))
    return crypto_text
def AES_decrypt(key,crypto_text):
    aes = AES.new(padding(key),AES.MODE_ECB)
    crypto_text_temp = base64.decodebytes(crypto_text.encode(encoding='utf-8'))
    # crypto_text_temp = base64.decodebytes(crypto_text_temp)
    plain_text = str(aes.decrypt(crypto_text_temp),encoding='utf-8').rstrip('\0')
    return plain_text

plain_str ='AREFARFAERFERGGBT\n SBDRERFARFAREFARFAERFERGERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSdfasdfa sdf sgreig ergerg vea rgarf aergfaRGDFGSTRHRTHSVFSDGERTGSGAERGAREGFERGAERGAERGAERGAERGAERGAERGFSERGTRTGHTRHTDYHDTGZGSAERFGARFAREFAERFAREFAREFGAERFGERFARFARFERFERGERGERGAERGFE ERFEARGAERGRE FRVFAERGVEGRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRTRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGSGSRRTHRYUMJ YTHNDYBDRERFARFAREFARFAERFERGGBRT SRTGS SRTGSRTG SBVSDRBDTYHNTYJUYergaergasergaergaergaergaerbgrtrehtgtynyyy'
print(len(plain_str))
# plain_str = "fdgdsfgbdfsdzfbgzdgtbszgtbdstgbszdrtbgsdzrbszbstfb"
key_str ='sdfsdfadfas'
crypto_Str = AES_encrypt(key_str,plain_str)
print(crypto_Str)
plain_str = AES_decrypt(key_str,crypto_Str)
print(plain_str)
