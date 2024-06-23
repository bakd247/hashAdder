from tinyec.ec import SubGroup, Curve
from tqdm import tqdm, trange
from os import urandom
from binarySearch import binarySearch
import time
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
AA = int(input("Please Enter the Size of the Collision List you would like to Create. NOTE: The number you input will be doubled then squared (Example: input of 100 will OutPut - 40,000 total Keys Contained in the Multiples Collision List)(An input of 500 results in 1 million keys)...Please Consider This and keep your input number below 10,000 for Best Restults. Best Performance around 500...However Larger Nunbers are encouraged:"))
AAA = (AA * 2)
print("Creating Lookup table...Please Wait...")
from wordAdder import multiplyNum
half = 57896044618658097711785492504343953926418782139537452191302581570759080747169
N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
third = 77194726158210796949047323339125271901891709519383269588403442094345440996225
twosStartPubKey = pubKeyResult * ((half ** (AA))%N)
print("Creating Collision List...Please Wait...")
print("Total Number of Keys Contained In Collision List:", (AAA ** 2))
print("Please wait until the Below counter gets to:", AAA)
numList = []
for numberList in range(90000):
    prefixList = []
    prefixFindList = []
    prefixList.append(int(str(numberList)[:4])+10000)
    tuplePrefixList = tuple(prefixList)
    prefixFindList.append(tuplePrefixList)
    numList.append(prefixFindList)
twosPositionList = []
for numberedList in range(AAA):
    Place1 = twosStartPubKey + twosStartPubKey
    twosPositionList.append(Place1)
    twosStartPubKey = Place1
for twosPlace, twoPosition in tqdm(enumerate(twosPositionList),ascii=True,ncols=100,colour='#00ff00',unit='Number Of Rows',desc='Input Number of Rows per Column'): ##Add tqdm progress bar and change enumerate to indexing for loop
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
        thirdPrefix = (int(str(thirdPlace.x)[:4]))-10000
        numList[thirdPrefix].append(tupleThirdPlaceList)
        thirdStartPlace = thirdPlace
print("Sorting Prefix Lists, Please Wait...")
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
KeyFound = False
print("Searching...Please wait...")
while KeyFound != True:
    t = time.time()
    privKey = (int((((urandom(32))[2:])).hex(), 16))%N
    #privKey = 19624716410798423420468368083813728604159652301528221199333507958458170899451            Comment Out previous private key and replace this one with a known private key for testing.
    privateKey1 = (privKey - 10000)%N
    keyB = multiplyNum(privateKey1)
    keyG = multiplyNum(1)
    keyToFind = keyB.x
    prefix = int(str(keyToFind)[:4])
    for multipleTry in range(10):
        for triedSpot in range(20000):
            hashIteration = tupleOfTupleList[prefix-10000]
            result = binarySearch(hashIteration, keyToFind)
            if result != -1:
                KeyFound = True
                twosResult = result[1][0]
                threesResult = result[1][1]
                if twosResult >= 0 and threesResult >= 0:
                    foundPrivateKey = (privateKey1 * (((half ** twosResult)*(third ** threesResult))%N))%N
                elif twosResult < 0 and threesResult >= 0:
                    twosResult = 0 - twosResult
                    foundPrivateKey = (privateKey1 * (((2 ** twosResult)*(third ** threesResult))%N))%N
                elif twosResult >= 0 and threesResult < 0:
                    threesResult = 0 - threesResult
                    foundPrivateKey = (privateKey1 * (((half ** twosResult)*(3 ** threesResult))%N))%N
                elif twosResult < 0 and threesResult < 0:
                    twosResult = 0 - twosResult
                    threesResult = 0 - threesResult
                    foundPrivateKey = (privateKey1 * (((2 ** twosResult)*(3 ** threesResult))%N))%N
                print(result)
                print("This is the Found X-Coordinate:", result[0])
                print("Your Private Key is:", foundPrivateKey)
                exit()
            else:
                keyB = keyB + keyG
                keyToFind = keyB.x
                prefix = int(str(keyToFind)[:4])
                privateKey1 = privateKey1 + 1
    elapsed_time = time.time() - t
    print("Average Random Key Strings Created and Searched Per Second",(200000//elapsed_time))
    print("Average Seconds per Round ", elapsed_time)
