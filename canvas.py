from unicodedata import east_asian_width
class Canvas:
    messages = []

    @classmethod
    def store(cls, messages):
        cls.messages += messages

    @classmethod
    def draw(cls):
        def length(str):
            str_length = 0
            for c in str:
                # east_asian_widthを用いて全角を2文字として数える
                if 'NaH'.count(east_asian_width(c)) > 0:
                    str_length += 1
                else:
                    str_length += 2

            return str_length
        messages = cls.messages
        cls.__clear()
        max_length = 0
        for m in messages:
            m_len = length(m)
            if m_len > max_length:
                max_length = m_len
        messages.insert(0, '*' * max_length)
        messages.append('*' * max_length)
        for i, m in enumerate(messages):
            messages[i] = m + (' ' * (max_length - length(m)))

        return '\n'.join([f'*{m}*' for m in messages])

    @classmethod
    def __clear(cls):
        cls.messages = []
