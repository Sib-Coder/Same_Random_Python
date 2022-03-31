import random
import string
file = open("test.txt", "w")
for i in range(1, 10):
    file.write(f"user{i}:"+(''.join(random.choices(string.ascii_letters+string.digits, k=6)))+"\n")
file.close()