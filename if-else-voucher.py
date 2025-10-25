no_of_items=int(input("\n Enter the no of items which are in cart :"))

#How many itens to buy for the promotion
promotion_items=5
voucher_amount=1500

if no_of_items>=promotion_items:

    print("\nCongrats, you are qualified for the promotion")
    print("As a special offer, you will receive a voucger value of rs,", voucher_amount)
else:

    print("\n Sorry, you need atleast 5 items to qualify for the promotion")
    print("\Consider adding more kitens to you shopping cart to avial the offer")
          
