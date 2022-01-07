import numpy as np
import matplotlib.pyplot as plt

def plot_learning_curve(scores, x, figure_file):
    running_average = np.zeros(len(scores))
    for i in range(len(running_average)):
        running_average[i] = np.mean(scores[max(0, i-100):(i+1)])
    plt.plot(x, running_average)
    plt.title('Running average over previous 100 scores')
    plt.savefig(figure_file)