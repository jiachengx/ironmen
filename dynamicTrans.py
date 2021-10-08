dict_a = {
    "010203":"hello.exe -i {0}",
    "04050A":"hello.exe -t {0}"
    }

def genDynamicData(rawStr):
        c = []
        if rawStr[:6] in dict_a.keys():
            for idx in range(0, len(rawStr[6:])):
                if idx %2 == 0:
                    c.append(f"0x{rawStr[6+idx]}{rawStr[6+idx+1]}")
            return f"{dict_a[rawStr[:6]]}".format(' '.join(c))

print(genDynamicData('0102030C00'))
print(genDynamicData('04050A0B0E0D0F'))
