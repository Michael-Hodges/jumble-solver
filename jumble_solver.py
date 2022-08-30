import argparse
from collections import defaultdict

class JumbleSolver():
    """Generates all matching sub-anagrams for a word from a provided
    word list.

    Attrributes:
        file: path to the word list file
    """
    def __init__(self, file: str) -> None:
        """Initializes JumbleSolver class with the provided word list."""
        self.file = file

    def _build_list(self, word: str) -> [str]:
        ret = []

        # Count each letter in provided word for later comparison.
        word_letters = defaultdict(int)
        for letter in word:
            word_letters[letter] +=1

        with open(self.file, encoding='utf-8') as f:
            for line in f:
                check_word_letters = defaultdict(int)
                current_word = line.strip().lower()
                need_to_add_word = True
                # Only add to answer if count of each letter in current word
                # is less than provided jumbled word.
                for letter in current_word:
                    if check_word_letters[letter] >= word_letters[letter]:
                        need_to_add_word = False
                        break
                    check_word_letters[letter] += 1
                if need_to_add_word and current_word != word:
                    ret.append(current_word)
        return ret

    def solve(self, word: str) -> [str]:
        """Generates sub_anagrams from the provided word"""
        return self._build_list(word.strip().lower())


def main():
    parser = argparse.ArgumentParser(
                description="Solve Jumble with the given word list and word")
    parser.add_argument('file', type=str, nargs='?', default='./wordlist.txt', 
                        help="Path to word list")
    parser.add_argument('word', type=str, nargs='?', default="dog", 
                        help="Word to solve with")
    args = parser.parse_args()

    my_game = JumbleSolver(args.file)
    print(my_game.solve(args.word))

if __name__ == '__main__':
    main()
