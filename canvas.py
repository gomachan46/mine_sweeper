class Canvas:
    messages = []

    @classmethod
    def store(cls, messages):
        cls.messages += messages

    @classmethod
    def draw(cls):
        messages = cls.messages
        cls.__clear()
        return '\n'.join(messages)

    @classmethod
    def __clear(cls):
        cls.messages = []
