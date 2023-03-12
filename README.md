# hashAdder
an optimized ecdsa private key finding tool

Please note that the code listed in these files is just a preview of the current algorithm I am in the process of writing to show the methods I am introducing 
to allow for reduction of complexity as well as much much faster run times.

The fileCreator.py file is the method for creating files to store the keys accoriding to the first 4 digits of the x-coordinate...
(The Finding algorithm will use suffixes and each file will be sorted in accending order to allow for a reducion to the search space for each search try)
The ecdsaModule.py file is the a basic ecdsa implementation that uses the tinyEC library to create public keys...
instead of adding up the binary positions of a key according to the binary of the multiple like the "tinyEC" library does...
the tinyEC version is used in combiantion with the multiplyNum.py file to construct a "byte array" lookup table....reducing the complexity of each multiplication to (Theta(log(base32)*(n//2))) for all keys by reducing the number of additions from 255 down to 31...by using tuples as dictionaries to ensure the fastest possible lookup time as a result.
by taking a multiple and changing it to a 32 byte array...the elements in this array can then be looked up according to the iteration in the array and dictionary respectively.
The hashAdder.py file is the method for storing the keys to give a status bar as well...mostly used for benchmarking

I intend on using both multithreading and multiprocessing in order to calculate all of the multiples of 2 and 3 as well as all of the divisions of 2 and 3....
then I will be dividing the half point((n+1)//2) up in a clever way to locate a key according to its factors...
only ONE match is needed to recover ANY key...

please check out my youtube channel where I explain all of this code as well as much more "Math behind Bitcoin's ECDSA Algorithm" videos.
https://www.youtube.com/@quitethecontrary1846

If you would like to use the current version (very slow and gives wrong number of keys per second) which is an effective way to search for a key and is the main
premise that the hashAdder version is derived from...you can see it here:

https://github.com/bakd247/ecdsaKeyFinder

Thank You
