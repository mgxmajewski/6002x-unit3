import random
import pylab


def get_mean_and_std(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**2
    return mean, std


def plot_means(num_dice, num_rolls, num_bins, legend, color, style):
    means = []
    for i in range(num_rolls // num_dice):
        vals = 0
        for j in range(num_dice):
            vals += 5 * random.random()
        means.append(vals / float(num_dice))
    pylab.hist(means, num_bins, color=color, label=legend,
               weights=pylab.array(len(means) * [1]) / len(means),
               hatch=style)
    return get_mean_and_std(means)