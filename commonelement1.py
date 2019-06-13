#
a=int(input())
arr1=input().split()
arr2=input().split()
s1=[]
s2=[]
s3=[]
r=0
r1=0
co=0
for i in arr1:
  if r<a:
    s1.append(int(i))
    r=r+1
for i in arr2:
  if r1<a:
    s2.append(int(i))
    r1+=1
for i in range(a):
  for j in range(a):
    if s1[i]==s2[j] and s1[i] not in s3:
      s3.append(s1[i])
      co+=1
      break
for i in range(co):
  print(s3[i],end=" ")
