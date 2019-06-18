s1=[]
c=0
b=int(input())
a=input().split()
for i in a:
  s1.append(int(i))
#print(s1)
for i in range(b-1):
  c=c+s1[i]+s1[i+1]
print(c)
