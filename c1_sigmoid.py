"""
C1. Sigmoid function and its derivative.

sigma(x)  = 1 / (1 + exp(-x))
sigma'(x) = sigma(x) * (1 - sigma(x))   <- this identity is worth memorizing,
                                            it's why sigmoid is so convenient in ML
"""
import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)


x = np.linspace(-5, 5, 500)

plt.figure(figsize=(7, 5))
plt.plot(x, sigmoid(x), label=r"$\sigma(x)$")
plt.plot(x, sigmoid_derivative(x), label=r"$\sigma'(x)$")
plt.axhline(0, color="gray", linewidth=0.5)
plt.axvline(0, color="gray", linewidth=0.5)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sigmoid and its derivative")
plt.legend()
plt.tight_layout()
plt.savefig("c1_sigmoid.png", dpi=150)
plt.show()
