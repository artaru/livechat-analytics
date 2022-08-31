from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax


class Classifier:
    def __init__(self):
        self.sentiment = "cardiffnlp/twitter-roberta-base-sentiment"
        self.classifier = AutoModelForSequenceClassification.from_pretrained(
            self.sentiment)
        self.auto_tokenizer = AutoTokenizer.from_pretrained(self.sentiment)

    def predict(self, text):
        post = self.auto_tokenizer(" ".join(text), return_tensors="pt")

        prediction = softmax(self.classifier(**post)[0][0].detach().numpy())
        return prediction[0], prediction[1], prediction[2]
