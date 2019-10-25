import os
import sys

entryFileName = sys.argv[1]
nOfFrames = int(sys.argv[2])

path = os.getcwd()
entryPath = path + "\\Test files\\" + entryFileName

nOfRefs = 0
refString = []
frames = nOfFrames*[-1]

def getRefString():
    file = open(entryPath,'r')
    n = 0
    
    for line in file:
        line2 = line.strip()
        lineList = line2.split(' ')
        refString.append(int(lineList[0]))
        n += 1
    file.close()
    return n

def indexFromToEnd(refString, currTime, ref):
    for t in range(currTime, len(refString)):
        if(refString[t] == ref):
            return t
    return -1

def indexFromBegToIndexInv(refString, currTime, ref):
    for t in range(currTime-1, -1,-1):
        if(refString[t] == ref):
            return t
    return -1
        
def findAPageToBeReplacedOPT (currTime, refString, frames):
    biggerIndex = -1
    pageRef = -1
    
    for ref in frames:
        if (ref in refString[currTime:]):
            indexRef = indexFromToEnd(refString, currTime , ref)
            if(indexRef > biggerIndex):
                biggerIndex = indexRef
                pageRef = ref
        else:
            pageRef = ref
            break
    return pageRef, frames.index(pageRef)

def findAPageToBeReplacedLRU (currTime, refString, frames):
    smallerIndex = nOfRefs*2
    pageRef = -1
    
    for ref in frames:
        if  ref in refString[:currTime-1]:
            indexRef = indexFromBegToIndexInv(refString, currTime, ref)
            if(indexRef < smallerIndex):
                smallerIndex = indexRef
                pageRef = ref
        elif not(ref in refString[:currTime-1]):
            pageRef = ref
            break
    return pageRef, frames.index(pageRef)

def findAPageToBeReplacedFIFO(refQueue,frames):
    ref = refQueue.pop(0)
    index = frames.index(ref)

    return ref, index

def fifo (refString, frames, nOfRefs):
    refQueue = []
    nOfFaults = 0
    time = 0

    for ref in refString:
        time += 1
        if not(ref in frames):
            nOfFaults += 1
            refQueue.append(ref)
            if(-1 in frames):
                emptySpace = frames.index(-1)
                frames[emptySpace] = ref
            else:
                pageRef, pageIndex = findAPageToBeReplacedFIFO(refQueue,frames)
                frames[pageIndex] = ref

    return nOfFaults

def lru (refString, frames, nOfRefs):
    nOfFaults = 0
    time = 0
    faultTime = 1
    frameRefTime = nOfFrames * [-1]
    
    for ref in refString:
        time += 1
        if not(ref in frames):
            nOfFaults += 1
            if(-1 in frames):
                emptySpace = frames.index(-1)
                frames[emptySpace] = ref
                frameRefTime[emptySpace] = time
            else:
                pageRef, pageIndex = findAPageToBeReplacedLRU(time, refString, frames)
                frames[pageIndex] = ref
                frameRefTime[pageIndex] = time

    return nOfFaults

def opt (refString, frames, nOfRefs):
    nOfFaults = 0
    time = 0
    
    for ref in refString:
        time += 1
        if not(ref in frames):
            nOfFaults += 1
            if(-1 in frames):
                emptySpace = frames.index(-1)
                frames[emptySpace] = ref
            else:
                pageRef, pageIndex = findAPageToBeReplacedOPT(time, refString, frames)
                frames[pageIndex] = ref
                
    return nOfFaults

nOfRefs = getRefString()
nOfFaultsOPT = opt(refString.copy(), frames.copy(), nOfRefs)
nOfFaultsLRU = lru(refString.copy(), frames.copy(), nOfRefs)
nOfFaultsFIFO = fifo(refString.copy(), frames.copy(), nOfRefs)
print(str(nOfFrames) + " quadros, " + str(nOfRefs) + " refs: FIFO: " + str(nOfFaultsFIFO) + " PFs, LRU: " +
      str(nOfFaultsLRU) + " PFs, OPT: " + str(nOfFaultsOPT) + " PFs")
