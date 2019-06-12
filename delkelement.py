a,b=input().split()
a1=int(a)
b1=int(b)
s1=[]
num=input().split()
for i in num:
  s1.append(i)
c=len(s1)
for i in s1[:c-b1]:
  print(i,end=" ")
