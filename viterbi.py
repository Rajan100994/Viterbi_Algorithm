#start to hot
#start to cold
import sys
str1= sys.argv[1]
#str1= "331123312"
inputSequence=[]

for i in range(len(str1)):
    inputSequence.append(int(str1[i]))

print("\nInput Sequence : ",inputSequence)

#Starting probabilities
pStart = [0.8,0.2]
finalTags = ["Hot","Cold"]
#probabilities from hot to hot and cold and cold to hot and cold
pTransition = [[0.7,0.3],[0.4,0.6]]

#probabilities of observables(1,2,3) given hot and cold
pObs = [[0.2,0.4,0.4],[0.5,0.4,0.1]]

#declaring trellis and number of states(hot,cold)
trellis=[]
trePrev=[]
noStates = 2

#initialize trellis
for i in range(noStates):
    trellis.append([0])
    trePrev.append([])

#filling out column 1
maxProb = 0
maxIndex = 0

#filling out the first column
for i in range(noStates):
    trellis[i][0] = pStart[i]*(pObs[i][inputSequence[0]-1])
    tempMax = trellis[i][0]
    if tempMax>maxProb :
        maxProb=tempMax

#filling out the rest of the columns
for j in range(1,len(inputSequence)):
    for i in range(noStates):
        tempProb=[]
        for pre in range(noStates):
            tempProb.append(trellis[pre][j-1]*pTransition[pre][i]*(pObs[i][inputSequence[j]-1]))
        trellis[i].append(max(tempProb))
        trePrev[i].append(tempProb.index(max(tempProb)))

j=len(inputSequence)-1
tempProb=[]
for i in range(noStates):
    tempProb.append(trellis[i][j])

#print(tempProb)
maxLast =max(tempProb)
maxLastIndex = tempProb.index(max(tempProb))

#print(trePrev)
#print(maxLastIndex)
backtrace = [maxLastIndex]

for j in range((len(inputSequence)-1),0,-1):
    backtrace.append(trePrev[maxLastIndex][j-1])
    maxLastIndex=trePrev[trePrev[maxLastIndex][j-1]][j-2]

#print(backtrace)

mostProbableIndex = backtrace[::-1]
mostProbableSeq=[]

for i in range(len(mostProbableIndex)):
    mostProbableSeq.append(finalTags[mostProbableIndex[i]])

print("Most Probable Sequence : ",mostProbableSeq)
print("Probability of the sequence : ",maxLast,"\n")