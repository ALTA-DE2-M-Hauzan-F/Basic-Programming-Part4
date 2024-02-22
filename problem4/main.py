def ubah_huruf(sentence):
    pattern = ""
    geser=10
    for s in sentence:
        # get unicode (65-90)
        newcode=ord(s)+geser
        if s==" ":
            pattern +=" "
        # return unicode to alphabet
        elif newcode>90:
            pattern +=chr(newcode-26)
        else: pattern +=chr(newcode)
    return pattern

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB