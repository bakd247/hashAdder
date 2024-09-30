# hashAdder

Version 1.3 is the Most current Working Release...

An Optimized ECDSA Private Key Finding Tool

THIS TOOL IS FINALLY READY AND WORKING!!!!

Currently the hashAdder.py file multiplies and divides by 2 and 3 for the number of iterations input by the user and organizes the public Key x-coordinate results by the first 6 digits.
this allows for much larger collision lists to exsist while only having to search the keys that have the same prefix as well as much faster binary search times per iterative round.

The program will prompt to input a number for the sizxe of the collision list desired. This number will be double and then squared to give a total number of keys contained in the list.
Example: input of 100 will output 40000 keys because ((100*2) **2)= 40000. Please remmeber this when using the program as very large numbrs will take much longer to produce a collision list.
NOTE: This input does NOT account for memory overflow so keep the inputs at or below 1,000.

Please See wordAdder.py for the current multiplication method (very fast ecdsa Module) and hashAdder.py for the current storage method(store by first four digits)

the tinyEC version is used in combiantion with the multiplyNum.py file to construct a "byte array" lookup table....reducing the complexity of each
multiplication to (Theta(log(base_65536)*(n//2))) from (Theta(log2*(n//2))) for all keys by reducing the number of additions from 255 down to 15...

This is an exact 2.5 X speed increase per operation using this addition loop (base 65536) compared to a regular binary(base2) addition loop that is used by default...

The idea of hashAdder is to use tuples as dictionaries to ensure the fastest possible lookup time as a result. While providing every multiple of 2 and 3 to increase the key search space size and to show that by taking a multiple(number the publicKey is to be multiplied by) and changing it to a 32 byte array...the elements in this array
can then be looked up according to the iteration in the array and dictionary respectively.
The hashAdder.py file is the method for storing the keys to give a status bar as well...mostly used for benchmarking

The intention with the next release is to use both multithreading and multiprocessing in order to calculate all of the multiples of 2 and 3 as well as all of the 
divisions of 2 and 3....

All Collision Lists are currently Saved to memory and must be recreated everytime the software is run. Version 2.0 intends to solve this by writeing collision lists to file and reading to memory at start.
Version 2.0 will also supoport multiple keys and thier multiples. The current version only looks for 1 key along with its multiples

please check out the youtube channel which explains all of this code as well as much more "Math behind Bitcoin's ECDSA Algorithm" videos.

https://www.youtube.com/@quitethecontrary1846

Video showing hashAdder in action as well as a detailed explaination of how it works comming to the youTube channel soon...

Please download the first release of hashAdder 1.0 and run hashAdder.py using python3 from the command line / terminal
NOTE: do not run within virtual environments such as within visual studio. this Causes memory error after running for a long time. In order for the program to run for a long enough time to ever hope to find a key you MUST run the program contained in its own VM or from a terminal. Admin privledges should not be required but are recomended to best use of hardware resources.

Note: you must have tinyEC.py preinstalled to use this tool
Download the files into a sinlge folder which contains all of the files listed above. Then run the program using python 3 and follow the prompts.

Thank You
