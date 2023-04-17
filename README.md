# hashAdder
An Optimized ECDSA Private Key Finding Tool

THis TOOL IS NOT READY YET!!!!
The above files are just examples to show the method I am using in the newest version....Please Check back later for updates....Hoping to have this ready by June 2023 at the latest as I am currently working on the privateKeyFinder Tool on my other page which is the origional version of this. HashAdder will be an optimized key finding tool that supposrts multiple Keys and very large lists saved to disk with an optimized search method...
the privateKeyFinder.py tool only supports single keys and stores the lists in memory with basic search queiries....
they both use lookup tables to make for very fast "hashes per second" but the privateKeyFinder.py version only uses multiples and divisions by 2 where hashAdder uses all combinations of multiples and divisions of 2 and 3 and will supposrt biased 2's or biased 3's...(will be explained in the video)

Please Check Back Periodically for updates...
Until then please Use this tool if you need to search for a key:
https://github.com/bakd247/ecdsaKeyFinder

Please See byteAdderOptimized.py for the current multiplication method (very fast ecdsa Module) and hashAdder.py for the current storage method(store by first digit)
Please also note that the final release is expected to be complete by the end of April 2023...hopefully sooner...any questions...please send me a message.

The code listed in these files is just a preview of the current algorithm currently being written to show the methods that 
allow for the reduction of complexity as well as much much faster run times compared ecdsaKeyFinder.

Note that in order to multiply a public key when the private key is NOT known...replacing the x and y coordinates in the ecdsaModule.py file...
you can easily get the correct answer just as if you had multiplied the private key by the "origional generators" (aka "g") x and y coordinates...
Next the factors of the "unknonwn key" are created and searched for a match using random numbers multipled by the original generator x and y...

(origional generator = (x = 79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798, y = 483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8))
(Can be confirmed with any ecdsa Library)
(in order to multiply an unknown key...the above x and y coordinates are replaced with the public key in question)

"unknown key"= a key which the private key is NOT known and is to be recovered using this tool
aka a base 10 number between 1 and 115792089237316195423570985008687907852837564279074904382605163141518161494337

n = 115792089237316195423570985008687907852837564279074904382605163141518161494337

"n-1" is the largest possible ECDSA private key and "1" is the smallest

The fileCreator.py file is the method for creating files to store the keys accoriding to the first 4 digits of the x-coordinate...
(The Finding algorithm will use suffixes and each file will be sorted in accending order to allow for a reducion to the search space for each search try)
The ecdsaModule.py file is the a basic ecdsa implementation that uses the tinyEC library to create public keys...
instead of adding up the binary positions of a key according to the binary of the multiple like the "tinyEC" library does...

the tinyEC version is used in combiantion with the multiplyNum.py file to construct a "byte array" lookup table....reducing the complexity of each
multiplication to (Theta(log32(n//2))) from (Theta(log2(n//2))) for all keys by reducing the number of additions from 255 down to 31...

This is now complete and can be used by importing the method into a virtual environment or by just using the multiplyNum() function at the end of the file with the number you would like to use as a multiple / private Key...

The idea is to use tuples as dictionaries to ensure the fastest possible lookup time as a result.
And to show that by taking a multiple(number the publicKey is to be multiplied by) and changing it to a 32 byte array...the elements in this array
can then be looked up according to the iteration in the array and dictionary respectively.
The hashAdder.py file is the method for storing the keys to give a status bar as well...mostly used for benchmarking

The intentionis to use both multithreading and multiprocessing in order to calculate all of the multiples of 2 and 3 as well as all of the 
divisions of 2 and 3....

Once the keys are save to file in an organized and "quick search" fashion
the program will then search for a match using random numbers multipled by the original generator x and y ((x = 79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798, y = 483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8))
only ONE match is needed to recover ANY key...

please check out the youtube channel which explains all of this code as well as much more "Math behind Bitcoin's ECDSA Algorithm" videos.

https://www.youtube.com/@quitethecontrary1846

If you would like to use the current version (very slow and gives wrong number of keys per second but is still an effective way to search for a key)
which is the mainpremise that the hashAdder version is derived from...

you can see it here:
https://github.com/bakd247/ecdsaKeyFinder

Note: you must have tinEC.py preinstalled to use this tool

Thank You
