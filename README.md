# Talking To Robots

## Translation
Il y a une version française de ce tutoriel : [Parler aux robots](LISEZMOI.md).

## What Is This?
This document is a tutorial/checklist for installing, training, and using [GPT-2](https://en.wikipedia.org/wiki/GPT-2).

## History
We are going to be generating text with a bot. The field of computer science that figures out how to teach computers to interpret and generate text is [Natural Language Processing](https://en.wikipedia.org/). Natural Language Processing dates from the earliest reserach in computer science and many of the earliest theoretical texts from the very beginnings — cf. [Computing Machinery and Intelligence](https://en.wikipedia.org/wiki/Computing_Machinery_and_Intelligence) — are related to teaching computers to understand human languge and use it to communicate with us.

### Historical Approaches to Text Generation
Given this long history, there are many different historical methods used to generate text with a computer. An overview of the most important techniques can be helpful when making art and design projects that generate text. Sometimes, for example, a neural network is overkill and a simpler, or more straightforward approach would be more helpful.

An excellent overview of the history of “generative” artworks and the various techniques used to build them is [Philippe Pasquier](https://philippepasquier.com)’s online course [Generative Art and Computational Creativity](https://www.kadenze.com/programs/generative-art-and-computational-creativity).

Another important tool used for text generation is [Daniel Howe]()’s [RiTa](https://rednoise.org/rita/) library which includes tutorials and examples for integrating this library into a [P5](https://p5js.org) or [Processing](https://processing.org) project. It makes significant use of [markov chains](https://en.wikipedia.org/wiki/Markov_chain) to generating text: cf. [Tutorial: Generating with RiTa n-grams](https://observablehq.com/@dhowe/tut-rita-ngrams). RiTa is often a good starting point when learning to make generative works of art.

### Transformers
The type of text transformer we will be using for this tutorial is called « GPT », which stands for « Generative Pre-trained Transformer ». « Generative » means, as the name might suggest, that the computer will be generating text output for us. « Pre-trained » describes how previously captured text will be use to create a previously-trained model that we will then modify to generate a new text in the style we want. And finally, « transformer » describes the neural network algorithm itself that is used to make all this possible.

Dale Markowitz has a really good video from August 2021 describing briefly what a transformer “is”. It is probably your best starting point: [Transformers, explained: Understand the model behind GPT, BERT, and T5](https://youtu.be/SZorAJ4I-sA)

The original paper that invented this approach is probably hard to read for most people reading this tutorial, but here it is if you are curious: [Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf) (December 2017). This paper was a collaboration between Google (and more specifically, Google Brain) and the University of Toronto, i.e. the place where [Geoffrey Hinton](https://en.wikipedia.org/wiki/Geoffrey_Hinton) teaches and does research. If you want a data science analysis of why this work was important, and why it replaced the techniques that came before it, here is a somewhat more digestible presentation on its importance: [LSTM is dead. Long Live Transformers!](https://youtu.be/S27pHKBEp30).

## First Contact
Let's talk to some oneline bots written with GPT-2.

- [Talk To Transformer](https://talktotransformer.com)
- [Write With Transformer](https://transformer.huggingface.co)
- [Infer Kit Demo](https://app.inferkit.com/demo)

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
Probably the most important part of retraining is preparing the dataset — well before the actual neural network training itself. This is a process that more ressembles the art of curation, and less that of writing. I.e. you will mostly avoid writing new material during this phase, especially given the massive *amount* of text that you will need to feed to GPT in order to make it compelling and — textually speaking — *diverse*. A very short text file won't work for training GPT in any significant way. Therefore it is simply impractical in most cases to write the text yourself. Instead you will need to find a collection of texts that adhere in their diversity to the style of whatever it is you are trying to create stylistically, or in terms of personality.

For example, in [Simon Senn](http://www.simonsenn.com)'s and [Tammara Leites](https://issue-journal.ch/author/tammara-leites-en/)' performance [dSimon](https://www.liberation.fr/culture/scenes/la-premiere-intelligence-artificielle-sur-une-scene-de-theatre-repond-a-libe-alors-que-les-autres-donnent-lillusion-de-jouer-je-donne-lillusion-de-penser-20211122_DBVC5XT4JRAJJGZGLYB5ZMRJ6Q/), the duo used a huge collection of several years of Simon Senn's personal emails to train his GPT double. This created a disturbingly familiar, and yet consistently surreal, textual double that mimicked eerily Simon's own writings, musings, and interpersonnal communications — while simultaneously producing a lot of interresting absurd proclamations. For their result to work on a poetic level, this required thousands and thousands of lines of text, and not just a few emails selected here or there from Simon's epistolary life.

The type text you need to prepare is raw text — `.txt` format text — which simply means that the text has no extraneous fonts, formatting, color, size or even indications of bold or italic. It is just a collection of raw letters from A to Z, numbers, punctuation, and various accented characters. Special note: for now, we will be working entirely in *english*. Even though GPT is not technically limited to *english*, the original training was done in *english* and so will not simply tranfer easily over to another language during the retraining process. Perhaps you will have better luck than we did, but be forewarned.

There are many places where you can find raw blocks of text to source your training dataset. A good starting point is [Project Guttenberg](https://www.gutenberg.org), if for example you wish to teach your bot to speak like [Virginia Woolf](https://www.gutenberg.org/ebooks/author/89).

Texts found at Guttenberg and other sources online will contain a lot of extraneous legal disclaimers, punctuation, and other undesired textual noise that will enter into your training if you do not remove it. So once you have selected your text sources and copied it into a single `.txt` file, you will need to clean up your text.

We suggest using [VS Code](https://code.visualstudio.com) to edit your dataset. It has a simple 'find', 'replace', and 'replace all' function, much like many other text and code editors. For simple pattern matching cf. [VS Code, Basic Editing, Find and Replace](https://code.visualstudio.com/docs/editor/codebasics#_find-and-replace). Use this `find` + `replace all` method to clean out your giant block of text of all of the extraneous spaces and punctuation that you do not want to enter into GPT.

If you want to fall down a deep rabbit hole of text-wrangling awesomeness, this simple `find`/`replace` tool has a little button with a star that will activate a crazy-looking but sophisticated and powerful text “parsing” language called [Regular Expressions](https://en.wikipedia.org/wiki/Regular_expression). Regular Expressions are amazing, but also look like the unfortunate accident of some randpm computer error: it is famously very difficult to read. Thankfully, VS Code gives you some visual pointers on what your regular expressions will do to your text before you commit, and you will also found numerous tutorials online to teach you this nutso language:
	- [RegexOne: Learn Regular Expressions with simple, interactive exercises](https://regexone.com)
	- [Regex 101](https://regex101.com)
	- [RegexLearn](https://regexlearn.com/learn)

### Train Your Bot
Now that your text is ready for training, let us load it into our GPT pretrained network (the *P* of *GPT* stands for “pretrained”) and start retraining with it.

We will use the `Jupyter` environment of `VS Code` which should automatically activate whenever you open a text file ending in the `.ipynb` format.

Either create a new text file named `train.ipynb` or simply use the file provided with this document inside the `Jupyter` folder.

If you are writing your own text from scratch, you will need to clock on the `+Code` button in order to begin to create a new code block. This first bloc of code is :

```
!pip install -q gpt-2-simple
import gpt_2_simple as gpt2
from datetime import datetime
```

The above code checks to see if the `gpt-2-simple` library is installed in your system. We also need to `import` the `gpt_2_simple`and `datetime` libraries. 

Now you can press the button inside of the `[ ]` brackets, which will execute this part of code. It will take a little bit of time...

When this has finished executing, we try to accelerate the training process by testing if you have an Nvidia graphics card.

```
!nvidia-smi
```

Press Play to see the result. If you are on a Mac, there is little to no chances of this `nvifia` function activating anything.

After that we will downlad the smallest model of GPT2:

```
gpt2.download_gpt2(model_name="124M")
```

Press Play again and also wait for the model to download to your computer.

Now we will actually train GPT. First, we need to create a training session that we will place in a variable named `sess`. Then we need to tell GPT what the name of our text file will be. This file should be in the same folder as our `train.ipynb` file. Finally, we use this filename to start the training process, which needs some extra information for example the amount of training steps it will need to take, and how often to test out the state of its results.

```
sess = gpt2.start_tf_sess()
file_name = "shakespeare.txt"
gpt2.finetune(sess,
              dataset=file_name,
              model_name='124M',
              steps=1000,
              restore_from='fresh',
              run_name='run1',
              print_every=100,
              sample_every=200,
              save_every=500
              )
```

Depending on your computer this take several hours.

## Talking To Your Bot
Now that we have trained our bot with its own style, let's starting talking to it. To test it out yourself, use the `generate()` command:

```
gpt2.generate(sess)
```

We probably want more control over our output, and also to define a “prompt” which will be used to begin opening words and characters that GPT will attempt to continue:

```
gpt2.generate(sess,
              length=250,
              temperature=0.7,
              prefix="JULIET:",
              nsamples=1,
              batch_size=1
              )
```

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
This tutorial repackages [Max Woolf](https://minimaxir.com)'s [Train a GPT-2 Text-Generating Model w/ GPU](https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce) Google Colab notebook and their [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple) training code.

## Online Tutorials
- [GPT-2 Neural Network Poetry](https://www.gwern.net/GPT-2)
- [How To Make Custom AI-Generated Text With GPT-2](https://minimaxir.com/2019/09/howto-gpt2/)
- [How to Build a Twitter Text-Generating AI Bot With GPT-2](https://minimaxir.com/2020/01/twitter-gpt2-bot/)

## Context
This tutorial was created by the [Pool Numérique](https://www.hesge.ch/head/formations-recherche/pool-numerique) and the [Master Media Design](https://www.hesge.ch/head/formations-recherche/master-en-media-design) ([HEAD–Genève](https://www.hesge.ch/head)), for the Virtual Beings semester project (2021-22).
