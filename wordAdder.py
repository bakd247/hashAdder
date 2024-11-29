from tinyec.ec import SubGroup, Curve
from tqdm import tqdm
import pickle
# List parameters for ecdsa Curve
with open("wordGrid.pkl", "rb") as gridFile:
    grid = pickle.load(gridFile)
##Define Multiply Function
def multiplyNum(number):
    N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
    ##Read in the integer input as big endian hex 4 hex digits at a time
    array = ((number)%N).to_bytes(32, "big")
    counter = 0
    hexLists = []
    posList = []
    for count in range(16):
        element = (hex(array[counter])[2:])+(hex(array[counter+1])[2:])
        hexLists.append(element)
        counter += 2
    ##Then Reverse the "words" to be looked up
    ## Then using the grid above...lookup each "hex Word""
    hexLists.reverse()
    tupleHexList = tuple(hexLists)
    for itered, product in enumerate(tupleHexList):
        position = (grid[itered][(int(product, 16))])
        ##Each position is looked up according to its index, and each "hex word" is converted to an integer to give its index
        if position == 0:
            pass
        else:
            posList.append(position)
        tuplePos = tuple(posList)
    ##The positions are added to a list to be added together accounting for zeros along the way    
    if len(tuplePos) < 1:
        return("Infinity and Beyond")
    else:
        total = tuplePos[0]
        if len(tuplePos) < 2:
            return(total)            
        else:
            for k in tuplePos[1:]:
                total = total + k
            return(total)
##The result is exactly the same as any binary addition but this acheives the same result using a maximum of 15 additions per operation
##Where 256 bit binary addition takes 255 addition steps maximum...so this is an exact 17 X speed increase per operation