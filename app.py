from flask import Flask, request
import re

app = Flask(__name__)

intent_json = {
    "chatLog": [
        {
            "utterance": "Hi, Mario's what can I get you?",
            "intent": "Greeting"
        },
        {
            "utterance": "I'd like to order a pizza for pickup please.",
            "intent": "HowCanIHelp"
        },
        {
            "utterance": "OK, what would you like to order?",
            "intent": "ReadyToReceiveOrder"
        },
        {
            "utterance": "I'd like a medium supreme pizza.",
            "intent": "OrderItem"
        },
        {
            "utterance": "Anything more?",
            "intent": "AnyMoreItems"
        },
        {
            "utterance": "Also, a garlic bread.",
            "intent": "OrderItem"
        },
        {
            "utterance": "Is that all?",
            "intent": "AnyMoreItems"
        },
        {
            "utterance": "Yes, that is all thanks.",
            "intent": "EndOfOrder"
        },
        {
            "utterance": "OK, your order is a medium supreme and a garlic bread.",
            "intent": "ConfirmItem"
        },
        {
            "utterance": "Should be ready in about 30 minutes.",
            "intent": "DurationBeforePickupAnswer"
        },
        {
            "utterance": "Thank you, goodbye.",
            "intent": "Goodbye"
        }
    ]
}


def jaccard_similarity(str1, str2):
    split_regex = '[, . ? ! ]'
    x = str1[:-1]
    y = str2[:-1]

    a = set(list(filter(None, re.split(split_regex, x))))
    b = set(list(filter(None, re.split(split_regex, y))))

    c = a.intersection(b)
    d = a.union(b)

    return float(len(c)) / len(d)


def find_intent(utterance):
    max_similarity = 0
    intent = ""
    for chatLog in intent_json["chatLog"]:
        similarity = jaccard_similarity(chatLog["utterance"], utterance)
        if similarity > max_similarity:
            max_similarity = similarity
            intent = chatLog["intent"]
    return intent


@app.route('/')
def redirect():
    return "go to /health route"


@app.route('/health')
def health():
    ok_response = str(200)
    return '{"status: "' + ok_response + '"}'


# add post route
@app.route('/detect_intent', methods=['POST'])
def detect_intent():

    utterance = request.get_json()['message']
    # print(utterance)
    intent = find_intent(utterance)

    return '{"utterance: "' + utterance + ' ,"intent": "' + intent + '"}'


if __name__ == '__main__':
    app.run(debug=True)
