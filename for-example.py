# Demonstrate a for loop

import time
delay = 0.5
for num in range(10,0,-1):
    print(num)
    time.sleep(delay)
print("Blast off")