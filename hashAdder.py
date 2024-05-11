from tinyec.ec import SubGroup, Curve
from tqdm import tqdm, trange
from os import urandom
from binarySearch import binarySearch
from operator import itemgetter
print("                                                  ")
print("                                                  ")
print("\033[0;32m _               _        _       _     _\033[00m")
print("\033[0;32m| |__   __ _ ___| |__    / \   __| | __| | ___ _ __\033[00m")
print("\033[0;32m| '_ \ / _` / __| '_ \  / _ \ / _` |/ _` |/ _ \ '__|\033[00m")
print("\033[0;32m| | | | (_| \__ \ | | |/ ___ \ (_| | (_| |  __/ |\033[00m")
print("\033[0;32m|_| |_|\__,_|___/_| |_/_/   \_\__,_|\__,_|\___|_|\033[00m")
print("                                                  ")
print("                                                  ")
XX = int((input("Please Enter Your Public Key X Coordinate In Hex Format:")),16)
YY = int((input("Please Enter Your Public Key Y Coordinate In Hex Format:")),16)
def createKey(XX,YY):
    name = 'secp256k1'
    p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
    n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
    a = 0x0000000000000000000000000000000000000000000000000000000000000000
    b = 0x0000000000000000000000000000000000000000000000000000000000000007
    g = (XX,YY)
    h = 1
    if (((XX * XX * XX)%p) + 7) != ((YY * YY)%p):
        invalid = ("The Public Key X and Y Coordinates You Entered Are NOT Valid...NOTE: DO NOT Include 02, 03 Or 04 At The Begining Of The X Coordinate And Make Sure You Are Using Hexidecimal Format. If You Need Assistance...Please Contact Technical Support...Please Try Again...Enter Valid X and Y Coordinates For Your Public Key...")
        return(invalid)
        exit()
    else:
        curve = Curve(a, b, SubGroup(p, g, n, h), name)
        pubKey= curve.g*1
        return(pubKey)
pubKeyResult = createKey(XX,YY)
print("This is the Key you entered in base 10 integer format:",pubKeyResult)
AA = int(input("Please Enter the Size of the Collision List you would like to Create. Best Performance around 10,000:"))
print("Creating Lookup table...Please Wait...")
from wordAdder import multiplyNum
half = 57896044618658097711785492504343953926418782139537452191302581570759080747169
N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
third = 77194726158210796949047323339125271901891709519383269588403442094345440996225
AAA = (AA**2)
twosStartPubKey = pubKeyResult * ((half ** (AA))%N)
print("Creating Collision List...Please Wait...")
numList = []
for numberList in range(90):
    prefixList = []
    prefixFindList = []
    prefixList.append(int(str(numberList)[:2])+10)
    tuplePrefixList = tuple(prefixList) 
    prefixFindList.append(tuplePrefixList)
    numList.append(prefixFindList)
twosPositionList = []
for numberedList in range(AAA):
    Place1 = twosStartPubKey + twosStartPubKey
    twosPositionList.append(Place1)
    twosStartPubKey = Place1
threesList = []
for twosPlace, twoPosition in enumerate(twosPositionList):
    thirdStartPlace = twoPosition * (third ** AA)
    for thirdMultiple in range(AAA):
        thirdPlaceList = []
        indicatorList = []
        thirdPlace = thirdStartPlace + thirdStartPlace + thirdStartPlace
        thirdPlaceList.append(thirdPlace.x)
        indicatorList.append((twosPlace+1)-AA)
        indicatorList.append((thirdMultiple+1)-AA)
        tupleIndicatorList = tuple(indicatorList)
        thirdPlaceList.append(tupleIndicatorList)
        tupleThirdPlaceList = tuple(thirdPlaceList)
        for numedList in numList:
            if numedList[0][0] != int(str(thirdPlace.x)[:2]):
                pass                                            
            else:
                numedList.append(tupleThirdPlaceList)
        thirdStartPlace = thirdPlace   
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
print(tupleOfTupleList)
