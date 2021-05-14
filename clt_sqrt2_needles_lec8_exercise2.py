import random


def throw_needles(num_needles):
    """:param num_needles: number of trials
    simulation that estimates the value of 2–√
    in a way similar to the Buffon-Laplace
    Pi estimation shown in lecture.
    A flat line ranging from 0 to root 2
    and with a subsection that spans from 0 to 1.
    """
    success = 0
    for n in range(num_needles):
        x = random.random()
        if (1+x)**2 < 2.0:
            success += 1
    sqrt2 = 1+(float(success) / num_needles)
    return sqrt2


print(throw_needles(10000000))
