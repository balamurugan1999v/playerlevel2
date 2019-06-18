b=int(input())
s1=[]
a=input().split()
c=0
for i in a:
  c=c+int(i)
  s1.append(int(i))
d=len(s1)
if d==1:
  print(s1[0])
else:
  for i in range(d):
    print((c+s1[i]),end=" ")
