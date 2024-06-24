import spacy
from collections import Counter

def identify_and_sort_advanced_vocabulary(text):
    # Load the English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the text using SpaCy
    doc = nlp(text)

    # Extract advanced vocabulary (e.g., words with high complexity)
    advanced_vocab = [token.text.lower() for token in doc if token.is_alpha and token.is_stop is False and len(token.text) > 5]

    # Count the frequency of each word using Counter
    word_counts = Counter(advanced_vocab)

    # Sort the advanced vocabulary words by frequency
    sorted_advanced_vocab = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    return sorted_advanced_vocab

# Example usage
corpus_text = """
In order to foster a congenial environment, it is incumbent upon us to consistently exhibit altruism, fortitude, and sagacity, thereby empowering our interlocutors and engendering a sense of solidarity, camaraderie, and esprit de corps.
"""

sorted_advanced_vocab = identify_and_sort_advanced_vocabulary(corpus_text)

print("Sorted Advanced Vocabulary by Frequency:")
for word, frequency in sorted_advanced_vocab:
    print(f"{word}: {frequency}")
