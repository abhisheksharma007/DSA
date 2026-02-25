class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)
            
    def set_item(self, key, value):
        hash = self.__hash(key)
        if not self.data_map[hash]:
            self.data_map[hash] = []
        self.data_map[hash].append([key, value])
        
    def get_item(self, key):
        hash = self.__hash(key)
        if self.data_map[hash]:
            for i in self.data_map[hash]:
                if i[0] == key:
                    return i[1]
        return None
    
    def keys(self):
        keys = []
        if self.data_map:
            for i in self.data_map:
                if i: keys.extend([j[0] for j in i])
        return keys


#advance
def check_item_in_common(list1, list2):
    # return bool(set(list1) & set(list2))
    hash_map = {}
    for i in list1:
        hash_map[i] = True
    for i in list2:
        if i in hash_map:
            return True
    return False


def find_duplicates(list1):
    hash_map = {}
    dups = []
    for i in list1:
        if i in hash_map:
            if i not in dups: dups.append(i)
            continue
        hash_map[i] = True
    return dups


def first_non_repeating_char(string):
    if len(string) == 1: 
        return string
    hash_map1 = {}
    for i in string:
        if i not in hash_map1:
            hash_map1[i] = 1
        else:
            hash_map1.pop(i)
            if hash_map1:
                return next(iter(hash_map1))
    if hash_map1:
        return next(iter(hash_map1))
    return None
            

def group_anagrams(list1):
    if not list1:
        return []
    if len(list1) == 1:
        return [list1]
    hash_map = {}
    res = []
    for i in list1:
        temp = ''.join(sorted(i))
        if temp not in hash_map:
            hash_map[temp] = [i]
        else:
            hash_map[temp].append(i)
    return list(hash_map.values())
    


def two_sum(list1, target):
    hash_map = {}
    for i in range(len(list1)):
        if target - list1[i] in hash_map and hash_map.get(target - list1[i]) != i:
            return [hash_map[target - list1[i]], i]
        hash_map[list1[i]] = i
    return []


def subarray_sum(list1, target):
    hash_map = {}
    current_sum = 0
    
    for i in range(len(list1)):
        current_sum += list1[i]
        
        if current_sum == target:
            return [0, i]
        
        if (current_sum - target) in hash_map:
            return [hash_map[current_sum - target] + 1, i]
        
        hash_map[current_sum] = i

    return []
            

# nums = [1, 2, 4, 4, 5]
# target = 9
# print ( subarray_sum(nums, target) )

# nums = [-1, 2, 3, -4, 5]
# target = 0
# print ( subarray_sum(nums, target) )

# nums = [2, 3, 4, 5, 6]
# target = 3
# print ( subarray_sum(nums, target) )

# nums = []
# target = 0
# print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""




def longest_consecutive_sequence(list1):
    if len(list1) < 2:
        return len(list1)
    
    temp = sorted(set(list1))
    longest_seq = []
    current_seq = [temp[0]]
    for i in range(1, len(temp)):
        # if i == 0:
        #     current_seq.append(temp[i])
        #     continue
        
        if temp[i] - temp[i-1] == 1:
            current_seq.append(temp[i])
        else:
            longest_seq = current_seq if current_seq and len(current_seq) > len(longest_seq) else longest_seq
            current_seq = [temp[i]]

    longest_seq = current_seq if current_seq and len(current_seq) > len(longest_seq) else longest_seq 
            
    return len(longest_seq)
        


print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""