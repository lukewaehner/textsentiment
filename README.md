# Sentiment Analysis of Andrew Tate Speeches

This project analyzes the sentiment of speeches by Andrew Tate using spaCy and NLTK's VADER sentiment analysis tool. The analysis focuses on identifying negative sentences and calculating average sentiment scores.

## Project Structure

- **textsentiment.py**: The main script that processes text files containing speeches to analyze sentiment.
- **TATE_SPEECHES/**: Directory containing text files of Andrew Tate's speeches.

## Dependencies

- **spaCy**: Used for text preprocessing, including lemmatization and stop word removal.
- **NLTK**: Specifically, the VADER sentiment analysis tool is used to score the sentiment of sentences.
- **glob**: For file path matching.
- **matplotlib**: For plotting average sentiment scores.

## Usage

1. Ensure the `TATE_SPEECHES` directory contains text files to be analyzed.
2. Run the `textsentinemmt.py` script to output sentiment analysis results.

## Script Details

### textsentinemmt.py

This script processes text files containing speeches to analyze sentiment using spaCy and NLTK's VADER sentiment analysis tool. It identifies negative sentences and calculates average sentiment scores.

- **Preprocessing**: The script uses spaCy to preprocess text by lemmatizing and removing punctuation and stop words.
- **Sentiment Analysis**: NLTK's VADER is used to analyze the sentiment of each sentence in the speeches.
- **Negative Sentence Extraction**: Sentences with a compound score below a certain threshold are considered negative.
- **Average Sentiment Scores**: The script calculates and prints average sentiment scores for negative sentences.
- **Visualization**: A bar chart is plotted to visually represent the average sentiment scores.
- **Sorting**: Negative sentences are sorted by their negativity and compound scores for further analysis.

## Text Files

### TATE_SPEECHES/ANDREW_TATE_SIGMA_MALE.txt

Contains a speech by Andrew Tate discussing various topics, including depression, vaping, and societal norms.

### TATE_SPEECHES/TATE_EXPOSED.txt

An excerpt from a speech by Andrew Tate, by Piers Morgan.

### Other Files

- **TATE_SPEECHES/ANDREW_TATE_MOTIVATIONAL_SPEECH.txt**
- **TATE_SPEECHES/TATE_MISOGYNY.txt**
- **TATE_SPEECHES/ANDREW_TATE_MEN_ARE_BUILT_TO_CONQUER.txt**

These files are additional speeches by Andrew Tate.

## How to Run

1. Install the required Python packages:
   ```bash
   pip install spacy nltk matplotlib
   ```
2. Download the spaCy language model:
   ```bash
   python -m spacy download en_core_web_sm
   ```
3. Run the script:
   ```bash
   python textsentinemmt.py
   ```

## License

This project is for educational purposes and is not intended for commercial use. Ensure compliance with all applicable copyright laws when using the content.
