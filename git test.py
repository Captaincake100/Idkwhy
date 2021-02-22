import numpy
import tflearn
import tensorflow
import random
import json

import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

with open("intents.json") as file:


