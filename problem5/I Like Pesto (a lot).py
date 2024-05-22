other=[]
pesto: int = 0
inputlist=[]
for v in range(8):
    i=input()
    inputlist.append(i)
for y in inputlist:    
    if y=="pesto":
        pesto+=1
    else :
        other.append(y)
print(pesto)
print(other)
