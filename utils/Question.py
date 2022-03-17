from database import DB
from utils import create_connection
from utils.Answer import Answer


class Question(object):
    def __init__(self, data: tuple):
        self._question_id = data[0]
        self.questions = data[1]
        self.answer = self.get_answer()

    def get_answer(self):
        connection = create_connection()
        try:
            db = DB(connection)
            answer = db.get_answer_by_question_id(self._question_id)
        finally:
            connection.close()
        if answer is not None:
            answer = Answer(answer)
        return answer
