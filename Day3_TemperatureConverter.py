class Temperature_converter :
    def __init__(self) :
        pass
    def celsius_to_fahrenheit(self,celsius) :
        return (celsius * (9/5)) + 32
    def fahrenheit_to_celsius(self,fahrenheit) :
        return (fahrenheit - 32) * 5/9

    def run(self) :
        try :
            choice = int(input("Select the conversion type : \n" \
                        "1. Celsius to Fahrenheit\n" \
                        "2. Fahrenheit to Celsius\n" \
                        "" \
                        "Enter choice (1 or 2) : "))

            if choice == 1 :
                try :
                    celsius = float(input("Enter temperature in Celsius : "))
                except ValueError :
                    print("Error : Please enter the number.")
                    return
                r = self.celsius_to_fahrenheit(celsius)
                print(f"Temperature in Fahrenheit : {r:.1f}°F")
            elif choice == 2 :
                try :
                    fahrenheit = float(input("Enter temperature in Fahrenheit : "))
                except ValueError :
                    print("Error : Please enter the number.")
                    return
                r = self.fahrenheit_to_celsius(fahrenheit)
                print(f"Temperature in Celsius : {r:.1f}°C")
            else :
                print("Error : Please select 1 or 2")
        except ValueError :
            print("Error : Please select 1 or 2")
            return


app = Temperature_converter()
app.run()