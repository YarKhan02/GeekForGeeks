def merge_sort(nums, depth = 0):

    if len(nums) < 2:
        return nums

    mid = len(nums) // 2

    return merge(merge_sort(nums[:mid], depth + 1), merge_sort(nums[mid:], depth + 1))


def merge(nums1, nums2, depth = 0):
    merged = []
    i = 0
    j = 0

    while i < len(nums1) and j < len(nums2):

        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    return merged + nums1[i:] + nums2[j:]

def enter(nums):
    m = merge_sort(nums)

    return m[:-2]
    

print(enter([2, 8, 7, 1, 5]))