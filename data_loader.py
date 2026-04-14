import json

def load_data("dataset/eng_restaurant_trial_alltasks.jsonl"):
    data = []
    
    with open("dataset/eng_restaurant_trial_alltasks.jsonl", 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    
    return data


def get_sample(data):
    return data[0]