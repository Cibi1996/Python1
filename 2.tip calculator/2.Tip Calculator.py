#Tip Calculator
print("Welcome to the Tip Calculator!")
Total_Bill = float(input("What was the total bill? "))
Tip_as_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
No_of_people = int(input("How many people to split the bill? "))

# print(type(Total_Bill))
# print(type(Tip_as_percent))
# print(type(No_of_people))

Amount_in_percentage=(Total_Bill*(Tip_as_percent/100))
Bill_added_with_percentage=(Total_Bill+Amount_in_percentage)



Bill_per_person=round(Bill_added_with_percentage/No_of_people, 2)

print(f"Each person should Pay{Bill_per_person}")