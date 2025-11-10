import string
import nltk
from nltk.tokenize import TreebankWordTokenizer

REMOVE_PUNCTUATION = str.maketrans({x: None for x in string.punctuation})
TOKENIZER = TreebankWordTokenizer()

example_doc = docs[1]

example_doc_token = TOKENIZER.tokenize(
    example_doc.translate(REMOVE_PUNCTUATION)
)



