"""
Problem: "Positive Numbers In A List"

Given an array of integers, write a function in Python that returns the count of positive numbers in the array.

Function Signature:

python
Copy code
def count_positive_numbers(arr: List[int]) -> int:
    pass
Test Case:

python
Copy code
assert count_positive_numbers([1, -2, 3, -4, 5, -6, 7, -8, 9]) == 5
assert count_positive_numbers([-1, -2, -3, -4, -5, -6, -7, -8, -9]) == 0
assert count_positive_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
assert count_positive_numbers([]) == 0
Expected Complexity:

The time complexity should be O(n), where n is the length of the array.
The space complexity should be O(1), as we don't need any extra space other than the input array.
This problem focuses on using a for loop to iterate through an array and performing a simple comparison operation. The problem is designed to be a beginner-friendly introduction to loops in Python and the concept of array traversal.



"""
