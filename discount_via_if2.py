#discount rate can be indivudally written, you dont have to create a new variable
#under every if,else statement

book_price=165
quantity=int(input("Please enter an amount of books to purchase: "))

if (quantity>=200):
    discount_rate=0.25
elif (quantity>=150):
    discount_rate=0.20
elif (quantity>=100):
    discount_rate=0.15
elif (quantity>=50):
    discount_rate=0.10
else:
    discount_rate=0.00

total_price=(book_price*quantity)
discounted_price=total_price-(total_price*discount_rate)

print(f"The book price is: {book_price}")
print(f"The amount of books ordered: {quantity}")
print(f"Total discount based on quantity: {discount_rate}")
print(f"Total price before discount: {total_price}")
print(f"Total price after discount: {discounted_price}")

