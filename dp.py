def remove_element(nums, val):
    pop_indexes = []
    for i in range(len(nums)):
        if nums[i] == val:
            pop_indexes.append(i)
    while pop_indexes:
        nums.pop(pop_indexes.pop())
    return len(nums)


def remove_elements(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i+=1
    return i
        

def find_max_min(nums):
    if len(nums) == 0:
        return None
    max = min = nums[0]
    for i in range(len(nums)):
        if nums[i] < min:
            min = nums[i]
        elif nums[i] > max:
            max = nums[i]
    return (max, min)
        
    
def find_longest_string(list1):
    if not list1:
        return ''
    max = list1[0]    
    for i in list1:
        if len(i) > len(max):
            max = i
    return max


def remove_duplicates(nums):
    if len(nums) < 2:
        return len(nums)
    swap_index = 1
    prev = nums[0]
    for i in nums:
        if i != prev:
            nums[swap_index] = i
            prev = i
            swap_index += 1
    return swap_index


def max_profit(nums):
    if len(nums) < 2:
        return 0
    buy_index = 0 
    sell_index = len(nums)-1
    for i in range(len(nums)):
        if nums[i] < nums[buy_index] and i < sell_index:
            buy_index = i
        if nums[i] > nums[sell_index] and i > buy_index:
            sell_index = i
    profit = nums[sell_index] - nums[buy_index]
    return profit if profit > 0 else 0
    

def rotate(nums, k):
    for _ in range(k):
        nums.insert(0, nums.pop())


def max_subarray(nums):
    if len(nums) == 0:
        return 0

    max_curr = max_res = nums[0]
    for i in range(1, len(nums)):
        max_curr = max(nums[i], max_curr + nums[i])
        if max_curr > max_res:
            max_res = max_curr
    return max_res


def max_subarray_index(nums, k):
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return (0, 0)
    hash_map = {}
    curr_sum = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        hash_map[curr_sum] = i
        
        if curr_sum == k:
            return (0, i)
        
        if (curr_sum - k) in hash_map:
            return (hash_map[curr_sum-k]+1, i)
        
        


# Example 1: Simple case with positive and negative numbers

input_case_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result_1 = max_subarray(input_case_1)
index = max_subarray_index(input_case_1, result_1)
print("Example 1: Input:", input_case_1, "\nResult:", result_1)  
print(index)

# Example 2: Case with a negative number in the middle
input_case_2 = [1, 2, 3, -4, 5, 6]
result_2 = max_subarray(input_case_2)
index = max_subarray_index(input_case_2, result_2)
print("Example 2: Input:", input_case_2, "\nResult:", result_2) 
print(index)

# Example 3: Case with all negative numbers
input_case_3 = [-1, -2, -3, -4, -5]
result_3 = max_subarray(input_case_3)
index = max_subarray_index(input_case_3, result_3)
print("Example 3: Input:", input_case_3, "\nResult:", result_3) 
print(index)


"""
    EXPECTED OUTPUT:
    ----------------
    Example 1: Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
    Result: 6
    Example 2: Input: [1, 2, 3, -4, 5, 6] 
    Result: 13
    Example 3: Input: [-1, -2, -3, -4, -5] 
    Result: -1
    
"""