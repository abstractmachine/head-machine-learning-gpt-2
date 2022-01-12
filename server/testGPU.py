import tensorflow as tf

print("--------------------------------")
print("Number of GPU")
print("--------------------------------")
print(len(tf.config.list_physical_devices('GPU')))
print("--------------------------------")
print("details : ")
print("--------------------------------")
print(tf.config.list_physical_devices('GPU'))