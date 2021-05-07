# Input: n = 4
# Output: 5
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step + 1 step
# 2. 1 step + 2 steps + 1 step
# 3. 2 steps + 1 step + 1 step
# 4. 2 steps + 2 steps
# 5. 1 step + 1 step + 2 steps

# Input: n = 5
# Output: 8
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step + 1 step + 1 step
# 2. 1 step + 1 step + 1 step + 2 steps
# 3. 1 step + 1 step + 2 steps + 1 step
# 4. 1 step + 2 steps + 1 step + 1 step
# 5. 2 steps + 1 step + 1 step + 1 step
# 6. 1 step + 2 steps + 2 steps
# 7. 2 steps + 1 step + 2 steps
# 8. 2 steps + 2 steps + 1 step

# n = 0
# 0 outcomes
# n = 1
# 1 outcomes, + 1
# n = 2
# 2 outcomes, + 2
# n = 3
# 3 outcomes, + 3
# n = 4
# 5 outcomes, + 5
# n = 5
# 8 outcomes, + 8

def stair(n):
    prev = 0
    prev2 = 0
    for i in range(n):
        if i == 0:
            prev = 1
        if i == (n - 1):
            return prev + prev2
        else:
            total = prev + prev2
            prev2 = prev
            prev = total

n = 6
print(stair(n))



