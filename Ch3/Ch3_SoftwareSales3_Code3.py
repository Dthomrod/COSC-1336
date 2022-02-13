RETAIL = 99
fullPrice = 0.0
discount = 0.0
discountAmount = 0.0
totalAmount = 0.0

quantity = int(input('Enter the number of packages purchased: '))

if quantity > 99:
    discount = 0.40
elif quantity > 49:
    discount = 0.30
elif quantity > 19:
    discount = 0.20
elif quantity > 9:
    discount = 0.10
else:
    discount = 0

fullPrice = quantity * RETAIL
discountAmount = fullPrice * discount
totalAmount = fullPrice - discountAmount

print ('Discount Amount: $', format(discountAmount, '.2f'))
print ('Total Amount: $', format(totalAmount, '.2f'))
