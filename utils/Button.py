class Button(object):
    def __init__(self, data: tuple):
        self.button_id = data[0]
        self.answer_id = data[1]
        self.button_number = data[2]
        self.button = data[3]
