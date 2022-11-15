n=int(input())
l=0
m=0
h=0
if n<0:
  print("Invalid Input")
elif n==0:
  print("No Earthquake predicted")
else:
  for i in range(n):
    k=float(input())
    if k<=5.4:
      l += 1
    elif k>5.4 and k<=7.0:
      m += 1
    else:
      h += 1
  print(l)
  print(m)
  print(h)
