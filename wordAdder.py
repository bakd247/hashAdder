from tinyec.ec import SubGroup, Curve
from tqdm import tqdm
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
# Create 16 powers of 65536
numList = []
numList.append(pubKey)
for bytePosition in range(15):
    for bitPosition in range(16):
        place = pubKey + pubKey
        pubKey = place
    numList.append(place)
    pubKey = pubKey
tupleNumList = tuple(numList)
finalList = []
for tupNum in tqdm(tupleNumList,ascii=True,ncols=100,colour='#00ff00',unit='Columns',desc='Rows'):
    subList = []
    zero = 0
    subList.append(zero)
    position1 = tupNum
    subList.append(position1)
    for iteration in range(65534):
        position2 = position1 + tupNum
        subList.append(position2)
        position1 = position2
    tupleSubList = tuple(subList)
    finalList.append(tupleSubList)   
grid = tuple(finalList)
##Define Multiply Function
def multiplyNum(number):
    N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
    ##Read in the integer input as big endian hex 4 hex digits at a time
    array = ((number)%N).to_bytes(32, "big")
    counter = 0
    hexLists = []
    posList = []
    for count in range(16):
        element = (hex(array[counter])[2:])+(hex(array[counter+1])[2:])
        hexLists.append(element)
        counter += 2
    ##Then Reverse the "words" to be looked up
    ## Then using the grid above...lookup each "hex Word""
    hexLists.reverse()
    tupleHexList = tuple(hexLists)
    for itered, product in enumerate(tupleHexList):
        position = (grid[itered][(int(product, 16))])
        ##Each position is looked up according to its index, and each "hex word" is converted to an integer to give its index
        if position == 0:
            pass
        else:
            posList.append(position)
        tuplePos = tuple(posList)
    ##The positions are added to a list to be added together accounting for zeros along the way    
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
##The result is exactly the same as any binary addition but this acheives the same result using a maximum of 15 additions per operation
##Where 256 bit binary addition takes 255 addition steps maximum...so this is an exact 17 X speed increase per operation