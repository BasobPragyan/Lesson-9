units=int(input("Enter the units consumed : "))
if(units<50):
    amount=50*2.60
    surchage=25
elif(units<=100):
    amount=130+((units-50)*3.25)
    surchage=35
elif(units<=200):
    amount=130+162.5+((units-100)*5.26)
    surchage=45
else:
    amount=130+162.5+526+((units-200)*8.45)
    surchage=75
total_bill=amount+surchage
print("Electricity bill is : ",total_bill)