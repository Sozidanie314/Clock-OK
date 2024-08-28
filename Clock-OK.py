import time
import threading
import pygame
from plyer import notification

def format_time(seconds):
    # Форматирование времени в часы, минуты и секунды
    hrs, secs = divmod(seconds, 3600)
    mins, secs = divmod(secs, 60)
    return f"{hrs:02}:{mins:02}:{secs:02}"

def countdown_timer(hours, minutes, seconds):
    # Конвертируем время в секунды
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    while total_seconds > 0:
        # Форматирование и вывод оставшегося времени
        time_left = format_time(total_seconds)
        print(f"Осталось: {time_left}", end='\r')
        time.sleep(1)
        total_seconds -= 1
    
    print("\nВремя истекло!")
    print(f'Описание таймера: {notes}')
    pygame.mixer.init()
    pygame.mixer.music.load(r"D:\Progs\Vcode\VSCode-Projects\TTimer\iphone-song.mp3") # В эти ковычки нужно добавить адресную строку и название .mp3 файла
    pygame.mixer.music.play(loops=-1)  # loops=-1 заставляет повторять аудио - бесконечно.
    
    notification_title = "Таймер завершен"
    notification_message = f"Описание таймера: {notes}"
    notification.notify(
        title=notification_title,
        message=notification_message,
        timeout=15  # Продолжительность показа уведомления в секундах
    )

    wait_for_ok()

def wait_for_ok():
    while True:
        user_input = input("Введите 'ок/ok' для завершения: ")
        if user_input.strip().lower() == 'ок' or user_input.strip().lower() == 'ok':
            pygame.mixer.music.stop()
            print("Таймер завершен.")
            break

if __name__ == "__main__":
    hours = int(input("ЧЧ: "))
    minutes = int(input("ММ: "))
    seconds = int(input("СС: "))
    notes = input("Описание таймера: ")
    
    timer_thread = threading.Thread(target=countdown_timer, args=(hours, minutes, seconds))
    timer_thread.start()
