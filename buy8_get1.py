def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
    # total_price = 0
    # until_free = 8

    # while numberOfCoffees:
    #     numberOfCoffees -= 1
    #     if until_free == 0:
    #         until_free = 8
    #     else:
    #         total_price += pricePerCoffee
    #         until_free -= 1

    # return total_price

    free_coffees = numberOfCoffees // 9
    paid_coffees = numberOfCoffees - free_coffees
    return paid_coffees * pricePerCoffee


assert getCostOfCoffee(7, 2.50) == 17.50
assert getCostOfCoffee(8, 2.50) == 20
assert getCostOfCoffee(9, 2.50) == 20
assert getCostOfCoffee(10, 2.50) == 22.50
for i in range(1, 4):
    assert getCostOfCoffee(0, i) == 0
    assert getCostOfCoffee(8, i) == 8 * i
    assert getCostOfCoffee(9, i) == 8 * i
    assert getCostOfCoffee(18, i) == 16 * i
    assert getCostOfCoffee(19, i) == 17 * i
    assert getCostOfCoffee(30, i) == 27 * i
