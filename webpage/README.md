# Webpage demo

## What is this?
This is a demo of a webpage that communicates with the GPT-2 [server.py](../server/server.py).

## PHP server
Many macOS machines have a server already built-in. To run this server open your Terminal and go into the `webpage` folder:

```
$ cd head-machine-learning-gpt-2/webpage
```

Once you are in the webpage folder, start your php server:

```
$ php -S localhost:8080
```

## Node Server
If you do not have PHP installed, and you do not want to install it, you can instead install a Node server to run your webpage

```
$ brew install node
```

Once node has been installed, you can open your Terminal and go into the `webpage` folder:

```
$ http-server
```