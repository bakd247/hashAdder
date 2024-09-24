from tqdm import tqdm, trange
from os import urandom
from binarySearch import binarySearch
import time
from recoverFoundKey import recoverFoundKey
from createKeyToFind import createKey
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
pubKeyResult = createKey(XX,YY)
print("This is the Key you entered in base 10 integer format:",pubKeyResult)
AA = int(input("Please Enter the Size of the Collision List you would like to Create. NOTE: The number you input will be doubled then squared (Example: input of 100 will OutPut - 40,000 total Keys Contained in the Multiples Collision List)(An input of 500 results in 1 million keys)...Please Consider This and keep your input number below 10,000 for Best Restults. Best Performance around 500...However Larger Nunbers are encouraged:"))
AAA = (AA * 2)
print("Creating Lookup table...Please Wait...")
#Create Lookup Table Grid...
from wordAdder import multiplyNum
half = 57896044618658097711785492504343953926418782139537452191302581570759080747169
N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
third = 77194726158210796949047323339125271901891709519383269588403442094345440996225
twosStartPubKey = pubKeyResult * ((half ** (AA))%N)
print("Creating Collision List...Please Wait...")
print("Total Number of Keys Contained In Collision List:", (AAA ** 2))
print("Please wait until the Below counter gets to:", AAA)
#Create Sorted Collision List...
numList = []
for numberList in range(9000):
    prefixList = []
    prefixFindList = []
    prefixList.append(int(str(numberList)[:4])+1000)
    tuplePrefixList = tuple(prefixList)
    prefixFindList.append(tuplePrefixList)
    numList.append(prefixFindList)
twosPositionList = []
for numberedList in range(AAA):
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
        thirdPrefix = (int(str(thirdPlace.x)[:4]))-1000
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
#EasyGrid Search...
print("Searching LookUp Table Grid for Collision Match...")
firstRow = []
for easyGridCount in range(16):
    firstRowEntry = (65536 ** easyGridCount) % N
    firstRow.append(firstRowEntry)
tupleFirstRow = tuple(firstRow)
for easyGrid in tqdm(tupleFirstRow,ascii=True,ncols=100,colour='#00ff00',unit='Rows',desc='GridRows'):
    privKey1 = easyGrid
    tryPlace = multiplyNum(privKey1)
    easyGridPlace = multiplyNum(easyGrid)
    easyKeyToFind = tryPlace.x
    easyPrefix = int(str(easyKeyToFind)[:4])
    for privKeyTry in range(65535):
        firstRowCheck = binarySearch(tupleOfTupleList[easyPrefix-1000], easyKeyToFind)
        if firstRowCheck != -1:
            KeyFound = True
            recoveredKey = recoverFoundKey(firstRowCheck, privKey1)
            print(firstRowCheck)
            print("This is the Found X-Coordinate:", firstRowCheck[0])
            print("Your Private Key is:", recoveredKey)
            exit()
        else:
            tryPlace = tryPlace + easyGridPlace
            easyKeyToFind = tryPlace.x
            easyPrefix = int(str(easyKeyToFind)[:4])
            privKey1 = (privKey1 + easyGrid) % N
#Reverse Grid Search...
print("Checking Lookup Reverse Lookup Grid for Collision Match...Please wait...")
for reverseEasyGrid in tqdm(tupleFirstRow,ascii=True,ncols=100,colour='#00ff00',unit='Rows',desc='GridRows'):
    privKeyR = reverseEasyGrid
    reverseTryPlace = multiplyNum((half-reverseEasyGrid)%N)
    reverseEasyGridPlace = multiplyNum(reverseEasyGrid)
    reverseEasyKeyToFind = reverseTryPlace.x
    reverseEasyPrefix = int(str(reverseEasyKeyToFind)[:4])
    for reversePrivKeyTry in range(65535):
        reverseFirstRowCheck = binarySearch(tupleOfTupleList[reverseEasyPrefix-1000], reverseEasyKeyToFind)
        if reverseFirstRowCheck != -1:
            KeyFound = True
            recoveredKeyR = recoverFoundKey(reverseFirstRowCheck, privKeyR)
            print(reverseFirstRowCheck)
            print("This is the Found X-Coordinate:", reverseFirstRowCheck[0])
            print("Your Private Key is:", ((half - recoveredKeyR)%N))
            exit()
        else:
            reverseTryPlace = (reverseTryPlace - reverseEasyGridPlace)
            reverseEasyKeyToFind = reverseTryPlace.x
            reverseEasyPrefix = int(str(reverseEasyKeyToFind)[:4])
            privKeyR = (privKeyR - reverseEasyGrid) % N
#Enter easyCount Here...]
#Start Here at 65537 and half - 65537
print("Checking Easily Countable Positions for Collision Match...Please wait...")
print("Easy Count is Currently NOT enabled until next update...")
##Random Seach
print("Searching Randomly for a Collision Match...Please wait...")
while KeyFound != True:
    t = time.time()
    privKey = (int((((urandom(32))[2:])).hex(), 16))%half
    #privKey = 39249432821596846840936736167627457208319304603056442398667015916916341738904            #Comment Out previous private key and replace this one with a known private key for testing.
    privateKey1 = privKey-100000
    keyB = multiplyNum(privateKey1)
    keyG = multiplyNum(1)
    keyToFind = keyB.x
    prefix = int(str(keyToFind)[:4])
    for triedSpot in range(200000):
        hashIteration = tupleOfTupleList[prefix-1000]
        result = binarySearch(hashIteration, keyToFind)
        if result != -1:
            KeyFound = True
            recoveredKeyRandom = recoverFoundKey(result, privateKey1)
            print(result)
            print("This is the Found X-Coordinate:", result[0])
            print("Your Private Key is:", recoveredKeyRandom)
            exit()
        else:
            keyB = keyB + keyG
            keyToFind = keyB.x
            prefix = int(str(keyToFind)[:4])
            privateKey1 = privateKey1 + 1
    elapsed_time = time.time() - t
    print("Average Random Key Strings Created and Searched Per Second",(200000//elapsed_time),
            "Average Seconds per Round ", elapsed_time,  end='\r')
    
    