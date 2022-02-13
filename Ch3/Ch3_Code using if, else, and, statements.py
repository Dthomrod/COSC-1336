#Chapter 3, Week 4 Lecture 1, Sample Code-----Selection Statements
#my notes:  pay attention to the DETAILS!  I put 1 extra space or indentation and it
#took me 30 min to fix the indentation for all code


#User information

print('Enter three different integers and this program \nwill print them out high to low')


#input

num1 = int(input('Enter the first number'))
num2 = int(input('Enter the second number'))
num3 = int(input('Enter the third number'))


#Selection Structure

if num1 > num2 and num2 > num3:
    print( num1,'>', num2,'>', num3)

else:
    if num1 > num3 and num3 > num2:
        print( num1,'>', num3,'>', num2)

    else:
        if num2 > num1 and num1 >num3:
            print( num2,'>', num1,'>', num3)
            
        else:
            if num2 > num3 and num3 > num1:
                print( num2,'>', num3,'>', num1)

            else:
                if num3 > num1 and num1 > num2:
                    print( num3,'>', num1,'>', num2)

                else:
                    if num3 > num2 and num2 > num1:
                        print( num3,'>', num2,'>', num1)

                    else:
                        print('You did not follow instructions!')







              







              





              
