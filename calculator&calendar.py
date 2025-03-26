import calendar
from calendar import IllegalMonthError


choice=[1,2,3]

while True:

    print("Welcome\nWhat would you like to do?")
    print("1.Calculator\n2.Calender\n3.Quit\n")
    try:
        user_int=int(input("Enter your choice:"))
        if user_int==1:
            print("\n\nWelcome To Simple Arithmetic Calculator\n")
            num1=int(input("Enter the first number:"))
            num2=int(input("Enter the second number:"))
            op=input("Enter the operator(+,-,*,/):")
            if op =="+":
                print(num1,"+",num2,"=",(num1+num2))
            elif op=="-":
                print(num1,"-",num2,"=",(num1-num2))
            elif op=="*":
                print(num1,"*",num2,"=",(num1*num2))
            elif op=="/":
                if num2!=0:
                    print(num1,"/",num2,"=",(num1/num2))
                else:
                    print("Second number should not be zero.")
            else:
                print("Enter the valid Operator.")
        elif user_int==2:
            print("Welcome To Calender")
            year=int(input("Enter the year:"))
            month=int(input("Enter the month(1-12):"))
            try:
                cal=(calendar.month(year,month))
                print(cal)
            except IllegalMonthError:
                print("Enter a valid month(1-12)")

        elif user_int==3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again")
    except ValueError:
        print("Error: Enter a valid number.")
