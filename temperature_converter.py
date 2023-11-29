print("Welcome to temperature converter, a lightweight utility for converting temperatures")

#Create variables for the unit that's being converted and the temperature
unit = input("Please specify the temperature you want converted: ").upper()
value = float(input("Please specify the temperature you want converted: "))
# Function that converts C to F
def c_to_f(temp_c):
    converted_c = temp_c * (9/5) + 32
    return converted_c


# Function that converts F to C
def f_to_c(temp_f):
    converted_f = (temp_f - 32) * (5/9)
    return converted_f

# Function that converts K to F
def k_to_f(temp_k):
    converted_k = (temp_k - 273.15) * (9/5) + 32
    return converted_k

# Function that converts F to K
def f_to_k(temp_f):
    converted_f = (temp_f - 459.67) * (5/9)
    return converted_f

# Main Function that uses Conditionals to decide which convert function to select
def main():
    if(unit == "C"):
        celsius_to_Fahrenheit = c_to_f(value)
        return celsius_to_Fahrenheit
    elif(unit == "F"):
        fahrenheit_to_celsius = f_to_c(value)
        return fahrenheit_to_celsius
    elif(unit == "K"):
        kelvin_to_fahrenheit = k_to_f(value)
        return kelvin_to_fahrenheit
    else:
        warning = "Please enter C, F, or K to specify the unit: "
        return warning

#Print results 
result = main()
print("Your value is: " + str(result))

