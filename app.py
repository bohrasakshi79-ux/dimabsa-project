from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

classifier = pipeline("sentiment-analysis")

@app.route("/", methods=["GET", "POST"])
def home():
    result = []
    overall_sentiment = ""

    if request.method == "POST":
        sentence = request.form["sentence"]
        aspects = request.form["aspects"].split(",")

        # Overall sentiment
        overall = classifier(sentence)[0]
        overall_sentiment = overall["label"]

        # Aspect-wise sentiment
        for aspect in aspects:
            aspect = aspect.strip()
            aspect_result = classifier(f"{aspect} {sentence}")[0]
            result.append({
                "aspect": aspect,
                "sentiment": aspect_result["label"]
            })

    return render_template("index.html", result=result, overall=overall_sentiment)

if __name__ == "__main__":
    app.run(debug=True)