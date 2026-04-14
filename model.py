from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def predict_va(text, aspect):
    result = classifier(text)[0]

    if result['label'] == 'POSITIVE':
        valence = 7.5
        arousal = 6.5
    else:
        valence = 2.5
        arousal = 7.0

    return round(valence, 2), round(arousal, 2)