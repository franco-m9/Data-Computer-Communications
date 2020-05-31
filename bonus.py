f = open("amazontrace.txt")
routes = []
current = []
previous = []
numbers = []
sum = 0
test = []
i = 0
j = 0
x = 0
p = 0

while(1):
	list = f.readline()
	if(list == ''):
		break
	routes.append(list.split())

f.close()

while(i<len(routes)):
	if('length' in routes[i]):
		if(i+1<len(routes) and '100' in routes[i+1]):
			current.append(routes[i+1])
	i += 1


while(j<len(current)):
	previous.append(current[j][0])	
	j += 1	

test = [e[8:] for e in previous]

while(p<len(test)):
	if(p+1<len(test)):
		sum += float(test[p+1])-float(test[p])
	p += 1



print("The average time interval between each transmission is:")
print(sum/len(test))	


#print(routes)
#print(current)		
#print(previous)
#print(numbers)

