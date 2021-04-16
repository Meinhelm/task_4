import sqlite3

class SQLighter:

    def __init__(self, database_file):
        """Подключаем к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def get_Users(self,status = True):
        """Получаем всех активных подпищиков бота"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM 'users' WHERE 'status' = ?" , (status,)).fetchall()

    def subscriber_exists(self,user_id):
        """Проверяем есть ли юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))

    def add_subscriber(self,user_id,status = True):
        """Добавляем нового юзера"""
        with self.connection:
            return self.cursor.execute("INSERT INTO 'users' ('user_id','status') VALUES (?,?)",(user_id,status))

    def update_users(self,user_id,status):
        """Обновляем статус подписки"""
        return self.cursor.execute("UPDATE 'users' SET 'status' = ? WHERE 'user_id' = ?",(user_id, status))

    def close(self):
        """Закрываем соединение"""
        self.connection.close()
