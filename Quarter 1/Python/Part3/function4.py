#arbitrary arguments parameter should be at end it will be in tuple form if user gives multiple unknown inputs
def pizzaOrder(size,flavour,*toppings):
    print(f"Size is:{size} and flavour is:{flavour} and toppings are:{toppings}")

pizzaOrder(12,"chickenTikka","olive","fruits","xyz")