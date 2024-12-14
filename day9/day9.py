with open ('input.txt') as f:
    data = f.read().strip()

def swap_position (lst):
    front = 0
    back = len(lst) - 1
    while front < back:
        while front < back and lst[front] != '.':
            front += 1
        while back >= 0 and lst[back] == '.':
            back -= 1

        if front < back:
            lst[front], lst[back] = lst[back], lst[front]
            front += 1
            back -= 1

    return lst

def check_sum (lst):
    i = 0
    checksum = 0
    while i < len(lst):
        if lst[i] != '.':
            checksum = checksum + int(lst[i])*i
            
        i += 1
    return checksum

def d9p1():
    memory_blocks = []
    id = 0
    for i in range(len(data)):
        if i % 2 == 0:
            for j in range(int(data[i])):
                memory_blocks.append(id)
            id += 1
        else:
            for j in range(int(data[i])):
                memory_blocks.append('.')
    
    return check_sum(swap_position(memory_blocks))

def find_free(lst):
    free_list = []
    count = 0
    #find the first free space
    for i in range(len(lst)):
        if lst[i] == '.':
            if count == 0:
                start = i
            count +=1
        else:
            if count > 0:
                end = i
                free_list.append([start, end])
                count = 0
    if count > 0:
        free_list.append([start, len(lst)])
        
    return free_list

def move_file(memory_blocks, memory_lengths):
    i = len(memory_blocks) - 1
    empty_space = find_free(memory_blocks)
    while i >= 0:
        if memory_blocks[i] != '.':
            possbile = False
            for space in empty_space:
                length_index = int(memory_blocks[i])
                if space[1] - space[0] >= memory_lengths[length_index]:
                    if space[0] < i:
                        for j in range(space[0], space[0] + memory_lengths[length_index]):
                            memory_blocks[j], memory_blocks[i-j+space[0]] = memory_blocks[i-j+space[0]], memory_blocks[j]
                        i = i - memory_lengths[length_index]  # Decrement i by the length of the moved block
                        possbile = True
                        space[0] += memory_lengths[length_index]
                        break
            if not possbile:
                i -= 1
        else:
            i -= 1
    return memory_blocks

def d9p2():
    memory_blocks = []
    memory_lengths = []
    id = 0
    for i in range(len(data)):
        if i % 2 == 0:
            memory_lengths.append(int(data[i]))
            for j in range(int(data[i])):
                memory_blocks.append(id)
            id += 1
        else:
            for j in range(int(data[i])):
                memory_blocks.append('.')
    with open ('output.txt','w') as f:
        f.write(str(memory_blocks))
    return check_sum(move_file(memory_blocks, memory_lengths))

if __name__ == '__main__':
    print(d9p1())
    print(d9p2())
    
