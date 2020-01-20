import multiprocessing as mp
import random
import string

random.seed(123)

def cube(x):
    return x**3


# The Pool.map and Pool.apply will lock the main program until all processes are finished,
# which is quite useful if we want to obtain results in a particular order for certain applications.


pool = mp.Pool(processes=4)
results = [pool.apply(cube, args=(x,)) for x in range(1,7)]
print(results)

pool = mp.Pool(processes=4)
results = pool.map(cube, range(1,7))
print(results)

# The async variants will submit all processes at once and retrieve the
# results as soon as they are finished. One more difference is that
# we need to use the get method after the apply_async() call in order to
# obtain the return values of the finished processes.
pool = mp.Pool(processes=4)
results = [pool.apply_async(cube, args=(x,)) for x in range(1,7)]
output = [p.get() for p in results]
print(output)