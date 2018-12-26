class Cell:
    def __init__(self, text, visible):
        self.text = text
        self.visible = visible
        self.mark = False

    def toggle_mark(self):
        if self.visible is True:
            return
        self.mark = not self.mark

    def open(self):
        if self.mark is True:
            return
        self.visible = True
        return self

    def get_text(self):
        if self.mark is True:
            return 'X'
        if self.visible is False:
            return ' '
        return self.text

    def __str__(self):
        return self.get_text()
