
# Task 1: Text Summarization Tool
# EliteTech AI Internship
# This program summarizes long text into a shorter version.

import re

def summarize_text(text, sentence_count=3):
    """Create a simple extractive summary from the input text."""

    # Split the text into sentences.
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    sentences = [s for s in sentences if s]

    # Return the original text if it is already short.
    if len(sentences) <= sentence_count:
        return text

    # Count how frequently each word appears.
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    stop_words = {
        "the", "is", "a", "an", "and", "or", "of", "to",
        "in", "for", "on", "with", "this", "that", "are",
        "was", "were", "it", "as", "by", "be", "at", "from"
    }

    frequency = {}
    for word in words:
        if word not in stop_words:
            frequency[word] = frequency.get(word, 0) + 1

    # Give each sentence a score based on its important words.
    scored_sentences = []
    for index, sentence in enumerate(sentences):
        sentence_words = re.findall(r'\b[a-zA-Z]+\b', sentence.lower())
        score = sum(frequency.get(word, 0) for word in sentence_words)
        scored_sentences.append((index, score, sentence))

    # Select the highest-scoring sentences.
    best_sentences = sorted(
        scored_sentences, key=lambda item: item[1], reverse=True
    )[:sentence_count]

    # Keep the selected sentences in their original order.
    best_sentences.sort(key=lambda item: item[0])
    return " ".join(item[2] for item in best_sentences)


if __name__ == "__main__":
    print("===== TEXT SUMMARIZATION TOOL =====")
    print("Paste an article below.")
    article = input("Enter your text: ")

    summary = summarize_text(article)

    print("\n===== SUMMARY =====")
    print(summary)
