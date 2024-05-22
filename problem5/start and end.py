a=[]
l=["abc","123","2332","aBBA","helloo","1212","DcEfD"]
for x in l:
    y=x.upper()
    if y[0]==y[-1]:
        a.append(x)
print(a)