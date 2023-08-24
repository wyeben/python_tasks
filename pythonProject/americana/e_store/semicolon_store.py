from americana.e_store.cart_item import CartItem
from americana.e_store.product import Product


def main():
    store_name = "SEMICOLON STORES"
    branch = "MAIN BRANCH"
    location = "312, HERBERT MACAULAY WAY, SABO YABA, LAGOS."
    tel = "09033854588"
    VAT_RATE = 0.075

    try:
        customer_name = input("What is the customer's name: ")
        cart_items = []

        while True:
            item_name = input("What did the user buy? ( no ) to end): ")
            if item_name.lower() == "no":
                break

            try:
                quantity = int(input("How many pieces?: "))
                price = float(input("How much per unit?: "))
                cart_items.append(CartItem(Product(item_name, price), quantity))
            except ValueError:
                print("Invalid input. Please enter the actual value.")

        cashier_name = input("What is your name?: ")
        discount_percentage = float(input("Enter discount percentage: "))

        subtotal = sum(item.product.price * item.quantity for item in cart_items)
        discount = (discount_percentage / 100.0) * subtotal
        vat = VAT_RATE * subtotal
        total = subtotal + vat - discount

        print()
        print(store_name)
        print(branch)
        print(location)
        print(tel)
        print(time.strftime("%Y-%m-%d %H:%M:%S"))
        print("Cashier: " + cashier_name)
        print("Customer name: " + customer_name)
        print("=============================================================")

        print("%-20s%-10s%-10s%-10s" % ("Item", "Qty", "Price", "Subtotal"))
        print("-------------------------------------------------------------")
        for item in cart_items:
            product = item.product
            quantity = item.quantity
            price = product.price
            item_subtotal = price * quantity

            print("%-20s%-10d₦%-9.2f₦%-9.2f" % (product.product_name, quantity, price, item_subtotal))
        print("-------------------------------------------------------------")

        print("%-40s₦%-9.2f" % ("Subtotal:", subtotal))
        print("%-40s₦%-9.2f" % ("Discount:", discount))
        print("%-40s₦%-9.2f" % ("VAT (7.5%):", vat))
        print("=============================================================")
        print("%-40s₦%-9.2f" % ("Total:", total))
        print("=============================================================")
        print("THIS IS NOT THE ORIGINAL RECEIPT KINDLY PAY")
        print("=============================================================")

        amount_received = float(input("How much did the customer give to you? "))
        balance = amount_received - total

        print(store_name)
        print(branch)
        print(location)
        print(tel)
        print(time.strftime("%Y-%m-%d %H:%M:%S"))
        print("Cashier: " + cashier_name)
        print("Customer name: " + customer_name)
        print("=============================================================")

        print("%-20s%-10s%-10s%-10s" % ("Item", "Qty", "Price", "Subtotal"))
        print("-------------------------------------------------------------")
        for item in cart_items:
            product = item.product
            quantity = item.quantity
            price = product.price
            item_subtotal = price * quantity

            print("%-20s%-10d₦%-9.2f₦%-9.2f" % (product.product_name, quantity, price, item_subtotal))
        print("-------------------------------------------------------------")

        print("%-40s₦%-9.2f" % ("Subtotal:", subtotal))
        print("%-40s₦%-9.2f" % ("Discount:", discount))
        print("%-40s₦%-9.2f" % ("VAT (7.5%):", vat))
        print("=============================================================")
        print("%-40s₦%-9.2f" % ("Bill Total:", total))
        print("Amount Paid: ₦%.2f" % amount_received)
        print("Balance: ₦%.2f" % balance)
        print("=============================================================")
        print("\nThank you for shopping at " + store_name + "!")
        print("=============================================================")
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    import time

    main()
