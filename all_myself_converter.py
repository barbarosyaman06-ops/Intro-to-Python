def number_converter(number):
    # 1. Fix the logic trap: block if it is NOT a digit OR NOT 4 characters long
    if not number.isdigit() or len(number) != 4:
        return "Please try again"
        
    # 2. Add an empty string "" at index 0 to handle zero digits effortlessly
    ones = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
    tens = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]

    # 3. Pull digits directly using string indexing and turn them into integers for the lists
    thousands_place = int(number[0])
    hundreds_place = int(number[1])
    tens_place = int(number[2])
    ones_place = int(number[3])
    
    # 4. Build the holders safely (No return statements here!)
    
    # Thousands Logic
    if thousands_place == 1:
        thousand_holder = "bin"
    elif thousands_place > 1:
        thousand_holder = f"{ones[thousands_place]} bin"
    else:
        thousand_holder = ""
        
    # Hundreds Logic
    if hundreds_place == 1:
        hundreds_holder = "yüz"
    elif hundreds_place > 1:
        hundreds_holder = f"{ones[hundreds_place]} yüz"
    else:
        hundreds_holder = ""

    # Tens and Ones Logic (Our empty string "" at index 0 handles zeroes automatically!)
    tens_holder = tens[tens_place]
    ones_holder = ones[ones_place]

    # 5. Combine everything
    finalize = f"{thousand_holder} {hundreds_holder} {tens_holder} {ones_holder}"
    
    # We use .split() and " ".join() to clean up any weird double spaces if a holder was empty
    print(" ".join(finalize.split()))


entered_number = input("Please enter a 4-digit number: ")
number_converter(entered_number)


