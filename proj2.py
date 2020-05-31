import binascii
import sys
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

checker = 0
count = 0
f = open("proj1_testsignal1","r")
ff = open("proj2_noisesignal1","r")
numArray = []
binaryArray = []
afterfirst = 0
sum = 0
variance = 0
storageArray = []
cleanArray = []
noiseArray = []
combinedArray = []
preamble = 0
#clean = np.loadtxt("proj1_testsignal1", dtype=np.float)
#dirty = np.loadtxt("proj2_noisesignal1", dtype=np.float)


ParityMatrix = np.array([[1,0,1],[1,1,1],[1,1,0],[0,1,1],[1,0,0],[0,1,0],[0,0,1]])

isFinished = 0
while(isFinished==0):
	list = f.readline()
	if(list == ''):
		break	
	list = float(list)
	cleanArray.append(list)
	list = ff.readline()
	list = float(list)
	noiseArray.append(list)



size = len(cleanArray)
index = 0

while(index<size):
	storage = cleanArray[index] + noiseArray[index]
	combinedArray.append(storage)
	index += 1


#plt.plot(combinedArray)
#plt.show()
#print(combinedArray[1284447-1])
while(count != 10000):
	sum = sum + combinedArray[count]
	count += 1


mean = sum / 10000

for num2 in range(0,10000):
        variance += ((combinedArray[num2] - mean) * (combinedArray[num2] - mean))


variance = variance / 10000
stddev = math.sqrt(variance)
noise_threshold = mean * 8 + stddev * 16


#print(noise_threshold) 3544.311247531755

preamblefound = 0
while(checker == 0):
	if(combinedArray[preamblefound]>=noise_threshold):
		checker = 1
		preamble = preamblefound
		break
	
	preamblefound += 1


#Line that the preamble symbol starts around 1014939 (+1 , remember its stored in array!)
#Value of pulse found by line 4479.4309

preamble += 800

temp = -1
temp2 = -1

'''
while(preamble < len(combinedArray)):
	if(combinedArray[preamble]>=noise_threshold):
		temp = combinedArray[preamble]
	if(combinedArray[preamble+50]>=noise_threshold):
		temp2 = combinedArray[preamble+50]
	if(temp>temp2):
		binaryArray.append(0)
	elif(temp2>temp):
		binaryArray.append(1)

	temp = -1
	temp2 = -1
	preamble += 100
'''

ty = 0
final = -1
tx = 50
final2 = -1
while(preamble < len(combinedArray)):
	while(ty<10):
		if(combinedArray[preamble+ty]>=noise_threshold):
			temp = combinedArray[preamble+ty]
			if(temp>final):
				final = temp
		ty += 1
	
	while(tx<60):
		if(combinedArray[preamble+tx]>=noise_threshold):
			temp2 = combinedArray[preamble+tx]
			if(temp2 > final2):
				final2 = temp2
		tx += 1

	if(final>final2):
		binaryArray.append(0)
	elif(final2>final):
		binaryArray.append(1)
	ty = 0
	tx = 50
	temp = -1
	temp2 = -1
	final = -1
	final2 = -1
	preamble += 100	

'''
see = 42
while(see<56):
	print(binaryArray[see])
	see += 1
'''

#print(binaryArray)


bitchecker = 0
paritychecker = []
r = 0
q = 0
which = -1
while(r<len(binaryArray)):
	bitchecker = (binaryArray[r] * ParityMatrix[0][0])
	bitchecker += (binaryArray[r+1] * ParityMatrix[1][0])
	bitchecker += (binaryArray[r+2] * ParityMatrix[2][0])
	bitchecker += (binaryArray[r+3] * ParityMatrix[3][0])
	bitchecker += (binaryArray[r+4] * ParityMatrix[4][0])
	bitchecker += (binaryArray[r+5] * ParityMatrix[5][0])
	bitchecker += (binaryArray[r+6] * ParityMatrix[6][0])
	bitchecker = bitchecker % 2
	paritychecker.append(bitchecker)
	bitchecker = (binaryArray[r] * ParityMatrix[0][1])
	bitchecker += (binaryArray[r+1] * ParityMatrix[1][1])
	bitchecker += (binaryArray[r+2] * ParityMatrix[2][1])
	bitchecker += (binaryArray[r+3] * ParityMatrix[3][1])
	bitchecker += (binaryArray[r+4] * ParityMatrix[4][1])
	bitchecker += (binaryArray[r+5] * ParityMatrix[5][1])
	bitchecker += (binaryArray[r+6] * ParityMatrix[6][1])
	bitchecker = bitchecker % 2
	paritychecker.append(bitchecker)
	bitchecker = (binaryArray[r] * ParityMatrix[0][2])
	bitchecker += (binaryArray[r+1] * ParityMatrix[1][2])
	bitchecker += (binaryArray[r+2] * ParityMatrix[2][2])
	bitchecker += (binaryArray[r+3] * ParityMatrix[3][2])
	bitchecker += (binaryArray[r+4] * ParityMatrix[4][2])
	bitchecker += (binaryArray[r+5] * ParityMatrix[5][2])
	bitchecker += (binaryArray[r+6] * ParityMatrix[6][2])
	bitchecker = bitchecker % 2
	paritychecker.append(bitchecker)
	#print(paritychecker)
	if(paritychecker != [0,0,0]):
		while(q<7):
			if(paritychecker==[1,0,1]):
				which = 0
			elif(paritychecker==[1,1,1]):
				which = 1
			elif(paritychecker==[1,1,0]):
				which = 2
			elif(paritychecker==[0,1,1]):
				which = 3
			elif(paritychecker==[1,0,0]):
				which = 4
			elif(paritychecker==[0,1,0]):
				which = 5
			elif(paritychecker==[0,0,1]):
				which = 6
			q += 1

			if(binaryArray[r+which] == 0):
				binaryArray[r+which] = 1
			elif(binaryArray[r+which] == 1):
				binaryArray[r+which] = 0
 	
	paritychecker.clear()
	q = 0
	r += 7


starter = 0
increment = 0
bytecomplete = 0
g = 0

while(g<len(binaryArray)-4):
	increment += 1
	if(starter==0):
		message = str(binaryArray[g])
		bytecomplete += 1
		starter = 1
	elif(increment>4):
		g += 2
		increment = 0
	elif(starter==1):
		message += str(binaryArray[g])
		bytecomplete += 1
	if(bytecomplete==8):
		n = int(message,2)
		s = binascii.unhexlify('%x' % n)
		s = str(s)
		print(s[2],end = '')
		bytecomplete = 0
		starter = 0
		increment = 0
		g += 3
	g += 1


print('\n')

f.close()
ff.close()
