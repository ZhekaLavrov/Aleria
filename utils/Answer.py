from database import DB
from utils import create_connection
from utils.Button import Button
from utils.Attachment import Attachment


class Answer(object):
    def __init__(self, data):
        self._answer_id = data[0]
        self.question_id = data[1]
        self.answer_text = data[2]
        self.buttons = self.get_buttons()
        self.attachments = self.get_attachments()

    def get_buttons(self):
        connection = create_connection()
        try:
            db = DB(connection)
            buttons = db.get_buttons_by_answer_id(self._answer_id)
        finally:
            connection.close()
        buttons = [Button(button) for button in buttons]
        return buttons

    def get_attachments(self):
        connection = create_connection()
        try:
            db = DB(connection)
            attachments = db.get_attachments_by_answer_id(self._answer_id)
        finally:
            connection.close()
        attachments = [Attachment(attachment) for attachment in attachments]
        return attachments
