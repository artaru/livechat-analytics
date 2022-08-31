from sentimentModel import Classifier
from tokenizer import Tokenizer
from downloader import Downloader
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "True"


class Collector:

    def __init__(self, url):
        self.down = Downloader(url)
        self.tok = Tokenizer()
        self.cla = Classifier()

    def analytics(self, batch):
        mes = self.down.get_messages(batch)
        negative, neutral, positive = 0, 0, 0
        for o in range(len(mes)):
            mes[o] = self.tok.tokenize(mes[o])
            pred = self.cla.predict(mes[o])
            negative += pred[0]
            neutral += pred[1]
            positive += pred[2]
        return [negative, neutral, positive]
