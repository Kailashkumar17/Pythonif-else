purchase_amount=float(input("\nEnter the purchased amount :"))

qualifies_discount=1000

if(purchase_amount>=qualifies_discount):

    discount_amount=purchase_amount*0.1
    Final_amount=purchase_amount-discount_amount
    print("\nCongrats you have gor 10% discount")
    print("Your purchase amount is ", purchase_amount)
    print("Your discount amount is ", discount_amount)
    print("Your final amount is ", Final_amount)
else:
    print("\nSorry you are not eligible for discount")
    print("Your final amount is ", purchase_amount)
    
