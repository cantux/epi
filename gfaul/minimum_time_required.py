# You are planning production for an order. 
# You have a number of machines that each have a fixed number of days to produce an item. 
# Given that all the machines operate simultaneously, determine the minimum number of days to produce the required order.
# 
# For example, you have to produce goal=10 items. You have three machines that take machines = [2, 3, 2] days to produce an item. 
# The following is a schedule of items produced:
# 
# Day Production  Count
# 2   2               2
# 3   1               3
# 4   2               5
# 6   3               8
# 8   2              10
# It takes  days to produce  items using these machines.

def minTime(machines, goal):

    machines.sort()

    low_rate = machines[0]
    lower_bound = (goal // (len(machines) / low_rate))
    high_rate = machines[-1]
    upper_bound = (goal // (len(machines) / high_rate)) + 1

    while lower_bound < upper_bound:

        num_days = (lower_bound + upper_bound) // 2
        total = getNumItems(machines, goal, num_days)
        if total >= goal:
            upper_bound = num_days
        else:
            lower_bound = num_days + 1

    return int(lower_bound)


def getNumItems(machines, goal, num_days):

    total = 0

    for machine in machines:
        total += (num_days // machine)

    return total
