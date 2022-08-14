import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from time import time
from random import randint
from main import *

iters = 10_000

gst = time()
get = None

for i in range(iters):
    print(f"Iteration {i}...", end="")
    st = time()
    curve = bezier(2, [[randint(0, 100), randint(0, 100)], [randint(0, 100), randint(0, 100)], [randint(0, 100), randint(0, 100)]])
    et = time()
    print(f"\rIteration {i}: {(et - st)}")

get = time()

print(f"Total time for {iters} iters: {(get - gst)}, Average: {(get - gst) / iters}")