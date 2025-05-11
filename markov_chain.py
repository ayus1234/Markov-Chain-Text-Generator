import random
from collections import defaultdict

class MarkovChain:
    def __init__(self, text, order=2, level='char'):
        """
        Initialize a Markov chain model.
        
        Args:
            text (str): The input text to train the model on
            order (int): The order of the Markov chain (how many previous items to consider)
            level (str): Either 'char' for character-level or 'word' for word-level
        """
        self.order = order
        self.level = level
        self.model = defaultdict(list)
        self.tokens = self._tokenize(text)
        self._build_model()
    
    def _tokenize(self, text):
        """Convert text into tokens based on the specified level."""
        if self.level == 'char':
            return list(text)
        else:  # word level
            return text.split()
    
    def _build_model(self):
        """Build the Markov chain model from the tokens."""
        for i in range(len(self.tokens) - self.order):
            key = tuple(self.tokens[i:i + self.order])
            value = self.tokens[i + self.order]
            self.model[key].append(value)
    
    def generate(self, length=100, start=None):
        """
        Generate new text using the Markov chain model.
        
        Args:
            length (int): The desired length of the generated text
            start (tuple): Optional starting sequence for generation
            
        Returns:
            str: The generated text
        """
        if not self.model:
            return ""
        
        # If no start sequence provided, choose a random one from the model
        if start is None:
            current = random.choice(list(self.model.keys()))
        else:
            current = start
        
        result = list(current)
        
        # Generate the rest of the sequence
        for _ in range(length - self.order):
            if current not in self.model:
                break
            
            next_token = random.choice(self.model[current])
            result.append(next_token)
            current = tuple(result[-self.order:])
        
        # Join the tokens back into text
        if self.level == 'char':
            return ''.join(result)
        else:
            return ' '.join(result)

def main():
    # Example usage
    sample_text = """
    To be, or not to be, that is the question:
    Whether 'tis nobler in the mind to suffer
    The slings and arrows of outrageous fortune,
    Or to take Arms against a Sea of troubles,
    And by opposing end them: to die, to sleep
    No more; and by a sleep, to say we end
    The heart-ache, and the thousand natural shocks
    That Flesh is heir to? 'Tis a consummation
    Devoutly to be wished. To die, to sleep,
    To sleep, perchance to Dream; aye, there's the rub,
    For in that sleep of death, what dreams may come,
    When we have shuffled off this mortal coil,
    Must give us pause. There's the respect
    That makes Calamity of so long life:
    """
    
    # Create character-level model
    char_model = MarkovChain(sample_text, order=3, level='char')
    print("Character-level generation:")
    print(char_model.generate(length=100))
    print("\n")
    
    # Create word-level model
    word_model = MarkovChain(sample_text, order=2, level='word')
    print("Word-level generation:")
    print(word_model.generate(length=50))

if __name__ == "__main__":
    main() 