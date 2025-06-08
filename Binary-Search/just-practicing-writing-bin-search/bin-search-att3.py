def bin_search(nums: list[int], target: int):
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = start + (start + end ) // 2

        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            return mid
    return -1
