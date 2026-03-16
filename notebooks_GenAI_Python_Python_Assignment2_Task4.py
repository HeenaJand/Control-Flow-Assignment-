##Task 4 Loop Control with Conditions (break & continue)

daily=[200,150,0,400,50,-1,300]

daily 

total_sales=0

for sale in daily:
    if sale==-1:
        print("Corrupted Data")
        break
    if sale==0:
        print("A day with no sale. Skip")
        continue 
    
    total_sales+=sale
    print( sale," Added to the sale. Running Total is:", total_sales)
print(" Final Total:", total_sales)



