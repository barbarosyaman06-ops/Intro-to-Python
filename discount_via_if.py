#discount based on purchase

book_price=150
purchased_book=int(input("Enter the amount of books that will be purchased: "))

total=(book_price*purchased_book)

if (purchased_book>=200):
    discount1=total-(total*0.25)
    print(f"Your discount is %10 and the total price is {discount1}")
elif (purchased_book>=150):
    discount2=total-(total*0.20)
    print(f"Your discount is %20 and the total price is {discount2}")
elif (purchased_book>=100):
    discount3=total-(total*0.10)
    print(f"Your discount is %10 and the total price is {discount3}")
elif (purchased_book>=50):
    discount4=total-(total*0.05)
    print(f"Your discount is %5 and the total price is {discount4}")
else:
    print(f"Your total price is {total}")
    