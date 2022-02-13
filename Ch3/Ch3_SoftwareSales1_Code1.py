quantity = int(input('How many packages are you purchasing?'))
RETAIL = 99
if quantity < 10:
    discount = 0
    print('The total price of the purchase is:', RETAIL*quantity)
else:
    if quantity >= 10 and quantity <= 19:
        discount = .1
        print('The discount is 10%')
    else:
        if quantity >=20 and quantity <= 49:
            discount = .2
            print('The discount is 20%')
        else:
            if quantity >=50 and quantity <= 99:
                discount = .3
                print('The discount is 30%')
            else:
                if quantity >= 100:
                    discount = .4
                    print('The discount is 40%')

if discount > 0:                   
    sales = RETAIL*quantity*(1-discount)
    print('The total price of the purchase after discounting is:', sales)
                    
