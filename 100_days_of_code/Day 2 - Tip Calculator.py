#If the bill was $150.00, split between 5 people, with 12% tip. 
bill = float(input("What was the total bill? "))
people = int(input("How many people are paying? "))
tip = float(input("What tip percentage? "))
tip /= 100

bill += bill * tip
#Each person should pay (150.00 / 5) * 1.12 = 33.6
bill /= people
bill = round(bill,2)

#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇
print("The final total for the bill is {:0.2f} per person".format(bill))
