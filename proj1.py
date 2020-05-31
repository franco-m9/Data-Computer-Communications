import binascii
import sys
import math

checker = 0
count = 0
f = sys.stdin	
numArray = []
binaryArray = []
afterfirst = 0
sum = 0
variance = 0
storageArray = []

while(count != 10000):
	
	list = float(f.readline())
	numArray.append(list)
	count += 1


for num in numArray:
	sum = sum + num
 

mean = sum / 10000

for num2 in range(0,len(numArray)):
        variance += ((numArray[num2] - mean) * (numArray[num2] - mean))

variance = variance / len(numArray)
stddev = math.sqrt(variance)
noise_threshold = mean * 8 + stddev * 16

#print(noise_threshold) 3544.311247531755

while(checker!=1):
	list = float(f.readline())
	if(list>=noise_threshold):
		checker = 1
	
	count += 1


#Line that the preamble symbol starts around 1014941
#Value of pulse found by line 5140.6195
#when the first "1" in binary begins 1015841

count += 800
#801
for i in range(1, 800):
	list = float(f.readline())

lchecker = 0
while(lchecker==0):
	list = f.readline()
	if(list == ''):
		break
	list = float(list)
	storageArray.append(list)

#print(storageArray)
#print(len(storageArray))
b = 0
while(b < len(storageArray)):
	if(storageArray[b]>=noise_threshold):
		binaryArray.append(0)
		b += 100
	elif(storageArray[b+50]>=noise_threshold):
		binaryArray.append(1)
		b += 100
	else:
		break	


#print(binaryArray)
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
