from chat_downloader import ChatDownloader


class Downloader:

    def __init__(self, url):
        self.chat = ChatDownloader()
        self.url = url
        self.last_message = None

    def get_messages(self, num=None):
        result = []
        chat = self.chat.get_chat(self.url, max_messages = num)
        for i in chat:
            result.append(i["message"])
        return result



