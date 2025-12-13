class Calculate :
    def __init__(self):
        pass
    def addition(self,a,b) :
        return a + b
    def subtraction(self,a,b) :
        return a - b
    def multiplication(self,a,b) :
        return a * b
    def division(self,a,b) :
        return a / b
    

    def run(self) :
        try :
            a = float(input("Enter the first number : "))
            b = float(input("Enter the second number : "))
        except :
            print("Error : Please enter number.")
            return
    
        try :
            choice = int(input("Enter a choice (+,-,*,/) : \n" 
                        "1 : Addition (+) \n" \
                        "2 : Subtraction (-) \n" \
                        "3 : Multiplication (*) \n" \
                        "4 : Division (/) \n" \
                        "Example input : 4 \n"))
        except :
            print("Invalid choice. Please select 1, 2, 3, or 4.")
            return
        
        if choice == 1 :
            r = self.addition(a,b)
            print(f"result {a} + {b} = {r}")
        elif choice == 2 :
            r = self.subtraction(a,b)
            print(f"result {a} - {b} = {r}")
        elif choice == 3 :
            r = self.multiplication(a,b)
            print(f"result {a} * {b} = {r}")
        elif choice == 4 :
            if b == 0 :
                print("It cannot be divided by 0.")
            else :
                r = self.division(a,b)
                print(f"result {a} / {b} = {r:.2f}")
        else :
            print("Invalid choice. Please select 1, 2, 3, or 4.")

app = Calculate()
app.run()