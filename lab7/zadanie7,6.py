import itertools
import random

iter_zeroone= itertools.cycle('01')
dir = ["N", "E", "S", "W"]
rand_dir = (random.choice(dir) for _ in itertools.repeat(None))

dni = itertools.cycle(range(7))

for i in range(10):
    print(next(iter_zeroone), next(rand_dir), next(dni))