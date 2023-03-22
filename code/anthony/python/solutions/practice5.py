

# Practice 5: Lists
# Copy and paste this file into your own "05_lists.py"
# Fill in the code for each of the functions


# Even Even
# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.

def is_even(num):
    return num % 2 == 0


def even_even(nums):
    # Loop
    counter = 0
    for i in range(0, len(nums)):
        # Check each number to see if its even
        if is_even(nums[i]):
            # Count number of even numbers
            # counter = counter + 1
            counter += 1
            # counter = counter * 4
            # counter *= 4

    if is_even(counter):
        return True
    else:
        return False


print("even_even\t", even_even([5, 6, 2]) == True)
print("even_even\t", even_even([5, 5, 2]) == False)


# Reverse
# Write a function that takes a list and returns a new list with the elements in reverse order

def reverse(nums: list):
    nums.reverse()
    return nums


print("reverse\t\t", reverse([1, 2, 3]) == [3, 2, 1])


# Common Elements
# Write a function to find all common elements between two lists.


def common_elements(nums1, nums2):

    common = []
    # loop over listA
    for i in range(0, len(nums1)):
        if nums1[i] in nums2:
            common.append(nums1[i])
    # return list of common elements
    return common


print("common_elements\t", common_elements(
    [1, 2, 3], [2, 3, 4]) == [2, 3])  # [2, 3]


# Combine
# Write a function to combine two lists of equal length into one, alternating elements.


def combine(nums1, nums2):
    combined = []
    if len(nums1) == len(nums2):
        for i in range(0, len(nums1)):
            combined.append(nums1[i])
            combined.append(nums2[i])

    return combined


print("combine\t\t", combine(['a', 'b', 'c'], [1, 2, 3]) == [
      'a', 1, 'b', 2, 'c', 3])  # ['a', 1, 'b', 2, 'c', 3]


# Find Pair
# Given a list of numbers, and a target number,
# find a pair of numbers from the list that sum to a target number.
# Optional: return a list of all pairs of numbers that sum to a target value.


def find_pair(nums, target):

    # nums[0] + nums[1] == target
    # nums[0] + nums[2] == target
    # nums[0] + nums[3] == target
    # nums[1] + nums[2]
    # nums[1] + nums[3]
    # nums[2] + nums[3]
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]


print("find_pair\t", find_pair([5, 6, 2, 3], 7) == [5, 2])  # [5, 2]


# Average
# Write a function to find the average of a list of numbers


def average(nums):
    ...


print("average\t\t", average([1, 2, 3, 4, 5]) == 3)  # 3


# Remove Empty
# Write a function to remove all empty strings from a list.


def remove_empty(mylist):
    ...


print("remove_empty\t", remove_empty(['a', 'b', '', 'c', '', 'd']) == [
      'a', 'b', 'c', 'd'])  # ['a', 'b', 'c', 'd']


# Merge
# Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.

def merge(nums1, nums2):
    ...


print("merge\t\t", merge([5, 2, 1], [6, 8, 2]) == [
      [5, 6], [2, 8], [1, 2]])  # [[5,6],[2,8],[1,2]]


# Combine All
# Write a function `combine_all` that takes a list of lists, and returns a list containing each element from each of the lists.


def combine_all(nums):
    ...


print("combine_all\t", combine_all([[5, 2, 3], [4, 5, 1], [7, 6, 3]]) == [
      5, 2, 3, 4, 5, 1, 7, 6, 3])  # [5,2,3,4,5,1,7,6,3]
