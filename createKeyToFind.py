from tinyec.ec import SubGroup, Curve
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