snack_name = "Crips"
price = 1.67
quantity = 4
is_available = True
print(snack_name, type(snack_name))
print(price, type(price))
print(quantity, type(quantity))
print(is_available, type(is_available))
total_stock_value = price * quantity
sale_price = price * 0.89
double_stock = quantity * 2
print("Total stock value:", total_stock_value)
print("Sale price:", sale_price)
print("Double the stock:", double_stock)
print("Is price under $2?", price < 2)
print("Is quantity greater than 5?", quantity > 5)
print("Is price exactly $1.50?", price == 1.50)
shop_name = "Bakery" + " " + "Delights"
print("Shop name:", shop_name)
print("Number of letters:", len(snack_name))
print("First letter:", snack_name[0])
price_a = 2.57
price_b = 3.70
print("Before swap:", price_a, price_b)
temp = price_a
price_a = price_b
price_b = temp
print("After swap:", price_a, price_b)