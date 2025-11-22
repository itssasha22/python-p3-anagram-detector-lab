class Anagram:
    def __init__(self, word):
        self.word = word.lower()
    
    def match(self, words):
        # Sort the letters of the initialized word
        sorted_word = sorted(self.word)
        
        # Filter words that have the same sorted letters
        matches = []
        for word in words:
            if sorted(word.lower()) == sorted_word and word.lower() != self.word:
                matches.append(word)
        
        return matches
