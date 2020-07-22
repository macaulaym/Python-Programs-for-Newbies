names=[]

name=input("Please enter a name: \n")

while name!="END":

  names.append(name)

  name=input("Please enter a name: \n")

  print("You have entered", len(names), "names\n", names)

