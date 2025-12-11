###### question number 7

num = 15

def fizzbuzz(n):
    ans = []

    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0 :
            ans.append("FizzBuzz")
        elif i % 5 == 0:
            ans.append("Buzz")
        elif i % 3 == 0:
            ans.append("Fizz")                                                                                                                                          
        else:
            ans.append(str(i))
    return ans

print(fizzbuzz(num))

###### question number 8

nums = [0,1,0,3,12]
def move_zeros(arr):
    l = 0
    r = 0
    while r < len(arr):
        if arr[l] == 0 and arr[r] != 0:
            arr[l], arr[r] = arr[r], arr[l]

        elif arr[l] == 0 and arr[r] == 0:
            r += 1
            
        elif arr[l] != 0 and arr[r] != 0 or arr[l] != 0 and arr[r] == 0:
            l += 1
            r += 1
    return arr

print(move_zeros(nums))



