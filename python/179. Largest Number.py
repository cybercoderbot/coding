"""
179. Largest Number
Medium

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

"""


"""
1-we define a function that compares two string (a,b) . we consider a bigger than b if a+b>b+a
for example : (a="2",b="11") a is bigger than b because "211" >"112"

2-convert all elements of the list from int to string

3-sort the list descendingly using the comparing function we defined
for example sorting this list ["2","11","13"] using the function defined in step 1 would produce ["2","13","11"]

4-we concatatenate the list "21311"
"""


def cmp_func(x, y):
    """Sorted by value of concatenated string increasingly."""
    if x + y > y + x:
        return 1
    elif x == y:
        return 0
    else:
        return -1


class Solution:

    def largestNumber(self, nums: List[int]) -> str:

        # Build nums contains all numbers in the String format.
        nums = [str(x) for x in nums]

        # Sort nums by cmp_func decreasingly.
        nums.sort(key=cmp_to_key(cmp_func), reverse=True)

        # Remove leading 0s, if empty return '0'.
        return ''.join(nums).lstrip('0') or '0'
