class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item, price, quantity=1):
        if item in self.cart:
            self.cart[item]['quantity'] += quantity
        else:
            self.cart[item] = {'price': price, 'quantity': quantity}
        print(f"Added {quantity} {item}(s) to the cart.")

    def remove_item(self, item, quantity=1):
        if item in self.cart:
            if self.cart[item]['quantity'] > quantity:
                self.cart[item]['quantity'] -= quantity
                print(f"Removed {quantity} {item}(s) from the cart.")
            elif self.cart[item]['quantity'] == quantity:
                del self.cart[item]
                print(f"Removed all {item}(s) from the cart.")
            else:
                print(f"Error: Not enough {item} to remove.")
        else:
            print(f"Error: {item} is not in the cart.")

    def calculate_total(self):
        total = sum(item['price'] * item['quantity'] for item in self.cart.values())
        return f"Total price: ${total:.2f}"

if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Apple", 1.5, 3)
    cart.add_item("Banana", 0.75, 5)
    print(cart.calculate_total())
    cart.remove_item("Apple", 1)
    print(cart.calculate_total())
    cart.remove_item("Banana", 5)
    print(cart.calculate_total())