from collections import deque

i = 0
w = 0
c = 0
g = 0
q = 0
b = 0
z = 0
k = 0
l = 0
p = 0
s = 0
a = 0
m = 0
skipfirst = 0
sf = 0
mscount = 0
routes = []
storage = []
neighbors = []
tcount = 0
hops = 0
hopd = 0
delay = 0
totald = 0
pathd = [0] * 30
pathhop = 0
sf = 0
mscount = 0
msindex = -1
msval = deque()
f = open("log19","r")
ff = open("log19","r")

#storing file
while(1):
    list = f.readline()
    if(list == ''):
        break
    routes.append(list)

#avg hops
while(i<len(routes)):
    if(routes[i][0]=='t'):
        tcount += 1
    else:
        hops += 1
    i += 1

#path delay
while(1):
    list = ff.readline()
    if(list == ''):
        break
    storage.append(list.split())

while(q<len(storage)):
    while(b<len(storage[q])):
        if(storage[q][b]=='ms'):
            msindex = q
        elif(storage[q][b]=='traceroute' and sf==1):
            while(k<len(storage[msindex])):
                if(storage[msindex][k]=='ms'):
                    delay = float(storage[msindex][k-1])
                    msval.appendleft(delay)
                k += 1
            delay = 0
            while(z<len(msval)):
                delay += msval[z]
                z += 1
            totald += (delay/len(msval))
            msval.clear()
            delay = 0
            mscount = 0
            z = 0
            k = 0
            break
        b += 1
    if(q+1==len(storage)):
        while(k<len(storage[msindex])):
            if(storage[msindex][k]=='ms'):
                delay = float(storage[msindex][k-1])
                msval.appendleft(delay)
            k += 1
        delay = 0
        while(z<len(msval)):
                delay += msval[z]
                z += 1
        totald += (delay/len(msval))
        z = 0
        delay = 0
    sf = 1
    b = 0
    q += 1

#path distribution
while(c<len(routes)):
    if(skipfirst==1 and routes[c][0]=='t'):
        pathd[hopd-1] += 1
        hopd = 0
    elif(skipfirst==0):
        pass
    else:
        hopd += 1
        if(c+1==len(routes)):
            pathd[hopd-1] += 1
            hopd = 0
    skipfirst = 1
    c += 1


print("Avg path length: %f hops" %(hops/tcount))
print("Avg path delay: %f ms" %(totald/tcount))
print("Path length distribution:")
while(g<len(pathd)):
    print(" 	%d " %(g+1), end = '')
    print(pathd[g])       
    g += 1

#neighbors
router = input("Enter a router to find its neighbors: ")
while(l<len(storage)):
	while(p<len(storage[l])):
		if(storage[l][p]==router):
			while(s<len(storage[l-1])):			
				if('(' in storage[l-1][s]):
					neighbors.append(storage[l-1][s-1])
					break
				s += 1
			while(m<len(storage[l+1])):
				if('(' in storage[l+1][m]):
					neighbors.append(storage[l+1][m-1])
					break
				m += 1
			m = 0
			s = 0
		p += 1
	p = 0
	l += 1


neighbors = set(neighbors)
print("-- Neighbors of %s --" %(router))
for e in neighbors:
	print("  %d: " %(a+1), end = '')
	print(e)
	a += 1	
		
f.close()
