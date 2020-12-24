mass = int(input("Enter your weight (in pounds): "))
feet = int(input("Enter your height (in feet): "))
inches = int(input("Enter your height (in inches): "))

height = (12 * feet) + inches
BMI = round((mass / (height * height) * 703), 2)

if BMI < 18.5:
  print ("Your BMI is " + str(BMI) + ". You are underweight!")
elif BMI >= 18.5 and BMI <= 24.9:
  print("Your BMI is " + str(BMI) + ". Your weight is normal.")
elif BMI >= 25 and BMI <= 29.9:
  print("Your BMI is " + str(BMI) + ". You are overweight!")
elif BMI >= 30:
  print("Your BMI is " + str(BMI) + ". You are obese! Lose weight A.S.A.P.!")

