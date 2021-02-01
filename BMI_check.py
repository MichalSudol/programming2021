#BMI Check 
#Author Michal Sudol = GMIT G00398852@gmit.ie


print('\n GMIT BMI CALCULATOR v2 2021 - MS \n')

cm = int(input(' Please insert your height in cm :'))
kg = int(input('\n Please insert your weight in kg :'))

m = (cm / 100)

bmi = (kg/(m*m))

if (bmi < 19):
    print('\n Your BMI result is :' + str(bmi) + '. You are: Thin    ')
elif (bmi < 25):
    print('\n Your BMI result is :' + str(bmi) + '. You are: Healthy ')
elif (bmi < 30):
    print('\n Your BMI result is :' + str(bmi) + '. You are: Slight Overweight ')
else:
    print('\n Your BMI result is :' + str(bmi) + '. You are: Slight Obese ')

input('\n Thanks for using! press Enter to exit.')