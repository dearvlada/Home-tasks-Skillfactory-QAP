S = 0
number_of_tickets = int(input("Enter number of tickets\n"))

for price in range(1, number_of_tickets + 1):
    age_of_participant = int(input("Enter the age of the participant\n"))
    if 0 <= age_of_participant < 18:
        price = 0
        S += price
        print("The price for this participant is:", price)
    elif 18 <= age_of_participant <= 25:
        price = 990
        S += price
        print("The price for this participant is:", price)
    elif 25 < age_of_participant:
        price = 1390
        S += price
        print("The price for this participant is:", price)
if number_of_tickets > 3:
    S = S - S * 0.1
    print("WOW! You have a discount in 10%! Total price will be:", S)
else:
    print("The total price is: ", S)

