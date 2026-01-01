with open("c:/Users/Farhan/Desktop/marks.txt") as file: 
     line = file.read().split()

     a = []
     b = []
     c = []

for i in range(0,len(line),2):
        mark = float(line[i])
        grade = line[i+1]

        if grade == "A":
           a.append(mark)
        elif grade == "B":
            b.append(mark)
        else:
          c.append(mark)
       
   average_a = round(sum(a)/len(a),2)
   average_b = round(sum(b)/len(b),2)
   average_c = round(sum(c)/len(c),2)

   print("Average mark for A: ", average_a)
   print("Average mark for B: ", average_b)
   print("Average mark for C: ", average_c)
