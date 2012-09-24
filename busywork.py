
import string
primes = """6373 6379 6389 6397 6421 6427 6449 6451 6469 6473 6481 6491 6521 6529 6547 6551 6553 6563 6569 6571 6577 6581 6599 6607 6619 6637 6653 6659 6661 6673 6679 6689 6691 6701 6703 6709 6719 6733  6737 6761 6763 6779 6781 6791 6793 6803 6823 6827 6829 6833 6841 6857 6863 6869 6871 6883 6899 6907 6911 6917 6947 6949 6959 6961 6967 6971 6977 6983 6991 6997 7001 7013 7019 7027 7039 7043 7057 7069 7079 7103 7109 7121 7127 7129 7151 7159 7177 7187 7193 7207 7211 7213 7219 7229 7237 7243 7247 7253 7283 7297 7307 7309 7321 7331 7333 7349 7351 7369 7393 7411 7417 7433 7451 7457 7459 7477 7481 7487 7489 7499 7507 7517 7523 7529 7537 7541 7547 7549 7559 7561 7573 7577 7583 7589 7591 7603 7607 7621 7639 7643 7649 7669 7673 7681 7687 7691 7699 7703 7717 7723 7727 7741 7753 7757 7759 7789 7793 7817 7823 7829 7841 7853 7867 7873 7877 7879 7883 7901 7907 7919""".split(' ')
x = 0
new_values = []
anagrams = {}
key_list = {}
for i in string.lowercase:
  x += 1

  new_values.append(ord(i) * int(primes[x]) * int(primes[-(x+1)]))

def generate_value(word, new_values=new_values, key_list=key_list, anagrams=anagrams):
  new_word = word.lower()
  word = new_word.translate(string.maketrans("",""), string.punctuation)
  total_value = 0
  for i in word:
    total_value += new_values[string.lowercase.index(i)]
  try:
    if key_list[total_value]:
      try:
        if anagrams[total_value]:

          anagrams[total_value] = anagrams[total_value] + [word]

      except KeyError:
        anagrams[total_value] = key_list[total_value] + [word]
        return

  except KeyError:
    key_list[total_value] = [word]
    return
  # return (word.upper(), total_value)

# anagrams = []
f = open('/usr/share/dict/words')
the_seas = []
counter = 0
for i in f.readlines():
  i = i.strip()
  counter += 1
  if i and counter % 2 == 0:
    the_seas.append(i)


the_seas = [generate_value(i) for i in the_seas]
# new_seas = [[] for i in range(26)]
# for i in the_seas:
#   bin = len(i[0]) -1
#   new_seas[bin].append(i)

# for r in new_seas:
#   for i in r:
#     anagram = False
#     current_anagrams = []
#     for j in r[r.index(i)+1:]:
#       if i[1] == j[1]:
#         current_anagrams.append(j[0])
#         r.pop(r.index(j))
#         anagram = True
#     if anagram:
#       current_anagrams.append(i[0])
#       anagrams.append(current_anagrams)
#     r.pop(r.index(i))
#   print anagrams

print anagrams.values()






