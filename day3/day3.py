# module for regular expressions
import re

with open ("input.txt","r") as file:
    content = file.read()



def d3p1():
    # r before the string make it a raw string, avoids escape characters
    # mul\( matches the string mul(
    # \d{1,3} matches 1 to 3 digits
    # , matches the comma
    # \) matches the closing parenthesis
    pattern1 = r'mul\(\d{1,3},\d{1,3}\)'
    mul_list = re.findall(pattern1, content)
    pattern2 = r'mul\((\d{1,3}),(\d{1,3})\)' #The parentheses around \d{1,3} are for creating group of digits so that they can be accessed
    total_sum = 0
    for mul in mul_list:
        match = re.match(pattern2,mul)
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
            total_sum += x*y
    return total_sum

def d3p2():
    neededpattern = r'(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))'
    cleanup = re.findall(neededpattern,content)
    action = True
    total_sum = 0
    for element in cleanup:
        if element[0] == "do()":
            action = True
        elif element[0] == "don't()":
            action = False
        else:
            if action:
                total_sum += int(element[1])*int(element[2])
    
    return total_sum

if __name__ == "__main__":
    print(d3p1())
    print(d3p2())

