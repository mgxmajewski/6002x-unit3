import random
import pylab


def get_mean_and_std(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**2
    return mean, std


L = [1, 1, 1, 1, 2]
pylab.hist(L)
pylab.show()
factor = pylab.array(len(L)*[1])/len(L)
print(factor)
pylab.figure()
pylab.hist(L, weights=factor)
pylab.show()


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


mean, std = plot_means(1, 1000000, 19, '1 die', 'b', '*')
print('Mean of rolling 1 die =', str(mean) + ',', 'Std =', std)
mean, std = plot_means(50, 1000000, 19, '50 dice', 'r', '//')
print('Mean of rolling 50 die =', str(mean) + ',', 'Std =', std)
pylab.title('Rolling Continuous Dice')
pylab.xlabel('Value')
pylab.ylabel('Profitability')
pylab.legend()
pylab.show()