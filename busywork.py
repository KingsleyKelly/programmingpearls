from collections import defaultdict
import string

def main():
  """Prints all anagrams in the wordlist."""
  f = open('/usr/share/dict/words')
  anagrams = defaultdict(list)
  for word in f.readlines():
    word = word.translate(string.maketrans("",""), string.punctuation).strip().lower()
    anagrams[''.join(sorted(word))] += [word]
  for i in anagrams.values():
    if len(i) > 1: print i

if __name__ == '__main__':
  main()




