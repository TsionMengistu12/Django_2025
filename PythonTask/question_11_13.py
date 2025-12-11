##### question number 11

num = 8
def sqrt(n):
    x = n
    for _ in range(20):
        x = 0.5 * (x + n / x)
    return int(x)

print(sqrt(num))

##### question number 13

try:
    with open("log.txt") as file:
        con = file.read()
except FileNotFoundError:
    print("File is not found")

print(con.upper())

