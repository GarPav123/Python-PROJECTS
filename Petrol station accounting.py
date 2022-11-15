n=int(input("Enter the number of substations:"))
i=1
sl=0
sml=0
while i<=n:
  li=int(input("Enter the number of literes of petrol from station",i))
  mli=int(input("Enter the number of milliliteres of petrol from station",i))
  sml=sml+mli
  sl=sl+li
  i=i+1
s=sml%1000
if sml>1000:
  S=sl+1
else:
  S=sl
print(S)
print(s)
