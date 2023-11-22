"""
Description of your module.

Author: kodamsupriya4
Date: 2023-10-19
"""

def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index) using weight (in kilograms) and height (in meters).

    :param weight: The weight in kilograms.
    :param height: The height in meters.
    :return: The calculated BMI as a floating-point number.
    """
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    """
    Classify the BMI value into health categories.

    :param bmi: The calculated BMI value.
    :return: The classification as a string (e.g., "Underweight," "Normal Weight," etc.).
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    """
    Main function to get user input, calculate BMI, and display the result.
    """
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Invalid input. Weight and height must be positive numbers.")
            return

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    main()