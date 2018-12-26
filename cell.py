class Cell:
    def __init__(self, text, visible):
        self.text = text
        self.visible = visible

    def open(self):
        self.visible = True

    def get_text(self):
        return self.text if self.visible is True else ' '
