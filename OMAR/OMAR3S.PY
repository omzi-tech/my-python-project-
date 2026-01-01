print ("Select a brand : ")
print ("1. Honda")
print ("2. Toyota")
ch1 = int(input("Enter your choice (1 or 2) >> "))
if ch1 == 1:
 print ("Select a model : ")
 print ("1. Honda City")
 print ("2. Honda Civic")
 ch2 = int(input("Enter your choice (1 or 2) >> "))
 if (ch2 == 1):
  print ("$90,000")
 elif (ch2 == 2):
  print ("$120,000")
 else:
  print ("Not a valid model!")
elif ch1 == 2:
 print ("Select a model : ")
 print ("1. Toyota Vios")
 print ("2. Toyota Camry")
 ch2 = int(input("Enter your choice (1 or 2) >> "))
 if (ch2 == 1):
  print ("$85,000")
 elif (ch2 == 2):
  print ("$140,000")
 else:
  print ("Not a valid model!")
else:
 print ("Not a valid brand!")