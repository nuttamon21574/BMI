weight = float(input("Enter your weight : " ))
height = float(input("Enter your height : " ))
BMI = weight/(height**2)


if BMI < 18.5 :
  print("underweight")
elif 18.5 < BMI < 24.9:
  print("normal")
else :
  print("overweight")

