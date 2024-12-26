from tinyec.ec import SubGroup, Curve
from tqdm import tqdm, trange
import os.path
#Define checkRange()
def checkRange(inputNumber, minVal, maxVal):
    if (minVal <= inputNumber <= maxVal) == True:
        return True
    else:
        return False
#Define check if input is integer
def checkNotInt(value):
    try:
        int(value)
        return False
    except ValueError:
        return True
#Define checkIfHex
def checkIfHex(entry):
    try:
        int(entry, 16)
        return True
    except ValueError:
        return False
#DefineCheckIfValidKey
def checkIfValidKey(XX, YY):
    if (((XX * XX * XX) + 7)%p) != ((YY * YY)%p):
        return False
    else:
        return True
#Define Binary Search
def binarySearch(array, integer):
    low = 0
    high = (len(array))//2
    mid = 0
    while low <= high:
        mid = low + (high - low) //2
        if array[mid][0] < integer:
            low = mid + 1
        elif array[mid][0] > integer:
            high = mid - 1
        else:
            return array[mid][0], array[mid][1]
    return -1
#Define CreateKey
##Need valid check in main NOt in this function...will check if hex and valid in loop in main
def createKey(XX,YY):
    name = 'secp256k1'
    p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
    n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
    a = 0x0000000000000000000000000000000000000000000000000000000000000000
    b = 0x0000000000000000000000000000000000000000000000000000000000000007
    g = (XX,YY)
    h = 1
    if ((XX * XX * XX)+7)%p != (YY * YY)%p:
        print("Invalid PublicKey Entry Please Relaunch The program and Try again... Be sure to NOT include the 02, 03 or 04 at the begining of the public key...Enter ONLY the X and Y Coordinates in Hexidecimal Format...")
        exit()
    else:    
        curve = Curve(a, b, SubGroup(p, g, n, h), name)
        pubKey= curve.g*1
        return(pubKey)
#Define RecoverFoundKey    
def recoverFoundKey(result, privateKey1, inputKey, multiplyNum):
    half = 57896044618658097711785492504343953926418782139537452191302581570759080747169
    N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
    third = 77194726158210796949047323339125271901891709519383269588403442094345440996225
    twosResult = result[1][0]
    threesResult = result[1][1]
    if twosResult >= 0 and threesResult >= 0:
        foundPrivateKey = (privateKey1 * ((half ** twosResult)*(third ** threesResult)))%N
        correctedPrivKey = multiplyNum(foundPrivateKey)
        if correctedPrivKey.y == inputKey.y:
            foundPrivateKey = foundPrivateKey
        else:
            foundPrivateKey = N - foundPrivateKey
        return(foundPrivateKey)
    elif twosResult < 0 and threesResult >= 0:
        twosResult = 0 - twosResult
        foundPrivateKey = (privateKey1 * ((2 ** twosResult)*(third ** threesResult)))%N
        correctedPrivKey = multiplyNum(foundPrivateKey)
        if correctedPrivKey.y == inputKey.y:
            foundPrivateKey = foundPrivateKey
        else:
            foundPrivateKey = N - foundPrivateKey
        return(foundPrivateKey)
    elif twosResult >= 0 and threesResult < 0:
        threesResult = 0 - threesResult
        foundPrivateKey = (privateKey1 * ((half ** twosResult)*(3 ** threesResult)))%N
        correctedPrivKey = multiplyNum(foundPrivateKey)
        if correctedPrivKey.y == inputKey.y:
            foundPrivateKey = foundPrivateKey
        else:
            foundPrivateKey = N - foundPrivateKey
        return(foundPrivateKey)
    elif twosResult <= 0 and threesResult <= 0:
        twosResult = 0 - twosResult
        threesResult = 0 - threesResult
        foundPrivateKey = (privateKey1 * ((2 ** twosResult)*(3 ** threesResult)))%N
        correctedPrivKey = multiplyNum(foundPrivateKey)
        if correctedPrivKey.y == inputKey.y:
            foundPrivateKey = foundPrivateKey
        else:
            foundPrivateKey = N - foundPrivateKey
        return(foundPrivateKey)
#Define Create Prefix List
def sortKeys(twosStartPubKey,AAA,AA,third,N):
    numList = []
    for numberList in range(900000):
        prefixList = []
        prefixFindList = []
        prefixList.append(int(str(numberList)[:6])+100000)
        tuplePrefixList = tuple(prefixList)
        prefixFindList.append(tuplePrefixList)
        numList.append(prefixFindList)
    twosPositionList = []
    #Fill Prefix List with keys to be sorted
    for numberedList in range(AAA+1):
        Place1 = twosStartPubKey + twosStartPubKey
        twosPositionList.append(Place1)
        twosStartPubKey = Place1
    for twosPlace, twoPosition in tqdm(enumerate(twosPositionList),ascii=True,ncols=100,colour='#00ff00',unit='Number Of Rows',desc='Input Number of Rows per Column'):
        thirdStartPlace = twoPosition * (third ** ((AAA))%N)
        for thirdMultiple in range(AAA):
            thirdPlaceList = []
            indicatorList = []
            thirdPlace = thirdStartPlace + thirdStartPlace + thirdStartPlace
            thirdPlaceList.append(thirdPlace.x)
            indicatorList.append((twosPlace+1)-AA)
            indicatorList.append((thirdMultiple+1)-(AAA))
            tupleIndicatorList = tuple(indicatorList)
            thirdPlaceList.append(tupleIndicatorList)
            tupleThirdPlaceList = tuple(thirdPlaceList)
            thirdPrefix = (int(str(thirdPlace.x)[:6]))-100000
            numList[thirdPrefix].append(tupleThirdPlaceList)
            thirdStartPlace = thirdPlace
    print("Sorting Prefix Lists, Please Wait...")
    #Sort Each Prefix List
    sortedPrefixList = []
    for numsListed in numList:
        sortedList = sorted(numsListed)
        tupleSortedList = tuple(sortedList)
        sortedPrefixList.append(tupleSortedList)
    tupledList = []
    for eachList in numList:
        tupleEachList = tuple(eachList)
        tupledList.append(tupleEachList)
    tupleOfTupleList = tuple(tupledList)
    return tupleOfTupleList
##ByteAdder
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
N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
numList = []
for bytePosition in range(32):
    A = pubKey * ((256 ** bytePosition)%N)
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