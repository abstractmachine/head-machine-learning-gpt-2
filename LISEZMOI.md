# Parler aux robots

## Traduction
There is an english version of this tutorial [Talking to robots](README.md).

## Entraîner un bot GPT-2
Il s'agit d'un didacticiel/liste de contrôle pour l'installation, la formation et l'utilisation de [GPT-2](https://en.wikipedia.org/wiki/GPT-2).

## Histoire
Qu'est-ce que c'est?

- Qu'est-ce qu'un Transformer (de texte) ?

## Premier contact
(Talking with a GPT-2 bot online)
- [](https://app.inferkit.com/demo)

## Re-former GPT dans votre propre style
GPT-2 est formé avec un ensemble de données générales de connaissances et de conversations humaines. Cela rend les conversations ennuyeuses. Apprenons-lui à parler dans un style, une manière ou une syntaxe spécifique.

### Préparation de votre machine
- Téléchargez [Visual Studio Code](https://code.visualstudio.com) pour votre machine (Mac, PC, Linux)
- Ouvrir le code VS
- Ouvrez l'onglet "Extensions" et vérifiez que l'extension [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) est installée
- Créez un dossier pour votre projet et ouvrez le dossier dans VS Code.
- Créez un nom de fichier intitulé "train.ipynb" dans ce dossier
- Cela devrait ouvrir l'interface d'entrée Jupyter. Par exemple, vous devriez voir de nouveaux boutons intitulés `+Code`, `+Markdown`, `>Run All`
- Cette interface est maintenant prête à recevoir des commandes Python (voir ci-dessous). Chaque commande est saisie étape par étape dans votre interface Jupyter. Les résultats à la fin de chaque commande seront affichés directement dans cette fenêtre, après quoi vous pourrez entrer la commande suivante.

### Préparation de votre ensemble de données
- Sources de texte (désolé, anglais uniquement pour l'instant)
- Guttenberg (apprenez à votre bot à parler comme Virginia Woolf)
- Nettoyer votre texte
- Correspondance de motifs
- Mode d'expérimentation : Apprendre Regex

### Entraînez votre bot
- À ce stade, commencez à créer un nouveau bloc de code.
- Le premier bloc de code est :

```
!pip install -q gpt-2-simple
import gpt_2_simple as gpt2
from datetime import datetime
```

Le code ci-dessus vérifie si la bibliothèque `gpt-2-simple` est installée sur votre système. Nous devons également `importer` les bibliothèques `gpt_2_simple` et `datetime`.

Vous pouvez maintenant appuyer sur Play pour exécuter cette partie du code. (ça va prendre un peu de temps...)
 
Nous allons maintenant vérifier l'état de la carte graphique, cela peut être utile si vous avez une carte graphique puissante.

```
!nvidia-smi
```

Appuyez sur Play pour voir le résultat.
Après cela, nous téléchargerons le plus petit modèle de GPT2 :

```
gpt2.download_gpt2(model_name="124M")
```

Appuyez à nouveau sur Play et attendez également que le modèle se télécharge sur votre ordinateur.

## Parler à votre bot
Maintenant que nous avons formé notre bot avec son propre style, commençons à lui parler.

### Invite de ligne de commande
(communication directe avec le bot en ligne de commande)

### Communication API simple
(créez un serveur rapide en Python, parlez-lui depuis une page Web)

Différentes façons de parler à votre bot.
- Page Web
- Traitement
-P5
- Unité
- Ficelle
- Godot
-Max/MSP

## Attribution
Ce tutoriel reconditionne le bloc-notes Google Colab de [Max Woolf](https://minimaxir.com) [Train a GPT-2 Text-Generating Model w/ GPU]() et leur [gpt-2-simple](https:/ /github.com/minimaxir/gpt-2-simple) code de formation.

## Tutoriels en ligne
- [GPT-2 Neural Network Poetry](https://www.gwern.net/GPT-2)
- [How To Make Custom AI-Generated Text With GPT-2](https://minimaxir.com/2019/09/howto-gpt2/)
- [How to Build a Twitter Text-Generating AI Bot With GPT-2](https://minimaxir.com/2020/01/twitter-gpt2-bot/)

## Le contexte
Ce tutoriel a été réalisé par le [Pool Numérique](https://www.hesge.ch/head/formations-recherche/pool-numerique) et le [Master Media Design](https://www.hesge.ch/head /formations-recherche/master-en-media-design) ([HEAD–Genève](https://www.hesge.ch/head)), pour le projet de semestre Virtual Beings (2021-22).