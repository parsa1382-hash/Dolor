l=[]
for i in range(0,4):
  l.append(int(input()))

x1=l[0]
x2=l[2]
v1=l[1]
v2=l[3]

if v1==v2:
  print("WAIT WAIT")
elif ((x1<x2) & (v1>v2)) or ((x2<x1) & (v1<v2)):
  print("SEE YOU")
else:
  print("BORO BORO")
