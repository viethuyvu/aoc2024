stones = dict()

with open('input.txt') as f:
    numbers = list(map(int, f.read().strip().split()))

for n in numbers:
    stones[n] = 1

def blink_one(stones):
    new_stones = dict()
    for stone, freq in stones.items():
        if stone == 0:
            if 1 in new_stones.keys():
                new_stones[1] += freq
            else:
                new_stones[1] = freq
        elif len(str(stone))%2 == 0:
            mid = len(str(stone))//2
            left = int(str(stone)[:mid])
            right = int(str(stone)[mid:])
            if left in new_stones.keys():
                new_stones[left] += freq
            else:
                new_stones[left] = freq
            if right in new_stones.keys():
                new_stones[right] += freq
            else:
                new_stones[right] = freq
        else:
            if stone*2024 in new_stones.keys():
                new_stones[stone*2024] += freq
            else:
                new_stones[stone*2024] = freq
    return new_stones

def blink(stones, n):
    for _ in range(n):
        stones = blink_one(stones)
    return stones

if __name__ == '__main__':
    print(sum(blink(stones, 25).values()))
    print(sum(blink(stones, 75).values()))
