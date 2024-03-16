# Импортируем необходимые библиотеки
import json  # Импортируем модуль для работы с JSON
import os  # Импортируем модуль для работы с операционной системой
import time  # Импортируем модуль для работы со временем
from watchdog.observers import Observer  # Импортируем класс Observer из библиотеки watchdog для отслеживания изменений в файловой системе
from watchdog.events import FileSystemEventHandler  # Импортируем класс FileSystemEventHandler для обработки событий файловой системы

# Путь к отслеживаемой директории
directory_to_watch = "путь к файлу"

# Путь к файлу JSON, куда будут записываться изменения
json_file_path = "changes.json"

# Функция для создания или обновления JSON файла
def update_json(events):
    with open(json_file_path, 'w') as json_file:  # Открываем файл для записи
        json.dump(events, json_file, indent=4)  # Записываем список событий в формате JSON с отступами для читаемости

# Класс обработчика событий файловой системы
class MyHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()  # Вызываем конструктор родительского класса
        self.events = []  # Инициализируем список для хранения событий

    # Метод для обработки любых событий
    def on_any_event(self, event):
        if event.is_directory:  # Если событие связано с директорией, игнорируем его
            return

        file_path = event.src_path  # Получаем путь к файлу, который вызвал событие
        event_type = event.event_type  # Получаем тип события
        timestamp = time.ctime()  # Получаем текущее время

        # Добавляем событие в список
        self.events.append({
            "event_type": event_type,  # Тип события
            "file_path": file_path,  # Путь к файлу
            "timestamp": timestamp  # Временная метка
        })

        # Записываем список событий в JSON файл
        update_json(self.events)

if __name__ == "__main__":
    # Создаем пустой JSON файл, если его нет
    if not os.path.exists(json_file_path):  # Проверяем существует ли файл по указанному пути
        update_json([])  # Если файла нет, создаем пустой JSON

    event_handler = MyHandler()  # Создаем экземпляр класса обработчика событий
    observer = Observer()  # Создаем объект наблюдателя
    observer.start()  # Запускаем наблюдение за изменениями в файловой системе
    try:
        observer.schedule(event_handler, directory_to_watch, recursive=True)  # Регистрируем обработчик событий для отслеживаемой директории
        while True:
            time.sleep(1)  # Приостанавливаем выполнение программы на 1 секунду
    except KeyboardInterrupt:  # Обрабатываем прерывание программы пользователем
        observer.stop()  # Останавливаем наблюдение за изменениями
    observer.join()  # Дожидаемся завершения работы наблюдателя