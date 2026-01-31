import json

# Simple sentiment word lists
positive_words = [
    "rise", "gain", "up", "strong", "profit", "positive",
    "higher", "growth", "beat", "rally"
]

negative_words = [
    "fall", "loss", "down", "weak", "negative",
    "lower", "decline", "drop", "slump"
]

INPUT_FILE = "arranged_data.json"
OUTPUT_FILE = "analyzed_data.json"


def get_sentiment(text):
    text = text.lower()
    score = 0

    for word in positive_words:
        if word in text:
            score += 1

    for word in negative_words:
        if word in text:
            score -= 1

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"


def main():
    # Read arranged data
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    analyzed_data = []

    for item in data:
        combined_text = item.get("headline", "") + " " + item.get("text", "")
        sentiment = get_sentiment(combined_text)

        item["sentiment"] = sentiment
        analyzed_data.append(item)

    # Save analyzed data
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(analyzed_data, file, indent=4, ensure_ascii=False)

    print("Part 2 done! Sentiment analysis completed.")


if __name__ == "__main__":
    main()