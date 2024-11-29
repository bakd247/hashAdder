from tinyec.ec import SubGroup, Curve
from tqdm import tqdm, trange
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
    
#Define RecoverFoundKey    
def recoverFoundKey(result, privateKey1):
    half = 57896044618658097711785492504343953926418782139537452191302581570759080747169
    N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
    third = 77194726158210796949047323339125271901891709519383269588403442094345440996225
    twosResult = result[1][0]
    threesResult = result[1][1]
    if twosResult >= 0 and threesResult >= 0:
        foundPrivateKey = (privateKey1 * (((half ** twosResult)*(third ** threesResult))%N))%N
        return(foundPrivateKey)
    elif twosResult < 0 and threesResult >= 0:
        twosResult = 0 - twosResult
        foundPrivateKey = (privateKey1 * (((2 ** twosResult)*(third ** threesResult))%N))%N
        return(foundPrivateKey)
    elif twosResult >= 0 and threesResult < 0:
        threesResult = 0 - threesResult
        foundPrivateKey = (privateKey1 * (((half ** twosResult)*(3 ** threesResult))%N))%N
        return(foundPrivateKey)
    elif twosResult < 0 and threesResult < 0:
        twosResult = 0 - twosResult
        threesResult = 0 - threesResult
        foundPrivateKey = (privateKey1 * (((2 ** twosResult)*(3 ** threesResult))%N))%N
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