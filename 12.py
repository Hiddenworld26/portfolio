import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Initialize the PorterStemmer
stemmer = PorterStemmer()

# Input sentence
sentence = "Stemming is the process of reducing words to their word stem, base or root form."

# Tokenize the sentence into words
words = word_tokenize(sentence)

# Apply stemming to each word in the sentence
stemmed_words = [stemmer.stem(word) for word in words]

# Join the stemmed words back into a sentence
stemmed_sentence = ' '.join(stemmed_words)

# Print the original and stemmed sentence
print("Original Sentence:", sentence)
print("Stemmed Sentence:", stemmed_sentence)
