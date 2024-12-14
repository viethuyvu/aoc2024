#with ensures the file is properly closed after reading
with open ("input.txt","r") as file: #  # open() opens the file in read mode ('r').
    lines = file.readlines() # readlines() reads the individual lines into a list of string

list1 = []
list2 = []

for line in lines:
    num1,num2 = map(int, line.split()) # map(int, ...) converts each split string to an integer
    list1.append(num1)
    list2.append(num2)

def d1p1(list1,list2):
    list1.sort()
    list2.sort()
    result = sum (abs(a-b) for a,b in zip(list1,list2)) 
    return result

def d1p2(list1, list2):
    result = 0
    for num in list1:
        count = list2.count(num)
        product = num * count
        result += product
    return result

if __name__ == "__main__":
    print(d1p1(list1,list2))
    print(d1p2(list1,list2))