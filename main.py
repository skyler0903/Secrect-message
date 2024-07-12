cd= (input("you want to code or decode?\n"))
if cd == "code":
 c=input("enter the message you want to give to adi:\n")
 if len(c) >=3:
  result= c[1:]+c[0]
  print(result)
 else:
   print(c[1]+c[0])
elif cd =="decode":
  d=input("enter the message you want to decode:\n")
  if len(d)<3:
   print(d[1]+d[0])
  else:
    print(d[-1]+d[0:-1])
