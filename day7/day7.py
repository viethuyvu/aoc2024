import itertools # handle a variety of tasks, such as generating combinations, permutations, and Cartesian products

with open ('input.txt') as f:
    lines = f.readlines()

def evaluate (numbers, operators):
    result = numbers[0]
    for i in range(1,len(numbers)):
        if operators[i-1] == '||':
            result += numbers[i]
        if operators[i-1] == '+':
            result += numbers[i]
        else:
            result *= numbers[i]
    return result

def check_target (target, numbers):
    #generate all possible combinations of operators
    operators_combination = itertools.product(['+', '*'], repeat=len(numbers)-1)

    #try each combinations of operator and check if the result is equal to the target
    for operators in operators_combination:
        if evaluate(numbers, operators) == target:
            return True
    return False

def d7p1 ():
    total_sum = 0
    for line in lines:
        target_str, numbers_str = line.strip().split(':')
        target = int(target_str)
        numbers = list(map(int, numbers_str.strip().split())) # Convert numbers to a list of integers
        if check_target(target, numbers):
            total_sum += target
    return total_sum

def evaluate2 (numbers, operators):
    result = str(numbers[0])
    for i in range(1,len(numbers)):
        if operators[i-1] == '||':
            result += str(numbers[i])
        elif operators[i-1] == '+':
            result = str(int(result) + numbers[i])
        else:
            result = str(int(result) * numbers[i])
    return int(result)

def check_target2 (target, numbers):
    #generate all possible combinations of operators
    operators_combination = itertools.product(['+', '*','||'], repeat=len(numbers)-1)

    #try each combinations of operator and check if the result is equal to the target
    for operators in operators_combination:
        if evaluate2(numbers, operators) == target:
            return True
    return False

def d7p2 ():
    total_sum = 0
    for line in lines:
        target_str, numbers_str = line.strip().split(':')
        target = int(target_str)
        numbers = list(map(int, numbers_str.strip().split())) # Convert numbers to a list of integers
        if check_target2(target, numbers):
            total_sum += target
    return total_sum

if __name__ == '__main__':
    print(d7p1())
    print(d7p2())

