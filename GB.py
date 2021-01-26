def findMaxNumnumPeople(list):
  numPeople = 0 
  maxPeriod = 0
  maxNumPeople = 0

  for i in range(len(list)):
    if list[i][2] == 1:
      numPeople += list[i][1]
    else:
      numPeople -= list[i][1]
    if (i < len(list)-1 and list[i][0] == list[i+1][0]):
      continue
    if numPeople > maxNumPeople:
      maxNumPeople = numPeople
      maxPeriod = list[i][0]
  return maxPeriod 


list = [ [1526579928, 14, 1], 
         [1526579928, 4,  0],
         [1526579928, 2,  0],
         [1526580378, 10, 1],
         [1526580380, 18, 0],
         [1526580380, 18, 1],
         [1526580381, 1,  0],
         [1526580382, 7,  1],
         [1526580382, 7,  0] ]

run = findMaxNumnumPeople(list)
run=str(run)
print("The busiest period time in the building is: " +run)