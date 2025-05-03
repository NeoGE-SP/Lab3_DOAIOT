import price_info

prices = price_info.price_list
quantities = price_info.quantity_list

def test_total_cost():

    result = 0
    for key in prices.keys():
        if key in quantities:
            # complete the implementation below:
            result += (prices[key] * quantities[key])


    assert (result == 46.75)

def test_fruit_cost():
    fruit = "apple"
    quantity = 10

    cost = 12.0

    for key in prices.keys():
        if key == fruit:
            result = quantity*prices[key]
            break

    #result = price_info.cost_of_fruits(fruit, quantity)

    assert (result == cost)