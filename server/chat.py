"""
Represents and store info about the chat
"""
from round import Round

class Chat(object):
    def __int__(self):
        self.content = []
        self.round = r

    def update_chat(self, mgs):
        self.content.append(mgs)

    def get_chat(self):
        return self.content

    def __len__(self):
        return len(self.content)

    def __str__(self):
        return " ".join(self.content)

    def __repr__(self):
        return str(self.content)