from collections import deque

i = 0
j = 0
window = 0
time = 0
retransmitcheck = 0
dataArray = []
ackArray = []
ackNum = deque()
newFrame = deque()
oldFrame = deque()
ackTransmit = deque()
ackTransmit.append(0)
frameTransmit = deque()
tempt = deque()
frameNum = 0
delaychecker = -1
checker = 0
f = open("ACK_GOOD","r")
ff = open("DATA_GOOD","r")
recounter = 0
retimer = deque()
x = 0
p = 0
case = 0

while(1):
	list = f.readline()
	if(list == ''):
                break
	list = float(list)
	ackArray.append(list)
	list = ff.readline()
	list = float(list)
	dataArray.append(list)


while(1):
	#receiver receiving frame
	if(newFrame and frameTransmit[0]==time):
		print("time %d: " %(time), end = '')
		if(ackArray[j]==0 and not oldFrame):
			print("receiver got frame %d, transmitting ACK%d, bad transmission" %(newFrame[0],newFrame[0]+1))
			frameTransmit.popleft()
			newFrame.popleft()
		elif(ackArray[j]==0 and oldFrame):
			#>=
			if(newFrame[0]-1>=oldFrame[0]):
				print("receiver got frame %d, transmitting ACK%d, bad transmission" %(newFrame[0],oldFrame[0]))
			else:
				print("receiver got frame %d, transmitting ACK%d, bad transmission" %(newFrame[0],newFrame[0]+1))
			frameTransmit.popleft()
			newFrame.popleft()
		elif(ackArray[j]==1 and not oldFrame):
			print("receiver got frame %d, transmitting ACK%d, good transmission" %(newFrame[0],newFrame[0]+1))
			frameTransmit.popleft()
			ackNum.append(newFrame[0]+1)
			newFrame.popleft()
			ackTransmit.append(time+3)
		elif(ackArray[j]==1 and oldFrame):
			if(newFrame[0]-1>=oldFrame[0]):
				print("receiver got frame %d, transmitting ACK%d, good transmission" %(newFrame[0],oldFrame[0]))
				ackNum.append(oldFrame[0])
			else:
				print("receiver got frame %d, transmitting ACK%d, good transmission" %(newFrame[0],newFrame[0]+1))
				ackNum.append(newFrame[0]+1)
			frameTransmit.popleft()
			newFrame.popleft()
			ackTransmit.append(time+3)
		j += 1
	#sender receiving ack
	if(ackTransmit and ackTransmit[0]==time):
		if(checker!=0):
			window = ackNum[0]
			ackNum.popleft()
		ackTransmit.popleft()
		checker = 1
		print("time %d: " %(time), end = '')
		print("sender got ACK%d, window [%d, %d]" %(window,window,window+6))
	#sender transmitting
	if(retimer and retimer[0]==time and case==0):
		oldFrame.append(oldFrame[x]+1)
		print("time %d: " %(time), end = '')
		if(dataArray[i]==0):
			print("sender window [%d, %d], retransmitting old frame %d, bad transmission" %(window,window+6,oldFrame[x]))
			retimer.append(time+8)
			tempt.append(oldFrame[x])
		elif(dataArray[i]==1):
			print("sender window [%d, %d], retransmitting old frame %d, good transmission" %(window,window+6,oldFrame[x]))
			frameTransmit.append(time+4)
			newFrame.append(oldFrame[x])
		retimer[0] += 1
		recounter += 1
		#oldFrame.popleft()
		x += 1
		if(recounter==7 and tempt):
			while(p<len(tempt)):
				oldFrame.append(tempt[p])
				p += 1
			retimer.popleft()
			x = 0
			tempt = deque()
		elif(recounter==7):
			retimer.popleft()
			case = 1
			x = 0
		i += 1
		p = 0
	elif(frameNum>=window and frameNum<=window+6):
		case = 0
		print("time %d: " %(time), end = '')
		if(dataArray[i]==0):
			print("sender window [%d, %d], transmitting new frame %d, bad transmission" %(window,window+6,frameNum))
			oldFrame.append(frameNum)
			retimer.append(time+8)
		elif(dataArray[i]==1):
			newFrame.append(frameNum)
			frameTransmit.append(time+4)
			print("sender window [%d, %d], transmitting new frame %d, good transmission" %(window,window+6,frameNum))
		i += 1
		frameNum += 1
	time += 1
	#print(oldFrame)
	if(i==98):
		break
	


f.close()
ff.close()
