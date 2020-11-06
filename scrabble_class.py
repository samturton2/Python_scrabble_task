# create parent class that stores scrabble scores
class Scrabble:
    def __init__(self):
        self.scrab_dict = {
            'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1,'R': 1, 'S': 1, 'T': 1, 'U': 1,
            'D': 2, 'G': 2,
            'B': 3, 'C': 3, 'M': 3, 'P': 3,
            'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
            'K': 5,
            'J': 8, 'X': 8,
            'Q': 10, 'Z': 10
        }

    # function that adds up the total score of the inputted string
    def score(self, word):
        total = 0

        # adds up the letters corresponding score
        for letter in word:
            total += self.scrab_dict[letter.upper()]

        return total

    # create a function that takes in the users word and gives out the score as long as they want
    def calculator_on(self):
        # loop round outputting user score
        while True:
            word = input("Input word ===> ")
            print(f"Scrabble score : {self.score(word)}")

            # ask user if they want to do another word, if not, break
            ask = input("Do you want to calculate another word? ")
            if ask[0].lower() == "n":
                break