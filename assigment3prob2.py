import numpy as np

random_vector = np.random.uniform(1,20,20)
reshaped_array = random_vector.reshape(4,5)
max_indices = np.argmax(reshaped_array,axis=1)

for  row_idx, max_idx in enumerate(max_indices):
    reshaped_array[row_idx, max_idx] =0

print("random vector")
print(random_vector)

print("\n reshaped vector (4x5)")
print(reshaped_array)
