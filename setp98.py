a,b=input().split()
b1=int(b)
s1=[]
for i in a:
  s1.append(int(i))
for i in range(b1):
  if i in s1:
    f=0
  else:
    f=1
    break
if f==1:
  print('no')
else:
  print("yes")
