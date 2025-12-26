s=[1,0,10,2,4,0,7,8]
res=[]
for num in s:
    if num!=0:
        res.append(num)
print(res+[0]*(len(s)-len(res)))
