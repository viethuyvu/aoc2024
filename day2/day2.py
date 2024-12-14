with open ("input.txt","r") as file:
    lines = file.readlines()

report = []
for line in lines:
    seperated = list (map(int, line.split())) # split by space and covnert to integer
    report.append(seperated)

def d2p1(report):
    safecount = 0
    for lst in report:
        increasing = all (lst[i] < lst[i+1] for i in range(len(lst)-1)) # all is used to check if all elements are True
        decreasing = all (lst[i] > lst[i+1] for i in range(len(lst)-1))
        if increasing:
            if (all (lst[i+1]-lst[i] <= 3 for i in range (len(lst)-1))):
                safecount += 1
        elif decreasing:
            if (all (lst[i]-lst[i+1] <= 3 for i in range (len(lst)-1))):
                safecount += 1
    return safecount

def is_safe(lst):
    increasing = all (lst[i] < lst[i+1] for i in range(len(lst)-1))
    decreasing = all (lst[i] > lst[i+1] for i in range(len(lst)-1))
    if increasing:
        if (all (lst[i+1]-lst[i] <= 3 for i in range (len(lst)-1))):
            return True
    elif decreasing:
        if (all (lst[i]-lst[i+1] <= 3 for i in range (len(lst)-1))):
            return True
    return False

def d2p2(report):
    safecount = 0
    for lst in report:
        if is_safe(lst):
            safecount += 1
        else: # Try removing one element at a time and check if the remaining list is safe
            for i in range (len(lst)):
                if is_safe(lst[:i]+lst[i+1:]): # Create a new list by removing the element at index i
                    safecount += 1
                    break
    return safecount

if __name__ == "__main__":
    print(d2p1(report))
    print(d2p2(report))

