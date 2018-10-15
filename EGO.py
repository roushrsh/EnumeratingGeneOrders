#Soroush
#Rosalind permutations problem. Had previously done it in a class forst first year I think.
#http://rosalind.info/problems/perm/

n = 6
theList = list(range (1, n+1))

def scramble(theList):
    listToReturn = [] #list to build off of
    if len(theList) == 0: #empty, no permutations possible
        return []
    if len(theList) == 1: #just one permutation possible
        return [theList]

    for x in range(len(theList)): #go from 0 to the length of the list
        value = theList[x] #save the value we're on, make it the first item
        remaining = theList[:x] + theList[x+1:] #take rest,
        for y in scramble(remaining):  #and rerun it all. For what's left...
            listToReturn.append([value] + y) #attach the front, to what's left
    return listToReturn #once done return it

listToPrint = scramble(theList)

count = 0
print len(listToPrint)
for x in listToPrint:
    for y in x:
        count = count +1
        print y,
        if (count%n ==0):
            print ("\n"),
