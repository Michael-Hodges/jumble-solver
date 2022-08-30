# Jumble-Solver

## Downloading Word List
```sh
curl http://www.mieliestronk.com/corncob_lowercase.txt --output wordlist.txt
```
## Usage
```sh
python3 jumble_solver.py <path_to_word_list> <word_to_solve_with>
```
or
```sh
python3 jumble_trie.py <path_to_word_list> <word_to_solve_with>
```
## Complexity analysis

### jumble_solver.py
This program runs in O(N(K!)) time. Where N is the length of the word list and
K is the number of letters in the provided word. If the user needs to solve 
many different jumbled words with the same word list the solution could take a 
long time as the solve method has to loop through the entire word list each 
time.

### jumble_trie.py (Alternate solution using a Trie)
To solve the problem with linear time we can store the word list in a Trie to 
make subsequent searches faster using DFS. The Trie is built in O(N) time. And 
then a solution is found in O(K!*log(N)). The drawback with this implementation
is that the trie stores whole word list in memory.
