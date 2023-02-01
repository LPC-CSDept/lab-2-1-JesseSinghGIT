def main():
   ##################################################
   # Comlete your code here
   ##################################################


    num1 = int( input( 'What is the regular price of the item? : '))
    num2 = int (input ('What is the percentage discount on the item? : '))
    num3 = num2/100
    num4 = num3* num1
    num5 = num1 - num4
    print ('Regular price: $' , num1 ) 
    print ('Discount amount: $' , num4 ) 
    print ( 'The final price: $' , num5 ) 
   
    pass


if __name__ == '__main__':
    main()
