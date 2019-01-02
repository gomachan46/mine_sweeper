from unicodedata import east_asian_width


class Canvas:
    main_messages = []
    side_messages = []

    @classmethod
    def store_main(cls, messages):
        cls.main_messages += messages

    @classmethod
    def store_side(cls, messages):
        cls.side_messages += messages

    @classmethod
    def draw(cls):
        main_messages = cls.main_messages
        main_size = len(main_messages)
        main_max_length = cls.__max_length(main_messages)
        side_messages = cls.side_messages
        side_size = len(side_messages)
        side_max_length = cls.__max_length(side_messages)
        messages = []
        message_size = len(messages)
        if main_size > side_size:
            message_size = main_size
            for _ in range(main_size - side_size):
                side_messages.append(' ' * side_max_length)
        elif side_size > main_size:
            message_size = side_size
            for _ in range(side_size - main_size):
                main_messages.append(' ' * main_max_length)

        cls.__clear()
        for index in range(message_size):
            main_messages[index] += ' ' * (main_max_length - cls.__length(main_messages[index]))
            side_messages[index] += ' ' * (side_max_length - cls.__length(side_messages[index]))
            if main_messages[index] == '':
                messages.append(side_messages[index])
            elif side_messages[index] == '':
                messages.append(main_messages[index])
            else:
                messages.append(' | '.join([main_messages[index], side_messages[index]]))

        message_max_length = cls.__max_length(messages)
        messages.insert(0, '*' * message_max_length)
        messages.append('*' * message_max_length)
        for i, m in enumerate(messages):
            messages[i] = m + (' ' * (message_max_length - cls.__length(m)))

        return '\n'.join([f'*{m}*' for m in messages])

    @classmethod
    def __clear(cls):
        cls.main_messages = []
        cls.side_messages = []

    @classmethod
    def __max_length(cls, messages):
        max_length = 0
        for m in messages:
            m_len = cls.__length(m)
            if m_len > max_length:
                max_length = m_len

        return max_length

    @classmethod
    def __length(cls, text):
        str_length = 0
        for c in text:
            # east_asian_widthを用いて全角を2文字として数える
            if 'NaH'.count(east_asian_width(c)) > 0:
                str_length += 1
            else:
                str_length += 2

        return str_length
