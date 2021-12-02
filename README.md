# head-machine-learning-gpt-2
A tutorial checklist for installing, training, and using gpt-2

## History
What is it?

- What is a Text Transformer

## First Contact
(Talking with a GPT-2 bot online)
- [](https://app.inferkit.com/demo)

## Re-train GPT In Your Own Style
GPT-2 is trained with a general dataset of knowledge and human conversations. This makes for boring converstaions. Let's teach it to speak in a specific style, manner, or syntax.

### Preparing Your Machine
- Download [Visual Studio Code](https://code.visualstudio.com) for your machine (Mac, PC, Linux)
- Open VS Code 
- Open the "Extensions" Tab and verify that the Extension [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) is installed
- Create a folder for your project and open the folder in VS Code.
- Create a filename titled `train.ipynb` in that folder
- This should open the Jupyter input interface. For example you should see new buttons titled `+Code`, `+Markdown`, `>Run All`
- This interface is now ready to receive Python commands (see below). Each command is entered step by step into your Jupyter interface. Results at the end of each command will be displayed directly in this window, following which you can enter the next command.

### Preparing Your Dataset
- Text sources (sorry, English only for now)
- Guttenberg (teach your bot to speak like Virginia Woolf)
- Clean up your text
- Pattern matching
- Experment mode: Learn Regex 

### Train Your Bot
- At this time, begin to create a new code block.
- The first bloc of code is :

```
	!pip install -q gpt-2-simple
	import gpt_2_simple as gpt2
	from datetime import datetime
```

it's means that you check if the library gpt-2-simple is installed in your system, and we need to `import gpt_2_simple`and `datetime` library. 
- Now you can press Play, to execute this part of code. (it take a little bit of time...)
- Now we will check the state of the graphic card, it can be usefull if you have a strong graphic card.
```
!nvidia-smi
```
- Press Play to see the result.
- After that we will downlad the smallest model of GPT2.
```
gpt2.download_gpt2(model_name="124M")
```
- Press Play again and also wait that the model download to your computer.
- 



## Talking To Your Bot
Now that we have trained our bot with its own style, let's starting talking to it.

### Command Line Prompt
(direct communication with the bot on the command line)

### Simple API Communication
(create a quick server in Python, speak to it from a webpage)

Different ways of speaking to your bot.
- Webpage
- Processing
- P5
- Unity
- Twine
- Godot
- Max/MSP

## Attributuion
This tutorial repackages [Max Woolf](https://minimaxir.com)'s [Train a GPT-2 Text-Generating Model w/ GPU]() Google Colab notebook and their [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple) training code.

## Online Tutorials
- [GPT-2 Neural Network Poetry](https://www.gwern.net/GPT-2)
- [How To Make Custom AI-Generated Text With GPT-2](https://minimaxir.com/2019/09/howto-gpt2/)
- [How to Build a Twitter Text-Generating AI Bot With GPT-2](https://minimaxir.com/2020/01/twitter-gpt2-bot/)

## Context
This tutorial was created by the [Pool Numérique](https://www.hesge.ch/head/formations-recherche/pool-numerique) and the [Master Media Design](https://www.hesge.ch/head/formations-recherche/master-en-media-design) ([HEAD–Genève](https://www.hesge.ch/head)), for the Virtual Beings semester project (2021-22).
