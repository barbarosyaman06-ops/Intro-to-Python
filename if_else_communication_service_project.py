#conditional expressions

minutes=int(input("Enter the call duration in minutes: "))

fixed_fee=50
overage_penalty=0.25

if minutes>100:
    total_cost=fixed_fee+(minutes-100)*overage_penalty
else:
    total_cost=fixed_fee

print(f"The total cost of your call is: ${total_cost:.2f}")