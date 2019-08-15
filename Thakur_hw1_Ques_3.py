#Rupin Singh Thakur 1001651167

original_Price=99

quantity=int(input("Enter the number of items purchased"))
if(quantity<=10):
    print("You need to purchase mor to get a discount")
elif(quantity>=10 and quantity<=19):
    discount= original_Price* 0.10
    print("The discount price is: $%.2f"  %discount)
    total_Amount= original_Price-discount
    print("The total price after discount is: $%.2f" %total_Amount)
elif(quantity>=20 and quantity<=49):
    discount= original_Price* 0.20
    print("The discount price is: $%.2f"  %discount)
    total_Amount= original_Price-discount
    print("The total price after discount is: $%.2f" % total_Amount)
elif(quantity>=50 and quantity<=99):
    discount= original_Price* 0.30
    print("The discount price is: $%.2f"  %discount)
    total_Amount= original_Price-discount
    print("The total price after discount is: $%.2f" %total_Amount)
else:
    discount = original_Price * 0.40
    print("The discount price is: $%.2f" % discount)
    total_Amount = original_Price - discount
    print("The total price after discount is: $%.2f" % total_Amount)









