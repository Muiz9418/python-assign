"""
Day 13 - Debugging
Angela Yu's Day 13 is a set of small broken programs you have to fix
using print statements, the Python Tutor visualizer, and a debugger.
Below are 3 classic bugs from that day, each shown as broken -> fixed,
with a note on the debugging technique used.
"""

# ---------------------------------------------------------------
# Bug 1: Off-by-one in a loop
# ---------------------------------------------------------------
def buggy_loop():
    # Bug: range(1, 5) misses 5, and the print is outside the intended scope
    total = 0
    for number in range(1, 5):
        total += number
    print(total)  # prints 10, but "should" sum 1 to 5 = 15


def fixed_loop():
    total = 0
    for number in range(1, 6):  # fix: include 5 by going to 6
        total += number
    print(total)  # 15


# Technique: step through with a debugger/breakpoint and watch `number`
# and `total` on each iteration to spot where the loop stops early.


# ---------------------------------------------------------------
# Bug 2: Mutable default argument / wrong variable reused
# ---------------------------------------------------------------
def buggy_price_check(price, discount_list=[]):
    # Bug: default list is shared across calls, causing values to
    # accumulate unexpectedly between separate function calls.
    discount_list.append(price * 0.9)
    return discount_list


def fixed_price_check(price, discount_list=None):
    if discount_list is None:
        discount_list = []
    discount_list.append(price * 0.9)
    return discount_list


# Technique: print(id(discount_list)) at the top of the function on
# each call — the buggy version keeps the same id, revealing the
# shared-state bug.


# ---------------------------------------------------------------
# Bug 3: Comparing a string to an int
# ---------------------------------------------------------------
def buggy_age_check():
    age = input("What's your age? ")  # returns a string
    if age > 18:  # Bug: TypeError, can't compare str > int
        print("You can vote.")


def fixed_age_check():
    age = int(input("What's your age? "))  # fix: convert to int
    if age > 18:
        print("You can vote.")


# Technique: read the traceback from the bottom up — Python names
# the exact line and the TypeError tells you the two types involved.


if __name__ == "__main__":
    print("Fixed loop result:")
    fixed_loop()

    print("Fixed price check:")
    print(fixed_price_check(100))
    print(fixed_price_check(50))  # won't carry over the previous call's value

    print("Fixed age check:")
    fixed_age_check()
