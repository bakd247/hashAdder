from tqdm import tqdm, trange
from tinyec.ec import SubGroup, Curve


name = 'secp256k1'
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
a = 0x0000000000000000000000000000000000000000000000000000000000000000
b = 0x0000000000000000000000000000000000000000000000000000000000000007
g = (0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798, 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
h = 1

curve = Curve(a, b, SubGroup(p, g, n, h), name)
pubKey = curve.g*1

bits = []

for bitPosition in trange(256,total=256,ascii=True,ncols=100,colour='#00ff00',unit='Row',desc='Creating Key LookUp Table...Please Wait:'):
    bit = pubKey + pubKey
    bits.append(bit)
    pubKey = bit
tupleBits = tuple(bits)

def multiplyNum(number):
    additionList = []
    N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
    array = ((bin((number)%N))[2:])[::-1]
    additionList = []
    for Pos, Bit in enumerate(array):
        if int(Bit, 2) == 0:
            pass
        else:
            additionList.append(tupleBits[Pos])
    tupleAddList = tuple(additionList)
    
    if len(tupleAddList) < 1:
        print("Infinity and Beyond")
        
    else:
        total = tupleAddList[0]
        if len(tupleAddList) < 2:
            print(total)
            
        else:
            for k in tupleAddList[1:]:
                total = total + k
            print(total)
    
multiplyNum(115792089237316195423570985008687907852837564279074904382605163141518161494334)
multiplyNum(3)
