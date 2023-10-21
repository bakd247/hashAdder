from tinyec.ec import SubGroup, Curve
from tqdm import tqdm, trange

print("                                                  ")
print("                                                  ")
print("\033[0;32m _               _        _       _     _\033[00m")
print("\033[0;32m| |__   __ _ ___| |__    / \   __| | __| | ___ _ __\033[00m")
print("\033[0;32m| '_ \ / _` / __| '_ \  / _ \ / _` |/ _` |/ _ \ '__|\033[00m")
print("\033[0;32m| | | | (_| \__ \ | | |/ ___ \ (_| | (_| |  __/ |\033[00m")
print("\033[0;32m|_| |_|\__,_|___/_| |_/_/   \_\__,_|\__,_|\___|_|\033[00m")
print("                                                  ")
print("                                                  ")


keyIters= input("Please Enter the number of Key Iterations you would like to Store:")

def createKey(X,Y):
    name = 'secp256k1'
    p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
    n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
    a = 0x0000000000000000000000000000000000000000000000000000000000000000
    b = 0x0000000000000000000000000000000000000000000000000000000000000007
    g = (X,Y)
    h = 1
    
    if (((X * X * X)%p) + 7) != ((Y * Y)%p):
        print("The Public Key X and Y Coordinates You Entered Are NOT Valid...NOTE: DO NOT Include 02, 03 Or 04 At The Begining Of The X Coordinate And Make Sure You Are Using Hexidecimal Format. If You Need Assistance...Please Contact Technical Support...Please Try Again...Enter Valid X and Y Coordinates For Your Public Key...")
        exit()
    else:
        curve = Curve(a, b, SubGroup(p, g, n, h), name)
        pubKey= curve.g*1
        return(pubKey.x)

XX = int((input("Please Enter Your Public Key X Coordinate In Hex Format:")),16)
YY = int((input("Please Enter Your Public Key Y Coordinate In Hex Format:")),16)

print(createKey(XX,YY))
##Multiply

def keyMultiply(iterations):
    intIter = ((int(iterations))//2)
    two = 2
    three = 3
    n= 115792089237316195423570985008687907852837564279074904382605163141518161494337
    list2 = []
    list3 = []
    list4 = []
    for iter in trange(intIter,total=intIter,ascii=True,ncols=100,colour='#00ff00',unit='Multiples',desc='Twos'):
        A = (two ** iter)%n
        list2.append(A)
    
    for iter1 in trange(intIter,total=intIter,ascii=True,ncols=100,colour='#00ff00',unit='Multiples',desc='Threes'):
        B = (three ** iter1)%n
        list3.append(B)
    
    for iter2 in tqdm(list2,ascii=True,ncols=100,colour='#00ff00',unit='Multiples',desc='Combinations'):
        for iter3 in list3:
            C = (iter2 * iter3)%n
            if C in list4:
                pass
            else:
                list4.append(C)   
    list.sort(list4)
    for i in list4:
        AA = i
        with open('Multiples.txt', 'a') as e:
            e.write("%s\n" % AA)
keyMultiply(keyIters)
##Divide

def keyDivide(iterations1):
    intIter1 = ((int(iterations1))//2)
    two = 57896044618658097711785492504343953926418782139537452191302581570759080747169
    three = 77194726158210796949047323339125271901891709519383269588403442094345440996225
    n= 115792089237316195423570985008687907852837564279074904382605163141518161494337
    listD2 = []
    listD3 = []
    listD4 = []
    for iterA in trange(intIter1,total=intIter1,ascii=True,ncols=100,colour='#00ff00',unit='Divisions',desc='DivideByTwo'):
        A1 = (two ** iterA)%n
        listD2.append(A1)
    
    for iter1A in trange(intIter1,total=intIter1,ascii=True,ncols=100,colour='#00ff00',unit='Divisions',desc='DivideByThree'):
        B1 = (three ** iter1A)%n
        listD3.append(B1)
    
    for iter2A in tqdm(listD2,ascii=True,ncols=100,colour='#00ff00',unit='Divisions',desc='CombinationDivisions'):
        for iter3A in listD3:
            C1 = (iter2A * iter3A)%n
            if C1 in listD4:
                pass
            else:
                listD4.append(C1)   
    list.sort(listD4)
    for i in listD4:
        AA1 = i
        if AA1 == 1:
            continue
        with open('Divisors.txt', 'a') as f:
            f.write("%s\n" % AA1)
keyDivide(keyIters)
print("Finished Creating Mulitples")
