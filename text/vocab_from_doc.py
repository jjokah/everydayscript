import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")

text = "In order to foster a congenial environment, it is incumbent upon us to consistently exhibit altruism, fortitude, and sagacity, thereby empowering our interlocutors and engendering a sense of solidarity, camaraderie, and esprit de corps."

doc = nlp(text)

advanced_words = []

for token in doc:
    if token.lemma_ not in nlp.Defaults.stop_words:
        if token.pos_ in ["NOUN", "VERB", "ADJ"]:
            # if token.dep_ in ["nsubj", "dobj", "amod"]:
            advanced_words.append(token.text)

# Count occurrences of each word
word_freq = Counter(advanced_words)

# Sort only by frequency
sorted_words = sorted(advanced_words, key=lambda x: word_freq[x], reverse=True)

print("Sorted advanced words by frequency:", sorted_words)
