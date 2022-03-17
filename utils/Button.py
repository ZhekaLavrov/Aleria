class Button(object):
    def __init__(self, data: tuple):
        self._button_id = data[0]
        self._answer_id = data[1]
        self.button_number = data[2]
        self.button = data[3]

    def get_button_id(self):
        return self._button_id
