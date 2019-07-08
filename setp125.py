n1=int(input()) 
b=input().split()
s1=[]
for i in b:
  s1.append(int(i))
s1.sort()
for i in range(1,s1[0]+1):
  temp=0
  for j in range(n1):
    if (s1[j]%i)!=0:
      temp=1
  if temp==0:
    c=i
print(c)
