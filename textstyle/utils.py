import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt


class Statistics:

    @classmethod
    def mean_std(cls, data, axis=None):
        data = np.asarray(data)

        return np.mean(data, axis=axis), np.std(data, axis=axis)

    @classmethod
    def mean(cls, data, axis=None):
        data = np.asarray(data)

        return np.mean(data, axis=axis)

    @classmethod
    def std(cls, data, axis=None):
        data = np.asarray(data)

        return np.std(data, axis=axis)

    @classmethod
    def ecdf(cls, data):
        n = len(data)

        x = np.sort(data)

        y = np.arange(1, n + 1) / n

        return x, y

    @classmethod
    def generate_theoritical_gauss(cls, data, size=1000):
        mean, std = np.mean(data), np.std(data)

        theor_samples = np.random.normal(mean, std, size=size)

        return theor_samples


class Plot:

    @classmethod
    def ecdf(cls, x, y, x_label=None, y_label=None, show=False):
        plt.plot(x, y, marker='.', linestyle='none')

        if show:
            plt.xlabel(x_label)
            plt.ylabel(y_label)

            plt.show()

    @classmethod
    def histogram(cls, x, bins=None, x_label=None, y_label=None, label=None, show=False):
        plt.hist(x, color=np.random.rand(3, ), alpha=0.5, bins=bins, label=label)

        if show:
            plt.xlabel(x_label)
            plt.ylabel(y_label)

            plt.show()

    @classmethod
    def dist_histogram(cls, x, x_label=None, y_label=None, show=False):
        sb.distplot(x)

        if show:
            plt.xlabel(x_label)
            plt.ylabel(y_label)

            plt.show()

    @classmethod
    def plot(cls, x_label=None, y_label=None):
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        plt.legend(prop={'size': 10})

        plt.show()