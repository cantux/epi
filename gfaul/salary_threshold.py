#!/usr/bin/env python

def adjust(salaries, target):
    # start by assuming we will pay the current salary for every employee

    # keep track of the funds we have left 
    # as we go over the salaries, update the left over funds

    # check on every encountered salary if we can pay that salary to people left over
    # this means we will pay the same for employees left up the curve return it. 

    len_salaries = len(salaries)
    salaries.sort()

    funds_left = target

    for i, current_salary in enumerate(salaries):
        emp_left = len_salaries - i 
        candidate_spendeture = emp_left * current_salary
        if candidate_spendeture > funds_left:
            return funds_left / emp_left
        funds_left -= current_salary 

    return 0


def epi(current_salaries, target_payroll):
    current_salaries.sort()
    unadjusted_salary_sum = 0.0

    for i, current_salary in enumerate(current_salaries):
        adjusted_people = len(current_salaries) - i
        adjusted_salary_sum = current_salary * adjusted_people

        if unadjusted_salary_sum + adjusted_salary_sum >= target_payroll:
            return (target_payroll - unadjusted_salary_sum) / adjusted_people
        unadjusted_salary_sum += current_salary

    return -1.0

def find_salary_cap(salaries, budget):
    sortedSalaries = sorted(salaries)
    salaryCap = float(budget) / len(salaries)
    for index, salary in enumerate(sortedSalaries):
        if salary <= salaryCap:
            overAllocated = salaryCap - salary
            restOfSal = (len(salaries) - 1) - index
            salaryCap += (overAllocated / float(restOfSal))
    return salaryCap


def bin_search(sal, budget):
    sal.sort()

    def calc(cap):
        sum = 0
        for s in sal:
            sum += min(s, cap)
        return sum

    lo, hi = 0, sal[-1]

    while lo <= hi:
        mid = lo + ((hi - lo) // 2)
        calc_res = calc(mid)
        if calc_res == budget:
            return mid
        elif calc_res > budget:
            hi = mid
        else:
            lo = mid

def test():
    lst = [20, 30, 40, 90, 100]
    print epi(lst, 210)
    print adjust(lst, 210)
    print find_salary_cap(lst, 210)
    print bin_search(lst, 210)

    lst = [20, 30, 40, 90, 100]
    print epi(lst, 10)
    print adjust(lst, 10)
    print find_salary_cap(lst, 10)
    print bin_search(lst, 10)

    lst = [20, 30, 40, 90, 100]
    print epi(lst, 20)
    print adjust(lst, 20)
    print find_salary_cap(lst, 20)
    print bin_search(lst, 20)
    
    lst = [100, 200, 300, 500]
    print epi(lst, 300)
    print adjust(lst, 300)
    print find_salary_cap(lst, 300)
    print bin_search(lst, 300)


if __name__ == "__main__":
    test()

