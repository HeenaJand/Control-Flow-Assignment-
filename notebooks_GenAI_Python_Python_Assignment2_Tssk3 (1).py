## Task 3 : User Menu(while loop+break/continue)

order=[]
while True:
    print("-----Menu Options-----")
    print("1 : Add order amount to a running list")
    print("2 : Show all orders and total after applying discount ")
    print("q : Quit")
    
    choice= input("Enter your choice:")

    if choice=="1":
       amount= float(input("Enter order amount"))
       order.append(amount)
       print("Amount added successfully")
    
    elif choice=="2":
        if len(order)==0:
         print("No order")
         continue 
        print("All orders are:", order)
   
        total = sum(order)
        
        if total >2000:
           total= total - total*0.15
        elif total>=1500:
            total= total -total* 0.10
        elif total>=1000:
             total=total-total*0.7
        else :
           total=total
        
        print("Total amount after applying discount:", total)

    elif choice=="q":
        print("Exiting the program ")
        break
    else:
        print("Invalid Input ! Please try again")
        continue 





