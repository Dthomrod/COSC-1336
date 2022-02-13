
#User input (variables)
delivery_service = int(input('Hello, please choose your delivery service-- \n1 for FedEx, \n2 for UPS, \n3 for USPS: '))
weight = float(input('Indicate the weight of your package in ounces-- \n(rounded to the nearest ounce) \nwith a max shipping weight of 64oz: '))
region = int(input('Indicate the region you are shipping to-- \n1 for Central Zone, \n2 for Western Zone, \n3 for Eastern Zone,\n4 for International Zone: '))              
delivery_type = int(input('Choose your delivery type-- \n1 for overnight delivery, \n2 for standard delivery, \n3 for lowest priority delivery: '))
delivery_fee = delivery_service


#Delivery Service input
if delivery_service in [1, 2, 3]:
    delivery_fee = delivery_service
else:
    print("Delivery Service is Not Supported.")
    exit()


#Weight Cost
if weight <= 8:
    weight_cost = 2.5
elif 8 < weight <= 16:
    weight_cost = 4.5
elif 16 < weight <= 32:
    weight_cost = 7.5
elif weight > 32:
    weight_cost = 12
else:
    print("Weight is Not Supported.")
    exit()


#Region (using array)
if region in [1, 2, 3, 4]:
    region_multiplyer = region
else:
    print("Delivery Region is Not Supported.")
    exit()


#Delivery Type
if delivery_type == 1:
    additional_fee = 7
elif delivery_type == 2:
    additional_fee = 4
elif delivery_type == 3:
    additional_fee = 1
else:
    print("Delivery Type is Not Supported.")


#Final Calculations
print(f"Your Total Shipping Cost Comes out to ${delivery_fee + weight_cost + (delivery_fee * region_multiplyer) + additional_fee:.2f}")

exit()
