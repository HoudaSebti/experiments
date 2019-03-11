from scipy.stats import norm
import numpy as np

def compute_wiener_process(W_0, dt, size):
    W = [W_0]
    for t in range(1, size):
        W.append(W[-1] + norm.rvs(scale = dt))
    return W

def compute_geometric_brownian_motion(S_0, mu, sigma, W_0, size):
    S = [S_0]
    W = compute_wiener_process(W_0, 1, size)
    for t in range(1, size):
        S.append(S_0 * np.exp((mu - sigma**2 / 2)* t + sigma * W[t]))
        print(S[-1])
    return 0

def plot_geometric_brownian_motion():
    return 0

def main():
    compute_geometric_brownian_motion(0.0, .5, .01, 0.0, 30)

if __name__ == "__main__":
    main()
