##Task2 Process Multiple orders(for loop)

orders = [1200,2500,800,1750,3000]
total_revenue = 0
discount = 0

print("----------------SUMMARY TABLE---------------")
print(f"{'Order Amount':<15} | {'Discount %': <12}| {'Final Amount ': <15}")
print("-"*45)

for amount in orders:
    if amount > 2000:
        discount_rate=15
    elif amount >= 1500:
        discount_rate=10
    elif amount >= 1000:
        discount_rate=7
    else:
        discount_rate= 0
        
    discount_value=amount*(discount_rate/100)
    final_amount=amount-discount_value
    total_revenue+=final_amount
    if discount_rate>0:
            discount+=1
    print(f"{ amount:<15} | {discount_rate: <12}|{final_amount:<15}")
print("-"*45)
print(f"Total Revenue after discount:{total_revenue: .2f}")
print(f"Number of orders received a discount:{discount}")



