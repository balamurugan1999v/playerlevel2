a1,k1=input().split()
a=int(a1)
k=int(k1)
arr1=input().split()
s1=[]
s2=[]
r=0
for i in arr1:
  if r<a:
    s1.append(int(i))
    r=r+1
#s1.sort()
for i in range(a):
  co=0
  for j in range(a):
    if s1[i]==s1[j]:
      co+=1
  if co==k and s1[i] not in s2:
    s2.append(s1[i])
for i in s2:
  print (i,end=" ")
