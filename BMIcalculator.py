def calculate_bmi(weight, height):
    """Calculate BMI given weight in kilograms and height in meters."""
    return weight / (height ** 2)

def get_bmi_category(bmi):
    """Classify BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the Command-line BMI Calculator!")
    
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")
    except ValueError:
        print("Invalid input. Please enter numerical values for weight and height.")

if __name__ == "__main__":
    main()
