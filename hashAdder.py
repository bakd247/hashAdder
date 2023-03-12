from tinyec.ec import SubGroup, Curve
from tqdm import trange
import csv
import time

t = time.perf_counter()
print("                                                  ")
print("                                                  ")
print("\033[0;32m _               _        _       _     _\033[00m")
print("\033[0;32m| |__   __ _ ___| |__    / \   __| | __| | ___ _ __\033[00m")
print("\033[0;32m| '_ \ / _` / __| '_ \  / _ \ / _` |/ _` |/ _ \ '__|\033[00m")
print("\033[0;32m| | | | (_| \__ \ | | |/ ___ \ (_| | (_| |  __/ |\033[00m")
print("\033[0;32m|_| |_|\__,_|___/_| |_/_/   \_\__,_|\__,_|\___|_|\033[00m")
print("                                                  ")
print("                                                  ")

def sortKeys():
    name = 'secp256k1'
    p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
    n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
    a = 0x0000000000000000000000000000000000000000000000000000000000000000
    b = 0x0000000000000000000000000000000000000000000000000000000000000007
    g = (0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798, 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
    h = 1

    curve = Curve(a, b, SubGroup(p, g, n, h), name)
    PubKey = curve.g*1

    Multiples = []
    multiples = tuple(Multiples)
    for mult in range(10000):
        Multi = (2**mult)%n
        if Multi < 57896044618658097711785492504343953926418782139537452191302581570759080747169:
            Multi = n- Multi
        else:
            Multi = Multi
        Multiples.append(Multi)
        

    for multiple in trange(len(Multiples),total=len(Multiples),ascii=True,ncols=100,colour='#00ff00',unit='KeySort',desc='Sorting Keys'):
        pubKey = PubKey * multiple
        A = str(pubKey.x)[:2]
        with open('%s.csv' % A, 'a') as e:
            e.write("%s" % pubKey.x)
            e.write(str(","))
            e.write("%s\n" % multiple)
    elapsed_time = time.perf_counter()          
    print("                                                  ")
    print("Finished in" ,elapsed_time-t, "seconds")

sortKeys()
