# Import modules.
import time
import math


# We are going to numerically integrate to find something.

dx = 0.001
x = 0
int_x = 0

# Print value of time
t0 = time.time()
t = time.time()-t0
print(t)

#time.sleep(10)

while x<=2: # or for i in range(0, 2, dx)

    f_x = math.cos(x)
    # Euler integration
    int_x = int_x + dx*f_x

    print(int_x)

    # increment x
    x = x + dx

t2 = time.time() - t0
dt = t2-t
print(f'loop time = {dt}')

    # Write your code here :-)
