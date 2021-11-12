import os.path
import random


f = open("test.txt", "w")
while os.path.getsize("test.txt") < 50 * 1024 * 1024:
    f.write(str(random.randint(0, 1000)) + '\n')
f.close()
