# Webpage demo

## What is this?
This is a demo of a webpage that communicates with the GPT-2 [server.py](../server/server.py).

## Setup Python
You will need Python installed on your machine. We have tested this server with Python 3.9.x.

### pyenv
On a Mac, you can use [brew](https://brew.sh) to install Python. It is recommended on macOS to install `pyenv` first, which will allow you to have several versions of Python for whatever project and version needs it.

To install `pyenv`, go into your `Terminal` and type:

```
$ brew install pyenv
```

When `pyenv` has finished installing you can test which verisons of `Python` are installed on your machine.

```
$ pyenv versions
  system
  3.10.0
* 3.9.1 (set by /Users/YourUserName/.pyenv/version)
```
### Python
  
Once you can installed `pyenv` you can easily install whatever version you want.

If you want to see the full list of Python distributions :

```
$ pyenv install --list
```

### Install pip (if you don't have pip installed)
```
$ sudo apt install pip
```

### Python Libraries

```
$ python3 -m pip install gpt_2_simple
$ python3 -m pip install tensorflow
```

## Start/Test the server

At this time, you can start the server with the command :

```
$ python3 test.py
```
Now you can ask the server when you enter commend line. Usually, it take around 10/20 seconds to the server respond a answer.

## Make fast answer with the GPU acceleration on linux (nvidia card with cuda)  

When you start `test.py`, your have probally a kind of `Could not load dynamic library 'libcudnn.so.8';` error.

### Step 1 : Install the last driver of your graphic card

Link installation on the nvidia website to download the last nvidia tool kit :

In our case, we choose, Linux > x86_64 > Ubuntu > 20.04 > deb(local)

https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=20.04&target_type=deb_local

```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
  
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
  
wget https://developer.download.nvidia.com/compute/cuda/11.5.1/local_installers/cuda-repo-ubuntu2004-11-5-local_11.5.1-495.29.05-1_amd64.deb
  
sudo dpkg -i cuda-repo-ubuntu2004-11-5-local_11.5.1-495.29.05-1_amd64.deb
  
sudo apt-key add /var/cuda-repo-ubuntu2004-11-5-local/7fa2af80.pub
  
sudo apt-get update
  
sudo apt-get -y install cuda
```

### Step 2 :

If you get an error, probably you need the libcudnn8 libray:

This is the adress of all version of the libray :  
https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/

We choose this (but an other version probally work) :  

libcudnn8_8.0.5.39-1+cuda11.1_amd64.deb
https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/libcudnn8_8.0.5.39-1+cuda11.1_amd64.deb

Now install the libray with double clicking on the .deb file.

## you can make this with the command line :  
```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/libcudnn8_8.0.5.39-1+cuda11.1_amd64.deb
  
sudo dpkg -i libcudnn8_8.0.5.39-1+cuda11.1_amd64.deb
```
### Check if the GPU is available :

If everything worked you need to have 1 (or more :-) ) after the line `Number of GPU`.

```
python3 testGPU.py
```







