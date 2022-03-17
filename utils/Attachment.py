class Attachment(object):
    def __init__(self, data):
        self._attachment_id = data[0]
        self._answer_id = data[1]
        self.attachment_number = data[2]
        self.attachment_link = data[3]
