from tinyec.ec import SubGroup, Curve

# List parameters for ecdsa Curve

name = 'secp256k1'
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
a = 0x0000000000000000000000000000000000000000000000000000000000000000
b = 0x0000000000000000000000000000000000000000000000000000000000000007
g = (0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798, 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
h = 1

curve = Curve(a, b, SubGroup(p, g, n, h), name)
pubKey = curve.g*1

# Create 32 powers of 256

numList = []
numList.append(pubKey)
for bytePosition in range(31):
    for bitPosition in range(8):
        place = pubKey + pubKey
        pubKey = place
    numList.append(place)
    pubKey = pubKey
tupleNumList = tuple(numList)

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

# Use the above grid to lookup each byte and add them all together

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
        return("Infinity and Beyond")
        
    else:
        total = tuplePos[0]
        if len(tuplePos) < 2:
            return(total)
            
        else:
            for k in tuplePos[1:]:
                total = total + k
            return(total)
        
# Resulting in a much faster output times for each multiply result
