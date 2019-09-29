from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


def compute_wiener_process(W_0, dt, number_dates):
    W = np.zeros(number_dates);
    W[0] = W_0
    for t in range(1, number_dates):
        W[t] = W[t - 1] + norm.rvs(loc = 0, scale = np.sqrt(dt / 365.0))
    
    return W

def compute_geometric_brownian_motion(S_0, mu, sigma, W_0, number_dates):
    W = compute_wiener_process(W_0, 1, number_dates)
    S = np.zeros(number_dates);
    S[0] = S_0
    for t in range(1, number_dates):
        S[t] = S_0 * np.exp((mu - (sigma ** 2) / 2)* t / 365.0 + sigma * W[t])
    
    return S


def plot_geometric_brownian_motions(brownian_motions, ylabels):
    t = list(range(len(brownian_motions[0])))
    fig, ax = plt.subplots()
    for k in range(len(brownian_motions)):
        ax.plot(t, brownian_motions[k], label=ylabels[k])
        plt.legend(loc='best')
    ax.set(title=r'Brownian_motion$(t)$',
    xlabel='$t$',
    ylabel='Brownian_motion')
    plt.show()

def main():
    S_0 = 100.0
    W_0 = 0.0
    number_dates = 1000   
    number_scenarii = 3

    scenarii = np.zeros((number_scenarii, number_dates))
    ylabels = ["" for x in range(number_scenarii)]
    
    scenarii[0] = compute_geometric_brownian_motion(S_0, .15, .2, W_0, number_dates)
    ylabels [0] = r'$\mu > \sigma^2 /2$'
    
    scenarii[1] = compute_geometric_brownian_motion(S_0, .01, .2, W_0, number_dates)
    ylabels [1] = r'$\mu < \sigma^2 /2$'
    
    scenarii[2] = compute_geometric_brownian_motion(S_0, .02, .2, W_0, number_dates)
    ylabels [2] = r'$\mu = \sigma^2 /2$'

    plot_geometric_brownian_motions(scenarii, ylabels)

if __name__ == "__main__":
    main()
