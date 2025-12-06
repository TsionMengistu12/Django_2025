## creating a new file and writing on it
with open("Tsion.txt", "w") as file:
    file.write("hello, world")

# fName = input("please enter the file name you want to access ")

# if fName == "Tsion.txt":
#     with open("Tsion.txt", "r") as file:
#         con = file.read()
#     print(con)
# else:
#     with open("Guest.txt", "w") as file:
#         file.write("Welcome")

#     print("Welcome, ", file.name.split("."))

try:
    with open("text.txt") as file:
        content = file.read()
    print(f"welcome", {content})

except Exception:
    with open("text.txt", "w") as file:
        file.write("Guest")
    name = file.name.split(".")
    print(f"welcome", name[0] )

