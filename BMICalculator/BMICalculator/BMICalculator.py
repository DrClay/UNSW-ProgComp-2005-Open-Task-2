# file = open('Test1.txt')
file = open('Test2.txt')

for line in file:
    weight, height = map(float, line.strip().split())
    height = height / 100
    bmi = weight/(height**2)
    if bmi < 18.5:
        status = "Underweight"
    elif bmi < 25:
        status = "Normal"
    elif bmi < 30:
        status = "Overweight"
    else:
        status = "Obese"

    if weight >= 100.0:
        print('{:3.1f}kg  {:3.0f}cm  BMI={:2.1f}  {}'.format(weight, height*100, bmi, status))
    else:
        print('{: 3.1f}kg  {:3.0f}cm  BMI={:2.1f}  {}'.format(weight, height*100, bmi, status))

