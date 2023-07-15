# SCALARS IN TENSOR FLOW
# Tensors created with a weapper
# tf.Variable
# tf.constant
# tf.placeholder
# tf.SparseTensor

# Most widely-used is tf.Variable, which we'll use here

# As with TF tensors, in PyTorch we can similarly perform operations, and we can easily convert to and from NumPy arrays

# Also, a full list of tensor data types is available here.


import tensorflow as tf

print("- Creating a basic int scalar")
x_tf = tf.Variable(25,dtype=tf.int16)
print(x_tf)
print("")

print("- Verify its current shape")
x_tf.shape
print(x_tf)
print("")

print("- Adding scalars")
y_tf = tf.Variable(3, dtype=tf.int16)
print(x_tf+y_tf)
print("")

print("- Printing current type")
tf_sum = tf.add(x_tf, y_tf)
print(type(tf_sum.numpy()))
print("")

print("- Creating a scalar with float typed value")
tf_float = tf.Variable(25., dtype=tf.float16)
print(tf_float)
print("")
