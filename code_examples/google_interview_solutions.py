# [1, 2, 3, 9]
# 1, 2, 4, 4]

def simple_solution(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] + l[j] == 8:
                return True
    return False

# Suggested a binary search approach

def has_pair_with_sum(l, sum):
    low = 0
    high = len(l)-1

    while low < high:
        s = l[low] + l[high]

        if s == sum:
            return True
        elif s < sum:
            low += 1
        elif s > sum:
            high -= 1
    
    return False

# [1, 2, 3, 9]

def has_pair_with_sum_unordered(l, sum):
    comp = set()

    for i in l:
        if i in comp:
            return True
        comp.add(sum - i)
    
    return False

