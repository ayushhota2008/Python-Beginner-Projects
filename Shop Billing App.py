from datetime import datetime


prices = {"cement":200,"rod":100,"paint":150,"tiles":300 }


cart = []
total = 0
def load():
    try:
        with open("bills.txt","r") as f:
            prev_bill = f.read().strip()
            print(prev_bill)
    except FileNotFoundError:
        print("No previous bill exists!")




def save_bill(cart, total, discount, fi_total):
    with open("bills.txt","a") as f:
        f.write("----Bill----\n")
        f.write(f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M')}\n")
        for i in cart:
            f.write(f"{i['Item'].title()} x{i['Quantity']}= {i['Cost']}\n")
        f.write(f"Subtotal:{total}\n")
        f.write(f"Discount: {discount:.2f}\n")
        f.write(f"Your total amount is {fi_total:.2f}")
        f.write("\n")
        f.write("\n")

print("----Simple Shop Billing App----")
print("Our items:")
for item,price in prices.items():
    print(f"{item}- {price}")

print("Choose item and quantity to add in cart")

prev = input("D you want see previous bill? y/n: ").strip().lower()
if prev == "y":
    load()
else:
    print("Continue adding new items.")
    pass
while True:
    product = input("Enter item name:").strip().lower()

    if product not in prices:
        print("Item not present.")
        continue

    try:
        quantity = int(input("Enter quantity:"))
    except ValueError:
        print("Enetr a whole number!")
        continue
    if quantity <= 0:
        print("Quantity must be atleast 1.")
        continue

    cost = prices[product]*quantity
    
    cart.append({"Item":product, "Quantity":quantity, "Cost":cost})
    total +=cost
    print(f"Added {product.title()} x{quantity}: {cost}")

    add_more = input("Want to add other items? (y/n): ").strip().lower()
    if add_more != "y":
        break

if not cart:
    print("Your cart is empty.")
else:
    print("-----BILL-----")
    for i in cart:
        print(f"{i['Item'].title()} x{i['Quantity']}= {i['Cost']}")
    print(f"Subtotal:{total}")

    discount = 0
    if total >= 10000:
            discount = total*0.05
            print(f"5% discount:{discount:.2f}")

    fi_total = total-discount
        
    print(f"Your total amount is {fi_total:.2f}")
    save_bill(cart, total, discount, fi_total)





    
