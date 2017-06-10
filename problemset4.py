#
# Problem 1
#

def nest_egg_fixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    F = [salary * save * 0.01]
    for i in range(1, years):
        F.append(F[i-1] * (1 + growthRate * 0.01) + salary * save * 0.01)

    return F


def test_nest_egg_fixed():
    salary = 10000
    save = 10
    growth_rate = 15
    years = 5
    savings_record = nest_egg_fixed(salary, save, growth_rate, years)
    print(savings_record)
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

#
# Problem 2
#


def nest_egg_variable(salary, save, growthRates):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """
    F = [salary * save * 0.01]
    for i in range(1, len(growthRates)):
        F.append(F[i-1] * (1 + growthRates[i] * 0.01) + salary * save * 0.01)
    return F


def test_nest_egg_variable():
    salary = 10000
    save = 10
    growth_rates = [3, 4, 5, 0, 3]
    savings_record = nest_egg_variable(salary, save, growth_rates)
    print(savings_record)
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

#
# Problem 3
#


def post_retirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    F = [savings * (1 + growthRates[0] * 0.01) - expenses]
    for i in range(1, len(growthRates)):
        F.append(F[i-1] * (1 + growthRates[i] * 0.01) - expenses)
    return F


def test_post_retirement():
    savings = 100000
    growth_rates = [10, 5, 0, 5, 1]
    expenses = 30000
    savings_record = post_retirement(savings, growth_rates, expenses)
    print(savings_record)
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

#
# Problem 4
#


def find_max_expenses(salary, save, preRetireGrowthRates, postRetireGrowthRates, epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    pre_retirement_fund = nest_egg_variable(salary, save, preRetireGrowthRates)[-1]
    max_bound = pre_retirement_fund
    min_bound = 0
    remaining = pre_retirement_fund
    i = 1
    expense = 0
    while abs(remaining) > epsilon and i < 1000:
        expense = (max_bound + min_bound) / 2
        remaining = post_retirement(pre_retirement_fund, postRetireGrowthRates, expense)[-1]
        if remaining < 0:
            max_bound = expense
        else:
            min_bound = expense

        i += 1

    if i == 1000:
        raise Exception('Not found in 1000 iterations')

    return expense


def test_find_max_expenses():
    salary = 10000
    save = 10
    pre_retire_growth_rates  = [3, 4, 5, 0, 3]
    post_retire_growth_rates = [10, 5, 0, 5, 1]
    epsilon = .01
    expenses = find_max_expenses(salary, save, pre_retire_growth_rates, post_retire_growth_rates, epsilon)
    print(expenses)
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.

if __name__ == '__main__':
    test_nest_egg_fixed()
    test_nest_egg_variable()
    test_post_retirement()
    test_find_max_expenses()


