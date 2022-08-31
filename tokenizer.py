import re  # library for regular expression operations
import string  # for string operations

from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer


def remove_hyperlinks(mes) -> str:
    new_message = re.sub(r'https?:.*[\r\n]*', '', mes)
    new_message = re.sub(r'#', '', new_message)
    return new_message


class Tokenizer:
    def __init__(self):
        self.token = TweetTokenizer(preserve_case=False,
                                    strip_handles=True,
                                    reduce_len=True)
        self.stopwords_english = stopwords.words('english')
        self.punctuations = string.punctuation

    def tokenize_message(self, new_mes) -> list:
        message_tokens = self.token.tokenize(new_mes)
        return message_tokens

    def remove_stopwords_punctuations(self, message_tokens) -> list:

        tweets_clean = []

        for word in message_tokens:
            if word not in self.stopwords_english and word not in self.punctuations:
                if word[-1] == '@' and len(word) > 1:
                    word = "@user"
                tweets_clean.append(word)

        return tweets_clean

    def tokenize(self, message):
        processed = remove_hyperlinks(message)
        tokenized = self.tokenize_message(processed)
        result = self.remove_stopwords_punctuations(tokenized)
        return result
