# hashAdder
an optimized ecdsa private key finding tool

Please note that the code listed in these files is just a preview of the current algorithm I am in the process of writing to show the methods I am introducing 
to allow for reduction of complexity as well as much much faster run times.

I intend on using both multithreading and multiprocessing in order to calculate all of the multiples of 2 and 3 as well as all of the divisions of 2 and 3....
then I will be dividing the half point((n+1)//2) up in a clever way to locate a key according to its factors...
only ONE match is needed to recover ANY key...

please check out my youtube channel where I explain all of this code as well as much more "Math behind Bitcoin's ECDSA Algorithm" videos.
https://www.youtube.com/@quitethecontrary1846

If you would like to use the current version (very slow and gives wrong number of keys per second) which is an effective way to search for a key and is the main
premise that the hashAdder version is derived from...you can see it here:

https://github.com/bakd247/ecdsaKeyFinder

Thank You
