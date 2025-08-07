# Markov Chain Text Generator

A simple implementation of a Markov chain text generator that can work at both character and word levels.

## Features

- Character-level text generation
- Word-level text generation
- Configurable order (number of previous items to consider)
- Customizable output length
- Optional starting sequence

## Usage

1. Clone this repository
2. Run the example:

```bash
python markov_chain.py
```

## Example Code

```python
from markov_chain import MarkovChain

# Create a character-level model
char_model = MarkovChain(text="Your input text here", order=3, level='char')
generated_text = char_model.generate(length=100)
print(generated_text)

# Create a word-level model
word_model = MarkovChain(text="Your input text here", order=2, level='word')
generated_text = word_model.generate(length=50)
print(generated_text)
```

## Parameters

- `text` (str): The input text to train the model on
- `order` (int): The order of the Markov chain (how many previous items to consider)
- `level` (str): Either 'char' for character-level or 'word' for word-level
- `length` (int): The desired length of the generated text
- `start` (tuple): Optional starting sequence for generation

## How it Works

The Markov chain model works by:

1. Breaking down the input text into tokens (characters or words)
2. Building a probability model based on the frequency of tokens following each sequence
3. Generating new text by randomly selecting tokens based on the learned probabilities

The higher the order, the more coherent but less varied the output will be. Lower orders will produce more varied but potentially less coherent text. 

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
