# Talking To Robots

## Translation
Il y a une version française de ce tutoriel : [Parler aux robots](LISEZMOI.md).

## What Is This?
This document is a tutorial/checklist for installing, training, and using [GPT-2](https://en.wikipedia.org/wiki/GPT-2).

## History
We are going to be generating text with a bot. The field of computer science that figures out how to teach computers to interpret and generate text is [Natural Language Processing](https://en.wikipedia.org/). Natural Language Processing dates from the earliest reserach in computer science and many of the earliest theoretical texts from the very beginnings — cf. [Computing Machinery and Intelligence](https://en.wikipedia.org/wiki/Computing_Machinery_and_Intelligence) — are related to teaching computers to understand human languge and use it to communicate with us.

### Historical Approaches to Text Generation
Given this long history, there are many different historical methods used to generate text with a computer. An excellent overview of the most important techniques can be helpful when making art and design projects that generate text. Sometimes, for example, a neural network is overkill and a simpler, or more straightforward approach would be more helpful.

An excellent overview of the history of “generative” artworks and the various techniques used to build them is [Philippe Pasquier](https://philippepasquier.com)’s online course [Generative Art and Computational Creativity](https://www.kadenze.com/programs/generative-art-and-computational-creativity).

Another important tool used for text generation is [Daniel Howe]()’s [RiTa](https://rednoise.org/rita/) library which includes tutorials and examples for integrating this library into a [P5](https://p5js.org) or [Processing](https://processing.org) project. It makes significant use of [markov chains](https://en.wikipedia.org/wiki/Markov_chain) to generating text: cf. [Tutorial: Generating with RiTa n-grams](https://observablehq.com/@dhowe/tut-rita-ngrams). RiTa is often a good starting point when learning to make generative works of art.

### Transformers
The type of text transformer we will be using for this tutorial is called « GPT », which stands for « Generative Pre-trained Transformer ». « Generative » means, as the name might suggest, that the computer will be generating text output for us. « Pre-trained » describes how previously captured text will be use to create a previously-trained model that we will then modify to generate a new text in the style we want. And finally, « transformer » describes the neural network algorithm itself that is used to make all this possible.

Dale Markowitz has a really good video from August 2021 describing briefly what a transformer “is”. It is probably your best starting point: [](https://youtu.be/SZorAJ4I-sA)

The original paper that invented this approach is probably hard to read for most people reading this tutorial, but here it is if you are curious: [Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf) (December 2017). This paper was a collaboration between Google (and more specifically, Google Brain) and the University of Toronto, i.e. the place where [Geoffrey Hinton](https://en.wikipedia.org/wiki/Geoffrey_Hinton) teaches and does research. If you want a data science analysis of why this work was important, and why it replaced the techniques that came before it, here is a somewhat more digestible presentation on its importance: [LSTM is dead. Long Live Transformers!](https://youtu.be/S27pHKBEp30).

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

The above code checks to see if the `gpt-2-simple` library is installed in your system. We also need to `import` the `gpt_2_simple`and `datetime` libraries. 

Now you can press Play, to execute this part of code. (It will take a little bit of time...)
 
Now we will check the state of the graphic card, it can be usefull if you have a strong graphic card.

```
!nvidia-smi
```

Press Play to see the result.
After that we will downlad the smallest model of GPT2:

```
gpt2.download_gpt2(model_name="124M")
```

Press Play again and also wait that the model download to your computer.

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
