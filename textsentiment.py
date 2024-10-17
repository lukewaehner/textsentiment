import spacy
import glob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Load spaCy language model
nlp = spacy.load('en_core_web_sm')

# Get the list of speech files
speech_files = glob.glob('TATE_SPEECHES/*.txt')

# Initialize the SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()


def preprocess_text_spacy(text):
    """
    Preprocesses the input text using spaCy to lemmatize and remove punctuation and stop words.

    Args:
        text (str): The text to preprocess.

    Returns:
        str: The preprocessed text.
    """
    doc = nlp(text)
    tokens = [token.lemma_.lower()
              for token in doc if not token.is_punct and not token.is_stop]
    return ' '.join(tokens)


# Read and preprocess each speech
preprocessed_speeches = []
for file_path in speech_files:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        preprocessed_speeches.append(preprocess_text_spacy(text))

# Update the negative sentence extraction using spaCy
negative_sentences = []

for file_path in speech_files:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        doc = nlp(text)
        for sent in doc.sents:
            score = sid.polarity_scores(sent.text)
            if score['compound'] < -0.2:  # Adjust the threshold as needed
                negative_sentences.append((sent.text, score))

# Initialize accumulators for sentiment scores
total_neg, total_neu, total_pos, total_compound = 0, 0, 0, 0

# Analyze sentiment for each negative sentence and accumulate scores
for sentence, score in negative_sentences:
    total_neg += score['neg']
    total_neu += score['neu']
    total_pos += score['pos']
    total_compound += score['compound']

# Calculate the average scores
num_sentences = len(negative_sentences)
if num_sentences > 0:
    avg_neg = total_neg / num_sentences
    avg_neu = total_neu / num_sentences
    avg_pos = total_pos / num_sentences
    avg_compound = total_compound / num_sentences

    # Print average scores
    print(f"Average Negative Score: {avg_neg}")
    print(f"Average Neutral Score: {avg_neu}")
    print(f"Average Positive Score: {avg_pos}")
    print(f"Average Compound Score: {avg_compound}")

    # Plot average sentiment scores
    labels = ['Negative', 'Neutral', 'Positive', 'Compound']
    averages = [avg_neg, avg_neu, avg_pos, avg_compound]

    plt.bar(labels, averages, color=['red', 'grey', 'green', 'blue'])
    plt.title('Average Sentiment Scores')
    plt.ylabel('Scores')
    plt.show()

    # Sort negative sentences by negativity and compound scores
    sorted_by_neg = sorted(
        negative_sentences, key=lambda x: x[1]['neg'], reverse=True)
    sorted_by_compound = sorted(
        negative_sentences, key=lambda x: x[1]['compound'])

    # Print sorted sentences
    print("\nSentences sorted by negativity:")
    for sentence, score in sorted_by_neg:
        print(f"Sentence: {sentence}")
        print(
            f"Negativity Score: {score['neg']}, Compound Score: {score['compound']}\n")

    print("\nSentences sorted by compound score:")
    for sentence, score in sorted_by_compound:
        print(f"Sentence: {sentence}")
        print(
            f"Compound Score: {score['compound']}, Negativity Score: {score['neg']}\n")
else:
    print("No negative sentences found.")
