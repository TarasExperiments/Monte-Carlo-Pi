"""Estimates the value of pi using the Monte Carlo method."""


import numpy as np
import matplotlib.pyplot as plt


def estimate_pi(num_samples):
    # Generate random points in the square
    x = np.random.uniform(0, 1, num_samples)
    y = np.random.uniform(0, 1, num_samples)

    # Calculate the squared distance from the origin
    distances_squared = x**2 + y**2

    # Count how many points fall inside the circle
    inside_circle = np.sum(distances_squared <= 1)

    # Estimate pi using the ratio of points inside the circle to total points
    pi_estimate = (inside_circle / num_samples) * 4
    return pi_estimate


def graph_estimation_trend(num_samples_list):
    # Loop through different sample sizes and estimate pi
    pi_estimates = [estimate_pi(n) for n in num_samples_list]

    # Plotting the results
    plt.plot(num_samples_list, pi_estimates,)
    plt.axhline(y=np.pi, color='r', linestyle='--', label='Actual π')
    plt.xscale('log')
    plt.xlabel('Number of Samples')
    plt.ylabel('Estimated π Value')
    plt.title('Estimation of π using Monte Carlo Method')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Create a list of sample sizes to test
    num_samples_list = np.logspace(1, 7, num=50, dtype=int).tolist()

    # Plot the estimation trend
    graph_estimation_trend(num_samples_list)