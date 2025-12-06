##### question number 14

scores = {"John": 85, "Sara": 92, "Fraol": 78}

try:
    name = input("Enter student name ")
    print(scores[name])
except Exception:
    print("Student not found! ")


###### question number 15

from collections import Counter
sentence = input("Enter sentence ")
words = sentence.split(" ")

freq = Counter(words)

print(freq)

###### question number 16

from collections import defaultdict
grades =  {"John": "A", "Sara": "B", "Musa": "A"}
rev = defaultdict(list)
for key, value in grades.items():
    rev[value].append(key) 

print(rev)
