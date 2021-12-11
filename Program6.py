class Store(name,location):
    self.name = name
    self.location = location
    def __print__():
        return self.name + self.location

class Cart():
    self.productName
    self.productQuantity
    self.cartDict
    self.Receipt

    def Add_item(item,quantity):
        productChoice = "Enter name of your product"
        productQuantity = "Enter quantity"
        myCart.Add_item(productChoice,productQuantity)
        self.cartDict[productChoice] += productQuantity

    def Remove_item():
        productToRemove = input("Enter name of your product")
        quantityToRemove = input("Enter Quantity")
        self.cartDict[productToRemove] -= quantityToRemove

    def __print__():
        return "User placed order from : " + myStore.name + "at address:" + myStore.address + "\n Order in cart is:" + cartDict.keys + "with quantity:" + cartDict.values + "\n Total receipt is $"

Products = {Milk:2.50, Bread:1.98, Egg:0.70, Flour:1.18, Oil:4.00, Cheese:2.68}

    
myCart = Cart()
storeName = input("Good morning! Which store you want to use today?")
storeLocation = input("Which location you want to use?")
print("Products as follow:" + Products.keys + Products.values)

removeBool = input("Do you want to remove an item (Yes/No)")
if removeBool.upper() == "YES":
    myCart.Remove_item
print(myCart)
AddAnother = input("Do you want to add another product (yes/no")
if AddAnother.upper() == "YES":
    myCart.Add_item
print(myCart)
