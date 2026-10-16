traveller_name = input("Enter traveller name: ")
destination = input("Enter destination: ")
number_of_tickets = int(input("Enter number of tickets: "))
ticket_price = float(input("Enter price per ticket: "))
total_cost = number_of_tickets * ticket_price
print("\n--- Travel Ticket Details ---")
print("Traveller:", traveller_name)
print("Destination:", destination)
print("Number of tickets:", number_of_tickets)
print("Price per ticket: Rs.", ticket_price)
print("Total ticket cost: Rs.", total_cost)
if total_cost > 5000:
    print("This is an expensive booking.")
elif total_cost < 5000:
    print("This booking costs less than Rs. 5000.")
else:
    print("The booking costs exactly Rs. 5000.")
print("Traveller name in uppercase:", traveller_name.upper())
print("Destination in uppercase:", destination.upper())
price1 = float(input("\nEnter the first ticket price: "))
price2 = float(input("Enter the second ticket price: "))
print("Before swapping:")
print("First price:", price1)
print("Second price:", price2)
temp = price1
price1 = price2
price2 = temp
print("After swapping:")
print("First price:", price1)
print("Second price:", price2)
