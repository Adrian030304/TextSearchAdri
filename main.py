import string
import nltk
from nltk.tokenize import TreebankWordTokenizer
from nltk.stem.porter import PorterStemmer

docs = [
    '''About us. We deliver Artificial Intelligence & Machine Learning
       solutions to solve business challenges.''',
    '''Contact information. Email [martin davtyan at filament dot ai]
       if you have any questions''',
    '''Filament Chat. A framework for building and maintaining a scalable
       chatbot capability''',
]


REMOVE_PUNCTUATION = str.maketrans({x: None for x in string.punctuation})
TOKENIZER = TreebankWordTokenizer()

example_doc = docs[1]
print(example_doc)
example_doc_token = TOKENIZER.tokenize(
    example_doc.translate(REMOVE_PUNCTUATION)
)

print(example_doc_token)

STEMMER = PorterStemmer()

example_doc_tokenized_stemmed = [STEMMER.stem(token) for token in example_doc_token]


