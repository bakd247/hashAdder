# hashAdder
An Optimized ECDSA Private Key Finding Tool

Please note that the code listed in these files is just a preview of the current algorithm currently being written to show the methods that 
allow for the reduction of complexity as well as much much faster run times compared ecdsaKeyFinder.

Note that in order to multiply a public key when the private key is NOT known...replacing the x and y coordinates in the ecdsaModule.py file...
you can easily get the correct answer just as if you had multiplied the private key by the "origional generators" (aka "g") x and y coordinates...

(origional generator = (0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798, 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8))

Next the factors of the "unknonwn key" are created and searched for a match using random numbers multipled by the original generator x and y...

"origional generator" or "g"= the x and y coordinated currently in the ecdsaModule.py file multiplied by 1. (Can be confirmed with any ecdsa Library)
origional generator = (0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798, 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
(in order to multiply an unknown key...the above x and y coordinates are replaced with the public key in question)

"unknown key"= a key which the private key is NOT known and is to be recovered using factors of the key within the 
modular form field - (1:n-1)

The fileCreator.py file is the method for creating files to store the keys accoriding to the first 4 digits of the x-coordinate...
(The Finding algorithm will use suffixes and each file will be sorted in accending order to allow for a reducion to the search space for each search try)
The ecdsaModule.py file is the a basic ecdsa implementation that uses the tinyEC library to create public keys...
instead of adding up the binary positions of a key according to the binary of the multiple like the "tinyEC" library does...
the tinyEC version is used in combiantion with the multiplyNum.py file to construct a "byte array" lookup table....reducing the complexity of each
multiplication to (Theta(log32(n//2))) from (Theta(log2(n//2))) for all keys by reducing the number of additions from 255 down to 31...
The idea is to use tuples as dictionaries to ensure the fastest possible lookup time as a result.
And to show that by taking a multiple(number the publicKey is to be multiplied by) and changing it to a 32 byte array...the elements in this array
can then be looked up according to the iteration in the array and dictionary respectively.
The hashAdder.py file is the method for storing the keys to give a status bar as well...mostly used for benchmarking

The intentionis to use both multithreading and multiprocessing in order to calculate all of the multiples of 2 and 3 as well as all of the 
divisions of 2 and 3....
Once the keys are save to file in an organized and "quick search" fashion
the program will then search for a match using random numbers multipled by the original generator x and y ((0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798, 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8))
only ONE match is needed to recover ANY key...

please check out the youtube channel which explains all of this code as well as much more "Math behind Bitcoin's ECDSA Algorithm" videos.

https://www.youtube.com/@quitethecontrary1846

If you would like to use the current version (very slow and gives wrong number of keys per second but is still an effective way to search for a key)
which is the mainpremise that the hashAdder version is derived from...

you can see it here:
https://github.com/bakd247/ecdsaKeyFinder

Thank You
