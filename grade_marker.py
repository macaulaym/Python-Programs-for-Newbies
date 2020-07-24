mark=float(input("what was your percentage? half marks are allowed. "))

if(mark>100):
    print("really?")
elif(mark<100 and mark>=70):
     print("well done, you got an A")
elif(mark<70 and mark>=60):
     print("not bad, you got an B")
elif(mark<60 and mark>=50):
     print("borderline, you got an C")
elif(mark<50 and mark>=40):
     print("you need to improve, you got an D")
elif(mark<40 and mark>=30):
     print("bad, you got an E")
elif(mark<0):
     print("really?")
else:
     print("Unacceptable, fail. Retest required")
