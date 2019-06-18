a1,b1=input().split()
a=int(a1)
b=int(b1)
s1=[]
s2=[]
s3=[]
num=input().split()
c=0
r=0
for i in num:
  if r<a:
    s1.append(int(i))
  else:
    s2.append(int(i))
  r+=1
for i in range(a):
  for j in range(b):
    if s1[i]==s2[j]:
      if s1[i] not in s3:
        s3.append(s1[i])
s3.sort()
for i in s3:
  print(i,end=" ")
