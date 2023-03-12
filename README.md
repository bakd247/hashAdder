# hashAdder
an optimized ecdsa private key finding tool

Please note that the code listed in these files is just a preview of the current algorithm I am in the process of writing to show the methods I am introducing 
to allow for reduction of complexity as well as much much faster run times.

I intend on using both multithreading and multiprocessing in order to calculate all of the multiples of 2 and 3 as well as all of the divisions of 2 and 3....
then I will be dividing the half point((n+1)//2) up in a clever way to locate a key according to its factors...
only ONE match is needed to recover ANY key...

The fileCreator.py file is the method for creating files to store the keys accoriding to the first 4 digits of the x-coordinate...
(The Finding algorithm will use suffixes and each file will be sorted in accending order to allow for a reducion to the search space for each search try)
The ecdsaModule.py file is the a basic ecdsa implementation that uses the tinyEC library to create public keys...this is used during initialization in combination with the multiplyNum.py file to allow for 31 additions maximum per multiplication instead of 255 which the tinyEC version does...
The multiplyNum.py file is the method for storing a "byte array" lookup table...
The hashAdder.py file is the method for storing the keys to give a status bar as well...mostly used for benchmarking


please check out my youtube channel where I explain all of this code as well as much more "Math behind Bitcoin's ECDSA Algorithm" videos.
https://www.youtube.com/@quitethecontrary1846

If you would like to use the current version (very slow and gives wrong number of keys per second) which is an effective way to search for a key and is the main
premise that the hashAdder version is derived from...you can see it here:

https://github.com/bakd247/ecdsaKeyFinder

Thank You
