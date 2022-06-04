import cleaning
from cleaning import *

# Return's index of the character from the vocab list
def index_character (vocab, character):
  for i in range(len(vocab)):
    if vocab[i] == character :
      return i
  return -1

def compute_oneHotEncoding(text):
  cleaned_text = cleaning_data(text)
  sentence_tensor = torch.zeros([1014,70])
  j = 0
  for i in cleaned_text:
    index = index_character(vocab, i)
    char_tensor = torch.zeros(1,70)
    char_tensor[0][index] = 1
    sentence_tensor[j] = char_tensor
    j += 1
  return sentence_tensor