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

numList = []
for bytePosition in trange(32,total=32,ascii=True,ncols=100,colour='#00ff00',unit='Row',desc='Creating Key LookUp Table...Please Wait:'):
    A = pubKey * (256 ** bytePosition)
    numList.append(A)
tupleNumList = tuple(numList)

# Need to replace above with 32 iteration addition loop @ every 8th iteration

finalList = []
for tupNum in tupleNumList:
    subList = []
    zero = 0
    subList.append(zero)
    position1 = tupNum
    subList.append(position1)
    for iteration in range(254):
        position2 = position1 + tupNum
        subList.append(position2)
        position1 = position2
    finalList.append(subList)   
grid = tuple(finalList)


def multiplyNum(number):
    N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
    array = ((number)%N).to_bytes(32, "little")       
    list = []
    for byte in array:
        BBB = int(((hex(byte)))[2:], 16)
        list.append(BBB)
    tupleNumber = (tuple(list))
    posList = []
    for iteration, place in enumerate(tupleNumber):
        position = (grid[iteration][place])
        if position == 0:
            pass
        else:
            posList.append(position)
    tuplePos = tuple(posList)
    
    if len(tuplePos) < 1:
        print("Infinity and Beyond")
        
    else:
        total = tuplePos[0]
        if len(tuplePos) < 2:
            print(total)
            
        else:
            for k in tuplePos[1:]:
                total = total + k
            print(total)
        
multiplyNum(115792089237316195423570985008687907852837564279074904382605163141518161494336)
