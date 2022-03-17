class DB(object):
    def __init__(self, conn):
        """
        Конструктор класса.
        :param conn: объект подключения к базе данных
        """
        self.conn = conn
        self.cursor = self.conn.cursor()

    def get_questions(self):
        """
        Получает список всех вопросов.
        :return: список вопросов
        """
        self.cursor.execute("SELECT question_id, question FROM questions")
        return self.cursor.fetchall()

    def get_question_by_id(self, question_id):
        """
        Получает вопрос по id
        :param question_id: id вопроса в бд
        :return: вопрос
        """
        self.cursor.execute(
            "SELECT question_id, question FROM questions WHERE question_id = %s",
            (question_id, )
        )
        fetchone = self.cursor.fetchone()
        return fetchone

    def get_answers(self):
        """
        Получает список всех ответов.
        :return: список ответов
        """
        self.cursor.execute("SELECT answer_id, question_id, answer_text FROM answers")
        return self.cursor.fetchall()

    def get_answer_by_id(self, answer_id):
        """
        Получает вопрос по id
        :param answer_id: id ответа в базе данных
        :return:
        """
        self.cursor.execute(
            "SELECT answer_id, question_id, answer_text FROM answers WHERE answer_id = %s",
            (answer_id, )
        )
        fetchone = self.cursor.fetchone()
        return fetchone

    def get_answer_by_question_id(self, question_id):
        """
        Получает вопрос по id
        :param question_id: id вопроса в базе данных
        :return:
        """
        self.cursor.execute(
            "SELECT answer_id, question_id, answer_text FROM answers WHERE question_id = %s",
            (question_id, )
        )
        fetchone = self.cursor.fetchone()
        return fetchone

    def get_buttons(self):
        """
        Получает все кнопки из бд.
        :return: Список кнопок
        """
        self.cursor.execute("SELECT button_id, answer_id, button_number, button FROM buttons")
        return self.cursor.fetchall()

    def get_button_by_id(self, button_id):
        """
        Получает кнопку по ее id.
        :param button_id: id кнопки в бд
        :return:
        """
        self.cursor.execute(
            "SELECT button_id, answer_id, button_number, button FROM buttons WHERE button_id = %s",
            (button_id, )
        )
        fetchone = self.cursor.fetchone()
        return fetchone

    def get_buttons_by_answer_id(self, answer_id) -> list:
        """
        Получает все кнопки к ответу.
        :return: Список кнопок
        """
        self.cursor.execute(
            "SELECT button_id, answer_id, button_number, button FROM buttons "
            "WHERE answer_id = %s "
            "ORDER BY button_number",
            (answer_id, )
        )
        return self.cursor.fetchall()

    def get_attachments(self):
        """
        Получает все вложения из бд.
        :return: Список вложений
        """
        self.cursor.execute("SELECT attachment_id, answer_id, attachment_number, attachment_link FROM attachments")
        return self.cursor.fetchall()

    def get_attachment_by_id(self, attachment_id: int) -> tuple | None:
        """
        Получает вложение по id.
        :param attachment_id: ID вложения в бд
        :return: Вложение
        """
        self.cursor.execute(
            "SELECT attachment_id, answer_id, attachment_number, attachment_link FROM attachments "
            "WHERE attachment_id = %s",
            (attachment_id, )
        )
        fetchone = self.cursor.fetchone()
        return fetchone

    def get_attachments_by_answer_id(self, answer_id: int) -> list:
        """
        Получает вложения к ответу.
        :param answer_id: ID ответа
        :return: список вложений
        """
        self.cursor.execute(
            "SELECT attachment_id, answer_id, attachment_number, attachment_link FROM attachments "
            "WHERE answer_id = %s "
            "ORDER BY attachment_number",
            (answer_id, )
        )
        return self.cursor.fetchall()
