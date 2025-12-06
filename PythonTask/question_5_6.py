##### question number 5_ 6
valid = []
with open("sales.txt") as file:
    for line in file:
        try:
            val = int(line)
            valid.append(val)

        except ValueError:
            print(f"{line} is Invalid type of data ")
    
print(" *** total sales is ",sum(valid))