import random

from flask import Flask, render_template
app = Flask(__name__)

with open('words.txt') as words_file:
    words = [w.strip() for w in words_file.readlines()]

with open('bits.txt') as bits_file:
    bits = [w.strip() for w in bits_file.readlines()]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/new')
def new():
    global bits, words
    bit = random.choice(bits)
    word = random.choice(words)

    word_position = -1
    if word[0] == '-':
        word_position = 1
        word = word[1:]
    elif word[-1] == '-':
        word_position = 0
        word = word[:-1]

    if word_position == 0:
        while bit == 'crypto':
            bit = random.choice(bits)

    if bit == 'crypto':
        word_position = 1
    elif word_position == -1:
        word_position = random.randint(0, 1)

    # Randomly switch case of singe letters
    if len(word) == 1 and random.random() >= 0.5:
        if word_position == 1:
            word = word.upper()
        else:
            bit = bit.capitalize()
        done = True

    else:
        done = False

    order = [bit, bit]
    order[word_position] = word
    name = ''.join(order)
    if not done:
        name = name.capitalize()
    return name

app.run()
