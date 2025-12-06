###### Question number 9

nums = [3,2,4]
target = 6

def target_sum(arr, t):

    # for i in range(len(arr)):
    #     for j in range(len(arr)):
    #         if i != j and arr[i] + arr[j] == t:
    #             return [i, j]

    values = {}

    for i, num in enumerate(arr):
        o_half = t - num

        if o_half in values:
            return [values[o_half], i]
        
        values[num] = i
            
print(target_sum(nums, target))

##### question number 10

num = 121

def palindrome(n):
    if n < 0:
        return False
    else:
        c = str(n)
        if c == c[::-1]:
            return True
        else:
            return False
        
print(palindrome(num))