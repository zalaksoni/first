print ("""Enter 1 for Addition

         Enter 2 for Substraction

         Enter 3 for multiplication

         Enter 4 for division
  
         Enter 5 for modulodivision""")

choice=int(input("Enter ur choice"))

no=int(input("Enter first number"))

no2=int(input("Enter second number"))
if choice==1:
    answer=num1+num2
    print ("The answer is:" ,answer)

elif choice==2:
    answer=num1-num2
    print ("The answer is:",answer)

elif choice==3:
    answer=num1*num2
    print ("The answer is:",answer)

elif choice==4:
    answer=num1/num2
    print ("The answer is:",answer)

elif choice==5:
    answer=num1%num2
    print ("The answer is:",answer)

else:

     print "Enter proper choice..."


