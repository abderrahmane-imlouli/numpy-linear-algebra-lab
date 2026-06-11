import numpy as np

print("=========== PART I - NUMPY ===========")

# ---------- Task 1 ----------
print("\n--- Task 1 ---")

# 1D Array from 5 to 25
arr1 = np.arange(5, 26)

# 3x3 Matrix from 1 to 9
arr2 = np.arange(1, 10).reshape(3, 3)

print("1D Array:", arr1)
print("ndim:", arr1.ndim)
print("shape:", arr1.shape)
print("size:", arr1.size)

print("\n3x3 Matrix:\n", arr2)
print("ndim:", arr2.ndim)
print("shape:", arr2.shape)
print("size:", arr2.size)


# ---------- Task 2 ----------
print("\n--- Task 2 ---")

arr = np.arange(12)
mat = arr.reshape(3,4)

print("3x4 Matrix:\n", mat)

# Extract
print("Last Row:", mat[-1])
print("First Column:", mat[:, 0])
print("Element (1,2):", mat[1,2])

# Boolean mask
print("Numbers > 5:", mat[mat > 5])


print("\n=========== PART II – FUNCTIONS ===========")

# ---------- Task 4 ----------
print("\n--- Task 4 ---")

def stats(arr):
    return arr.min(), arr.max(), arr.mean()

mn, mx, avg = stats(mat)
print("Min:", mn)
print("Max:", mx)
print("Mean:", avg)


# ---------- Task 5 ----------
print("\n--- Task 5 ---")

def safe_reshape(arr, new_shape):
    try:
        return arr.reshape(new_shape)
    except:
        return None

print("Reshape (3,4):\n", safe_reshape(arr, (3,4)))
print("Reshape (4,3):\n", safe_reshape(arr, (4,3)))
print("Reshape (5,5):", safe_reshape(arr, (5,5)))


# ---------- Task 6 ----------
print("\n--- Task 6 ---")

def normalize(arr):
    return (arr - arr.min()) / (arr.max() - arr.min())

random_matrix = np.random.randint(0, 50, (4,4))

print("Random Matrix:\n", random_matrix)
print("Normalized:\n", normalize(random_matrix))


print("\n=========== PART III – LINEAR ALGEBRA ===========")

# ---------- Task 7 ----------
print("\n--- Task 7 ---")

def mat_operations(A):
    print("Matrix A:\n", A)

    print("\nTranspose:\n", A.T)

    det = np.linalg.det(A)
    print("\nDeterminant:", det)

    if det != 0:
        print("\nInverse:\n", np.linalg.inv(A))
    else:
        print("\nMatrix is not invertible")


# Test
A = np.array([[4,7],
              [2,6]])

mat_operations(A)
