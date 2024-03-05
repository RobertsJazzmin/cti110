# Jazzmin Roberts
# 03/04/2024
# P1HW2
# create a program that does math

Budget= int(input('Enter Budget:\n'))
Destination= input('Enter yout travel destination:')
Gas= int(input('How much do you think you will spend on gas?\n'))
Hotel= int(input('Approximately, how much do you think you will need for accomodation/hotel?\n'))
Food= int(input('Last, how much do you need for food?\n'))
sum= Budget-Gas-Hotel-Food


print ('-----Travel Expenses-----')
print ('Location:', Destination)
print ('Initial Budget:', Budget)

print ('Fuel:', Gas)
print ('Accomodation:', Hotel)
print ('Food:', Food)

print ('Remaining Balance:', sum)
