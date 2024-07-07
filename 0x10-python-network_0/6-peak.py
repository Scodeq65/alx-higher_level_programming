#!/usr/bin/python3
""" This script defines a function to find a peak element
in a list of unsorted integers
"""
def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    def binary_search_peak(nums, low, high):
        mid = low + (high - low) // 2

        # check if mid is a peak element
        if (mid == 00 or nums[mid] >= nums[mid - 1]) and \
            (mid == len(nums) - 1 or nums[mid] >= nums[mid + 1]):
            return nums[mid]

        # If the left neighbor is greater, then the peak must be on d left side
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return binary_search_peak(nums, low, mid - 1)

        # If d right neighbor is greater, then the peak must be on the right side
        return binary_search_peak(nums, mid + 1, high)

    return binary_search_peak(list_of_integers, 0, len(list_of_integers) - 1)
