a1,k1=input().split()
a=int(a1)
k=int(k1)
arr1=input().split()
s1=[]
r=0
for i in arr1:
  if r<a:
    s1.append(int(i))
    r=r+1
s1.sort()
for i in range(a):
  if s1[i]<k:
    print(s1[i],end=" ")
