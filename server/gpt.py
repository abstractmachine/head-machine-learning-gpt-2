# import this gpt library by Max Woolf: https://github.com/minimaxir/gpt-2-simple
# pip install gpt_2_simple
import gpt_2_simple as gpt2

# import Google's TensorFlow python library
# import tensorflow
import tensorflow as tf

sess = gpt2.start_tf_sess(threads=1)
gpt2.load_gpt2(sess)

print("Ready")

while True:

	prompt = input()

	text = gpt2.generate(sess,
						 length=256,
						 temperature=0.7,
						 top_k=0,
						 top_p=0,
						 prefix=prompt,
						 truncate=None,
						 include_prefix='true',
						 return_as_list=True
						 )[0]

	print(text)

sess.close()


# configuration macOS M1 Max :

# pyenv install 3.9.1
# pyenv global 3.9.1

# hack to get tensorflow installed on m1 mac:
# brew install hdf5
# export HDF5_DIR=/opt/homebrew/Cellar/hdf5/1.12.0_4
# pip install --no-binary=h5py h5py
# python3 -m pip install tensorflow-macos
