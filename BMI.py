weight = float(input("Enter your weight (kg.) : " ))
height = float(input("Enter your height (cm.) : " ))
h_meter = height/100
BMI = weight/(h_meter**2)

print("ค่า BMI ของคุณคือ: ", BMI)

if BMI > 24.9 :
  print("overweight")
elif 18.5 < BMI < 24.9:
  print("normal")
else :
  print("underweight")

