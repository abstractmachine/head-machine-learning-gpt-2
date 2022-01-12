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


### Python Libraries

```
$ python3 -m pip install gpt_2_simple
$ python3 -m pip install tensorflow
```

