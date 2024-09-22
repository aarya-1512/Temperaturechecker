try:
    user = float(input("Enter the patient's temperature in degrees Fahrenheit: "))
    if user >= 99.5:
        print("The patient has a high temperature.")
    elif user < 99.5:
        print("The patient's temperature is normal.")
except ValueError:
    print("Error: Please enter a valid temperature (numeric value).")

