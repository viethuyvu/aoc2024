#defaultdict automatically initializes a default value for a key that doesn't exist yet. 
# This eliminates the need for explicit key checking before accessing or modifying values.
from collections import defaultdict, deque
import networkx as nx #Python package for creating, analyzing, and manipulating complex networks and graphs

with open ('input.txt') as f:
    data = f.read()

rules_part, update_part = data.split('\n\n')  

rules = []
for line in rules_part.strip().splitlines(): #Clean up the string with strip(), split the string into lines with splitlines()
    before, after = map(int, line.split('|'))
    rules.append((before, after))

updates = []
for line in update_part.strip().splitlines():
    numbers = list(map(int,line.split(',')))
    updates.append(numbers)

def addpred (pred, num):
    for rule in rules:
        if rule[1] == num:
            pred.append(rule[0])
            
    return pred

def d5p1 ():
    result = 0
    for line in updates:
        valid = True
        pred = addpred([],line[0])
        for i in range (1,len(line)):
            if line[i] not in pred:
                pred = addpred(pred,line[i])
            else:
                valid = False
                break

        if valid:
            result += line[len(line)//2]

    return result

def is_valid(line, rules):
    # Create a dictionary of positions for O(1) lookup
    relevant_rules = [(x, y) for x, y in rules if x in line and y in line]
    positions = {num: i for i, num in enumerate(line)}
    
    # Check all applicable rules
    for before, after in relevant_rules:
        if positions[before] > positions[after]:
            return False
    return True

def sort_pages(line,rules):
    # Create a directed graph
    G = nx.DiGraph()
    
    # Add edges for rules that apply to these pages
    for before, after in rules:
        if before in line and after in line:
            G.add_edge(before, after)
    
    try:
        # Perform topological sort
        sorted_pages = list(nx.topological_sort(G))
        # Filter to only include pages we need
        return [p for p in sorted_pages if p in line]
    except nx.NetworkXUnfeasible:
        # If there's a cycle, return None
        return None



def d5p2():
    
    result = 0
    
    # Find and fix only the incorrect updates
    incorrect_updates = [line for line in updates if not is_valid(line, rules)]
    
    for line in incorrect_updates:  # Only process incorrect updates
        fixed_line = sort_pages(line, rules)
        result += fixed_line[len(fixed_line) // 2]
    
    return result

if __name__ == "__main__":
    print(d5p1())
    print(d5p2())
