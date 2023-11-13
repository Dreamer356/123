import sqlite3
from datetime import datetime
import time

def update_temperature():
    # Підключення до бази даних
    conn = sqlite3.connect('temperature_database.db')
    cursor = conn.cursor()

    while True:
        # Вивід інформації про температуру з бази даних
        cursor.execute('SELECT * FROM temperature_data')
        rows = cursor.fetchall()

        print("ID\tDate Time\t\t\tTemperature")
        print("----------------------------------------")
        for row in rows:
            print(f"{row[0]}\t{row[1]}\t{row[2]}")

        # Оновлення температури
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_temperature = 27.5

        cursor.execute('INSERT INTO temperature_data (date_time, temperature) VALUES (?, ?)', (current_datetime, new_temperature))

        # Збереження змін та очікування 30 хвилин
        conn.commit()
        time.sleep(30 * 60)  # Затримка на 30 хвилин

    # Закриття підключення (цей код ніколи не виконається в силу безкінечного циклу)
    conn.close()

if __name__ == "__main__":
    update_temperature()