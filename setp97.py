a1,b1=input().split()
a=int(a1)
b=int(b1)
f=0
for i in range(a,b):
  if(i%2!=0):
    f=f+i
print(f)
