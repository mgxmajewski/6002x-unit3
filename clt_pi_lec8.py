import numpy
import random


def throw_needles_pi(num_needles):
    """
    :param num_needles: number of trials
    simulation that estimates the value of 2–√
    in a way described by Buffon-Laplace.
    """
    in_circle = 0
    for n in range(num_needles):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**0.5 <= 1.0:
            in_circle += 1
    return 4*(in_circle/float(num_needles))


def get_est(num_needles, num_trials):
    estimates = []
    for t in range(num_trials):
        pi_guess = throw_needles_pi(num_needles)
        estimates.append(pi_guess)
        std_dev = numpy.std(estimates)
    cur_est = sum(estimates)/len(estimates)
    print('Est. =' + str(cur_est) +
          ', Std.  dev. =' + str(round(std_dev, 6))
          + '. Needles = ' + str(num_needles))
    return cur_est, std_dev


def est_pi(precision, num_trials):
    num_needles = 1000
    std_dev = precision
    while std_dev >= precision/1.96:
        cur_est, std_dev = get_est(num_needles, num_trials)
        num_needles*=2
    return cur_est


random.seed(0)
est_pi(0.005, 100)





