tot=int(input(" Number of classes held : "))
att=int(input(" Number of classes attended : "))
med=int(input(" Student medical proof availability [1(for Yes)/0 (for No)] : "))
import math
if med==0:
  if (att)>=((0.75*(tot))):
    print(int(((att)/(tot))*100))
    print("Allowed")
  else:
    print(int((((att)/(tot))*100)))
    print("Not allowed")
else:
  print(int(((att)/(tot))*100))
  print("Allowed")

