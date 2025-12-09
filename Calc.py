class Opp:
    def add(a, b):
        return a+b
    
    def sub(a, b):
        return a-b
    
    def mul(a, b):
        return a*b
    
    def div(a, b):
        return a/b

while True:
    print("Choose Operation")
    print("1. ADD \t 2. SUB \t 3. MUL \t 4. DIV \t 5. EXIT ")
    ch = int(input("Enter your choice as 1/2/3/4/5 : "))
    if (ch < 1 or ch > 5):
        print("Enter a Valid Choice!! \n")
        continue
    elif (ch == 5):
        break
    else:
        print()
        num1 = int(input("Enter Your First Number: "))
        num2 = int(input("Enter Your Second Number: "))
        if (ch == 1):
            print(f"Sum of {num1} and {num2} is: ", Opp.add(num1, num2))
            print(" ")
        elif (ch == 2):
            print(f"Difference between {num1} and {num2} is:", Opp.sub(num1, num2))
            print(" ")
        elif (ch ==3):
            print(f"Product of {num1} and {num2} is: ", Opp.mul(num1, num2))
            print(" ")
        elif (ch == 4):
            if num2 == 0:
                try: 
                    num1/num2
                except:
                    print("Math Error: Cannot Divide by zero! \n")
            else: 
                print(f"Quotient of {num1} and {num2} is: ", Opp.div(num1, num2))
                print(" ")
        else:
            print("Invalid Choice!!")
