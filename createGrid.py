from tinyec.ec import SubGroup, Curve
from tqdm import tqdm
import pickle
# List parameters for ecdsa Curve
def createGrid():
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

    with open("wordGrid.pkl", "wb") as openedFile:
        pickle.dump(grid, openedFile)