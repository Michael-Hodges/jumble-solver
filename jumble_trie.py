import argparse
import time

class TrieNode():
    """A datastructure used to represent a letter in the trie.

    Attributes:
        val: a dictionary of children letters
        word: boolean indicating if this node represents a word
    """
    def __init__(self,):
        self.val = {}
        self.word = False

class JumbleSolver():
    """Generates all matching sub-anagrams for a word from a provided
    word list.

    Attrributes:
        file: path to the word list file
        trie: a trie representing the word list
    """
    def __init__(self, file: str) -> None:
        """Initializes JumbleSolver class with the provided word list."""
        self.file   = file
        self._trie  = self._build_trie()

    def _build_trie(self,) -> TrieNode:
        ret = TrieNode()
        with open(self.file, encoding='utf-8') as f:
            for line in f:
                # Start at root node for each word in list while building.
                start = ret
                for letter in line.lower().strip():
                    start = start.val.setdefault(letter, TrieNode())
                start.word = True
        return ret

    def solve(self, word: str) -> [str]:
        """Generates sub_anagrams from the provided word"""
        ret = [word]
        def helper(built_word, word, trie_node):
            if trie_node.word:
                add_word = ''.join(let for let in built_word)
                # Only add word to list if not in list already
                if add_word not in ret:
                    ret.append(add_word)
            for idx, val in enumerate(word):
                if val in trie_node.val:
                    helper(built_word + [val], word[0:idx] + word[idx+1:] , trie_node.val[val])
        helper([], list(word.strip().lower()), self._trie)
        # Don't include base word in returned answer
        return ret[1:]

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
