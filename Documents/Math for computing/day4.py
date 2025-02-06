import math

def g(x, alpha):
    return alpha * (x**2 - 2*x) + x  

def fixed_point_iteration(g, x0, alpha, epsilon=0.05, max_iter=100):
    x = x0
    iterations = 0
    while iterations < max_iter:
        x_new = g(x, alpha)
        iterations += 1
        if abs(x_new - x) < epsilon: 
            break
        x = x_new
    return x, iterations


# Initial guess
x0 = 1
alpha = -1/6 

# Run iteration
root, num_iterations = fixed_point_iteration(g, x0, alpha)

print(f"Approximate root: {root}")
print(f"Iterations required: {num_iterations}")
