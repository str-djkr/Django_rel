import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))


# import numpy as np

# def f(t, x, y):
#     return t / y

# def g(t, x, y):
#     return -t / y

# def runge_kutta_2_1_step(t, x, y, h):
#     T1 = f(t, x, y)
#     N1 = g(t, x, y)
#     T2 = f(t - h, x - h * T1, y - h * T1)
#     N2 = g(t - h, x - h * N1, y - h * N1)
    
#     x_new = x + (h / 2) * (T2 * (T1 + T2))
#     y_new = y + (h / 2) * (N2 * (N1 + N2))
    
#     return x_new, y_new

# def nystrom_3rd_order(x0, y0, h, k0):
#     x = [x0] * 3
#     y = [y0] * 3
    
#     for n in range(2, k0 + 2):
#         x_n1 = x[n] + (h / 3) * (7 * f(n, x[n], y[n]) - 2 * f(n - 1, x[n - 1], y[n - 1]) + f(n - 2, x[n - 2], y[n - 2]))
#         y_n1 = y[n] + (h / 3) * (7 * g(n, x[n], y[n]) - 2 * g(n - 1, x[n - 1], y[n - 1]) + g(n - 2, x[n - 2], y[n - 2]))
        
#         x.append(x_n1)
#         y.append(y_n1)
        
#     return x, y

# def solve_system(epsilon, h0, k0):
#     x0, y0 = 1.0, 1.0
#     t = 0
#     h = h0
#     k = 0
    
#     while k < k0:
#         x_h, y_h = nystrom_3rd_order(x0, y0, h, 2)
#         x_half, y_half = runge_kutta_2_1_step(t, x0, y0, h)
        
#         # Calculate the error
#         error_x = abs(x_h[2] - x_half)
#         error_y = abs(y_h[2] - y_half)
        
#         if error_x < epsilon and error_y < epsilon:
#             x0, y0 = x_h[2], y_h[2]
#             t += h
#             k += 1
#         else:
#             h /= 2  # Reduce the step size
        
#     return x0, y0

# epsilon = 0.01
# h0 = 0.2
# k0 = 15

# x1, y1 = solve_system(epsilon, h0, k0)
# print(f"x(1) = {x1:.6f}, y(1) = {y1:.6f}")
