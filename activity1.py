print("Exam eligibity attandence")
attandence=int(input("Enter your attandence in % : "))
if(attandence<75):
    med_cause=input("Please provide the causes : Y or N : ")
    if(med_cause=="Y"):
        print("You are allowed")
    else:
        print("You are not allowed")