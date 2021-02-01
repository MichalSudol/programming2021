#BMI Calculator
#Author Michal Sudol = GMIT G00398852@gmit.ie

print('\n GMIT BMI v1 2021 - MS \n')

def bmi():
     a = float(w)/(float(h)*float(h))
     return a
    
again = "y"

while again.lower() == "y":
    w = input("Enter your Weigth (kg)")
    h = input("Enter your Height (m.cm)")


    
    print ("Your BMI is :", bmi())

    again = input("Do you want to try again?y/n:")
    if again == "n":
        print('Enjoy the healthy Day!!');
        break