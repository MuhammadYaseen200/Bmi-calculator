def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)
        return bmi
    except ZeroDivisionError:
        return "Height cannot be zero."

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
        else:
            bmi = calculate_bmi(weight, height)
            print(f"Your BMI is: {bmi:.2f}")
            print(f"You are classified as: {bmi_category(bmi)}")
    except ValueError:
        print("Please enter valid numeric values for weight and height.")

if __name__ == "__main__":
    main()
