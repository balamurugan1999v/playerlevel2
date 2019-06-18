b=int(input())
s1=[]
a=input().split()
c=0
for i in a:
  c=c+int(i)
  s1.append(c)
s2=s1[::-1]
d=len(s2)
for i in range(d):
  print(s2[i],end=" ")
