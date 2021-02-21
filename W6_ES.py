# GMIT PforCS2021
# Author Michal Sudol G00398852@gmit.ie
# Python - program that reads in a text file and outputs the number


fname = input("Text.txt")
 
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter.isdigit()):
                    print(letter)