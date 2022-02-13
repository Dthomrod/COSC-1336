#Daniel Rodriguez
#Project 2
#Assignment due: February 6, 2022
#COSC 1336


###Project requirements###
#Enter the day of the week,
#Calculate the average high temp and average low temp over 3-day span in Fahrenheit,
#Sum up the total rain fall over 3-days in inches,
#Convert the average high temp and average low temp to Celsius,
#Convert the total rain fall to cm


#input and storage section
Day = input('Enter the day of the week: (Monday - Sunday)' )
High_1 = int(input('Enter the high temperature (in Fahreheit) for day 1: '))
Low_1 = int(input('Enter the low temperature (in Fahrenheit for day 1: '))
Rainfall_1 = float(input('Enter the amount of rainfall (in inches) for day 1: '))


Day = input('Enter the day of the week: (Monday - Sunday)' )
High_2 = int(input('Enter the high temperature (in Fahrenheit) for day 2: '))
Low_2 = int(input('Enter the low temperature (in Fahrenheit for day 2: '))
Rainfall_2 = float(input('Enter the amount of rainfall (in inches) for day 2: '))

Day = input('Enter the day of the week: (Monday - Sunday)' )
High_3 = int(input('Enter the high temperature (in Fahrenheit) for day 3: '))
Low_3 = int(input('Enter the low temperature (in Fahrenheit for day 3: '))
Rainfall_3 = float(input('Enter the amount of rainfall (in inches) for day 3: '))


#output
print('The 3-day average high temperature is: ', int((High_1+High_2+High_3)/3),u"\u00b0"'F',)

print('The 3-day average low temperature is: ', int((Low_1+Low_2+Low_3)/3),u"\u00b0"'F')

print('The total rainfall (in inches) is: ', format((Rainfall_1+Rainfall_2+Rainfall_3),'.2f'),'inches')

print('The 3-day average high temperature (in Celsius) is: ', int(((((High_1+High_2+High_3)/3)-32)*5)/9),u"\u00b0"'C')

print('The 3-day average low temperature (in Celsius) is: ', int(((((Low_1+Low_2+Low_3)/3)-32)*5)/9),u"\u00b0"'C')

print('The total rainfall (in cm) is: ', format(((Rainfall_1+Rainfall_2+Rainfall_3)*2.54),'.2f'),'cm')
