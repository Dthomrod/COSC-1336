# Initial Declaration of Variables.
delivery_fee, weight_cost, region_multiplyer, additional_fee = 0, 0, 0, 0

# Delivery Service Input.
delivery_service = int(input('Welcome!\nPlease Choose Your Delivery Service: \n1 - FedEx\n2 - UPS\n3 - USPS\n'))
# Setting Delivery Fee.
if delivery_service in [1, 2, 3]:
    delivery_fee = delivery_service
else:
    print("Delivery Service is Not Supported.")
    exit()

#  Weight Input.
weight = round(float(input('Please Input the Weight of Your Package (in Oz):\n')))
# Setting Weight Cost.
if weight <= 8:
    weight_cost = 2.5
elif 8 < weight <= 16:
    weight_cost = 4.5
elif 16 < weight <= 32:
    weight_cost = 7.5
else:
    weight_cost = 12

# Region Input
region = int(input('Please Indicate Your Shipping Zone:\n1 - Central \n2 - Western \n3 - Eastern\n4 - International\n'))
# Setting Region Multiplyer.
if region in [1, 2, 3, 4]:
    region_multiplyer = region
else:
    print("Delivery Region is Not Supported.")
    exit()

# Delivery Type Input
delivery_type = int(input('Please Choose your Delivery Type:\n1 - Overnight\n2 - Standard \n3 - Low Priority\n'))
# Setting Additional Fees.
if delivery_type == 1:
    additional_fee = 7
elif delivery_type == 2:
    additional_fee = 4
elif delivery_type == 3:
    additional_fee = 1
else:
    print("Delivery Type is Not Supported.")
    exit()

print(f"Total Shipping Cost is ${delivery_fee + weight_cost + (delivery_fee * region_multiplyer) + additional_fee:.2f}")
