import json

INPUT_FILE = "analyzed_data.json"
OUTPUT_FILE = "summary.json"

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    positive = 0
    negative = 0
    neutral = 0

    for item in data:
        sentiment = item.get("sentiment", "Neutral")

        if sentiment == "Positive":
            positive += 1
        elif sentiment == "Negative":
            negative += 1
        else:
            neutral += 1

    total_news = positive + negative + neutral

    if positive > negative and positive > neutral:
        overall_trend = "Overall Positive"
    elif negative > positive and negative > neutral:
        overall_trend = "Overall Negative"
    else:
        overall_trend = "Neutral / Mixed"

    summary = {
        "total_news": total_news,
        "positive_news": positive,
        "negative_news": negative,
        "neutral_news": neutral,
        "market_trend": overall_trend
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)

    print("Part 3 done! Market summary created.")

if __name__ == "__main__":
    main()