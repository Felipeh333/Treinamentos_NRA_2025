import numpy as np

# x = np.random.randint(0,9,3)
# y = np.random.randint(0,9,3)
# z = np.random.randint(0,9,3)

# a = np.array([x,y,z])

a = np.random.randint(0,9,9).reshape(3,3)
b = np.random.randint(0,9,9).reshape(3,3)

print(f"Matriz A:\n{a}\n")
print(f"Matriz B:\n{b}\n")

c = a + b
print(f"Matriz C:\n{c}\n")

d = a*b
print(f"Matriz D:\n{d}\n")

e = a @ b
print(f"Matriz E:\n{e}\n")

