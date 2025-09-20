# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 

def calculate_hot_dog_cost(hot_dog_type, toppings):
    # Base Prices for hot dogs
    HotDogPrices = {
        "Hot Dog": 3.50,
        "Chili Dog": 4.50
    }

    # Prices for toppings
    ToppingPrices = {
        "Cheese": 0.50,
        "Peppers": 0.75,
        "Grilled Onions": 1.00
    }

    # tax rate
    tax_rate = 0.07

    # Hot dog type validation
    if hot_dog_type not in HotDogPrices:
        raise ValueError("Invalid hot dog type")

    base_cost = HotDogPrices[hot_dog_type]

    # Add topping costs
    for topping in toppings:
        if topping in ToppingPrices:
            base_cost += ToppingPrices[topping]
        else:
            raise ValueError(f"Invalid topping: {topping}")

    # Calculate total cost
    tax = base_cost * tax_rate
    total_cost = base_cost + tax

    return base_cost, tax, total_cost
