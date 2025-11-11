from tqdm import tqdm, trange
from os import urandom
from functionality import binarySearch, recoverFoundKey, createKey, sortKeys, multiplyNum, checkRange, checkNotInt, checkIfHex, checkIfValidKey
import time
import os.path
import pickle
COLOR_GREEN = f"\033[92m"
COLOR_RESET = f"\033[0m"
print(r"                                                  ")
print(r"                                                  ")
print(COLOR_GREEN+r"      _               _        _       _     _"+COLOR_RESET)
print(COLOR_GREEN+r"     | |__   __ _ ___| |__    / \   __| | __| | ___ _ __"+COLOR_RESET)
print(COLOR_GREEN+r"     | '_ \ / _` / __| '_ \  / _ \ / _` |/ _` |/ _ \ '__|"+COLOR_RESET)
print(COLOR_GREEN+r"     | | | | (_| \__ \ | | |/ ___ \ (_| | (_| |  __/ |"+COLOR_RESET)
print(COLOR_GREEN+r"     |_| |_|\__,_|___/_| |_/_/   \_\__,_|\__,_|\___|_|"+COLOR_RESET)
print(r"                                                  ")
print(r"                                                  ")
#Save collisionList to File or Create New            
folder = "collisionLists"
openDir = os.getcwd()
fileToBeFound = os.path.join(openDir, folder)
if os.path.exists(fileToBeFound):
    ListFoundInFile = True
    os.chdir(fileToBeFound)
else:
    os.mkdir(folder)
    os.chdir(folder)
    ListFoundInFile = False
while ListFoundInFile == True:          
    subFolder = os.listdir()
    print("(C) -- Create New Collision List")
    listToUse = []
    for numbered, subFolder in enumerate(subFolder):
        if subFolder == "idFile.pkl":
                pass
        else:
            listToUse.append(subFolder)
            print(f"({numbered+1})", subFolder)
    folderToUse = input("Please Enter the Number File You Would Like to Use:")          
    if folderToUse == "C":
        ListFoundInFile = False
    else:
        if checkNotInt(folderToUse) == True:
            print("Invlaid Entry Please Try Again...")
        else:
            folderToUse = int(folderToUse)
            if checkRange(folderToUse, 0, (len(listToUse))) == True:
                print("Loading Selected Collision List...Please Wait...This Could Take a Minute...")
                fileToBeOpened = listToUse[folderToUse-1]
                os.chdir(fileToBeOpened)
                curDir = os.getcwd()
                filePath = os.path.join(curDir, fileToBeOpened)            
                with open(filePath, "rb") as fileBeingUsed:
                    tupleOfTupleList = pickle.load(fileBeingUsed)
                with open("idFile.pkl", "rb") as idFile:
                    idTuple = pickle.load(idFile)
                    pubKeyResult = idTuple[0]
                    AA = idTuple[1]
                break  
            else:
                print("Invlaid Entry Please Try Again...")      
else:
    ##Need invalid entry loop here NOT in functionality
    ##First check if input each(XX, YY) is hex or not then check if valid
    ##Both X and Y need a validHex check
    ##Use checkIfValidKey() and checkIfHex()

    XX = int((input("Please Enter Your Public Key X Coordinate In Hex Format:")),16)
    YY = int((input("Please Enter Your Public Key Y Coordinate In Hex Format:")),16)
    pubKeyResult = createKey(XX,YY)
    print("This is the Key you entered in base 10 integer format:",pubKeyResult)
    namedFile = str(input("Please Enter a Name for This Collision List:"))
    AA = int(input("Please Enter the Size of the Collision List you would like to Create. NOTE: The number you input will be doubled plus 1 then squared (If 'x' is the input then the formula is (2x+1)**2)(Example: input of 100 will OutPut - 40,401 total Keys Contained in the Multiples Collision List)(An input of 500 results in 1,002,001 keys)...Please Consider This and keep your input number below 10,000 to prevent overflow Errors caused By RAM capacity limitations. Best Performance around 1000...However Larger Nunbers are encouraged:"))
    AAA = (AA * 2)
    totalKeys = ((AAA+1) ** 2)
    namedAndNumbered = (str(namedFile) + "--" + str(totalKeys) + "--" + str(pubKeyResult.x))
    currentDir = os.getcwd()
    os.mkdir(namedAndNumbered)             
    os.chdir(namedAndNumbered)                  
    half = 57896044618658097711785492504343953926418782139537452191302581570759080747169
    N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
    third = 77194726158210796949047323339125271901891709519383269588403442094345440996225
    twosStartPubKey = pubKeyResult * ((half ** (AA))%N)
    print("Creating Collision List...Please Wait...")
    print("Total Number of Keys Contained In Collision List:", totalKeys)
    print("Please wait until the Below counter gets to:", (AAA+1))
    tupleOfTupleList = sortKeys(twosStartPubKey,AAA,AA,third,N)
    print("Saving Collision List To Disk...Please Wait")
    with open(namedAndNumbered, "wb") as openedFile:
        pickle.dump(tupleOfTupleList, openedFile)
    idFile = "idFile.pkl"
    idList = []
    idList.append(pubKeyResult)
    idList.append(str((AAA+1)**2))
    idTuple = tuple(idList)
    with open(idFile, "wb") as idedFile:
        pickle.dump(idTuple, idedFile)
#EasyGrid Search...
KeyFound = False
N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
os.chdir("..")
os.chdir("..")
if input("Would Your Like to Skip Lookup table Search? recomended only if you have already tried it on the key in the past and NOT found an answer...Please enter 'y' to Skip or 'n' to run the lookup table Search:") != "y":
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
        easyPrefix = int(str(easyKeyToFind)[:6])
        for privKeyTry in range(65535):
            firstRowCheck = binarySearch(tupleOfTupleList[easyPrefix-100000], easyKeyToFind)
            if firstRowCheck != -1:
                KeyFound = True
                recoveredKey = recoverFoundKey(firstRowCheck, privKey1, pubKeyResult, multiplyNum)
                print(firstRowCheck)
                print("This is the Found X-Coordinate:", firstRowCheck[0])
                print("Your Private Key is:", recoveredKey)
                with open("foundKeys.txt", "w") as foundKeyFile:
                    foundKeyFile.write("-- PrivateKey --")
                    foundKeyFile.write("%s" % recoveredKey)
                    foundKeyFile.write("-- PublicKey --")
                    foundKeyFile.write( "%s\n" % firstRowCheck[0])
                exit()
            else:
                tryPlace = tryPlace + easyGridPlace
                easyKeyToFind = tryPlace.x
                easyPrefix = int(str(easyKeyToFind)[:6])
                privKey1 = (privKey1 + easyGrid) % N
    #Reverse Grid Search...
    print("Checking Lookup Grid in Reverse from Half Point for Collision Match...Please wait...")
    for reverseEasyGrid in tqdm(tupleFirstRow,ascii=True,ncols=100,colour='#00ff00',unit='Rows',desc='GridRows'):
        privKeyR = reverseEasyGrid
        reverseTryPlace = multiplyNum((half-reverseEasyGrid)%N)
        reverseEasyGridPlace = multiplyNum(reverseEasyGrid)
        reverseEasyKeyToFind = reverseTryPlace.x
        reverseEasyPrefix = int(str(reverseEasyKeyToFind)[:6])
        for reversePrivKeyTry in range(65535):
            reverseFirstRowCheck = binarySearch(tupleOfTupleList[reverseEasyPrefix-100000], reverseEasyKeyToFind)
            if reverseFirstRowCheck != -1:
                KeyFound = True
                recoveredKeyR = recoverFoundKey(reverseFirstRowCheck, privKeyR, pubKeyResult, multiplyNum)
                print(reverseFirstRowCheck)
                print("This is the Found X-Coordinate:", reverseFirstRowCheck[0])
                print("Your Private Key is:", ((half - recoveredKeyR)%N))
                with open("foundKeys.txt", "w") as foundKeyFile:
                    foundKeyFile.write("-- PrivateKey --")
                    foundKeyFile.write("%s" % recoveredKeyR)
                    foundKeyFile.write("-- PublicKey --")
                    foundKeyFile.write( "%s\n" % reverseFirstRowCheck[0])
                exit()
            else:
                reverseTryPlace = (reverseTryPlace - reverseEasyGridPlace)
                reverseEasyKeyToFind = reverseTryPlace.x
                reverseEasyPrefix = int(str(reverseEasyKeyToFind)[:6])
                privKeyR = (privKeyR - reverseEasyGrid) % N
else:
    pass
#Enter easyCount Here...]
#Start Here at 65537 and half - 65537
print("Checking Easily Countable Positions for Collision Match...Please wait...")
print("Easy Count is Currently NOT enabled until Verion 2.0")
##Random Seach
print("Searching Randomly for a Collision Match...Please wait...")
while KeyFound != True:
    t = time.time()
    privKey = (int((((urandom(32))[2:])).hex(), 16))%N
    #privKey = 39249432821596846840936736167627457208319304603056442398667015916916341738904            #Comment Out previous private key and replace this one with a known private key for testing.
    privateKey1 = privKey-100000
    keyB = multiplyNum(privateKey1)
    keyG = multiplyNum(1)
    keyToFind = keyB.x
    prefix = int(str(keyToFind)[:6])
    for triedSpot in range(200000):
        hashIteration = tupleOfTupleList[prefix-100000]
        result = binarySearch(hashIteration, keyToFind)
        if result != -1:
            KeyFound = True
            recoveredKeyRandom = recoverFoundKey(result, privateKey1, pubKeyResult, multiplyNum)
            correctedKey = multiplyNum(recoveredKeyRandom)
            print(result)
            print("This is the Found X-Coordinate:", result[0])
            print("Your Private Key is:", recoveredKeyRandom)
            with open("foundKeys.txt", "w") as foundKeyFile:
                    foundKeyFile.write("-- PrivateKey --")
                    foundKeyFile.write("%s" % recoveredKeyRandom)
                    foundKeyFile.write("-- PublicKey --")
                    foundKeyFile.write( "%s\n" % result[0])
            exit()
        else:
            keyB = keyB + keyG
            keyToFind = keyB.x
            prefix = int(str(keyToFind)[:6])
            privateKey1 = privateKey1 + 1
    elapsed_time = time.time() - t
    print("Average Random Key Strings Created and Searched Per Second",(200000//elapsed_time),
            "Average Seconds per Round ", elapsed_time,  end='\r')
