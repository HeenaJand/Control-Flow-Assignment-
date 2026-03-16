# Task 1 : Discount Rules (if/elif/else)

order_amount_input=input("Enter the order amount")

##Getting input from user and check conditions 

if order_amount_input.isdigit():
    order_amount= int(order_amount_input)
    print("You have entered a valid integer")
    if order_amount>=2000:
        discount_rate= 15/100   ##15% discount 
    elif 1500<=order_amount<2000:
        discount_rate= 10/100   ##10% discount 
    elif 1000<=order_amount<1500:
        discount_rate=7/100  ##7% discount 
    else:
        discount_rate= 0 ##0% discount 
        
    ## Calculations ##
    discount=order_amount*discount_rate
    subtotal=order_amount-discount

    ##calculating Tax##
    tax=subtotal*0.05
    final_amount=subtotal+ tax
        
    ##Results##
    print("---ORDER SUMMARY---")
    print(f"Original price of the product:{order_amount}")
    print(f"Discount applied on the product:{discount}" , f"that is {discount_rate*100}%")
    print(f"Subtotal amount of the product:{subtotal}")
    print(f"5% Tax applied : {tax}")
    print(f"Final amount to be paid : {final_amount}")
    
else:
    print("You have entered wrong input value") 




