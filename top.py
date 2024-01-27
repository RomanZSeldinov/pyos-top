import psutil
import time
import os

def print_processes():
    # Получение списка процессов
    processes = psutil.process_iter(['pid', 'name', 'cpu_percent'])

    # Очистка консоли
    os.system('cls' if os.name == 'nt' else 'clear')

    # Вывод заголовка
    print(f'{"PID":<10} {"NAME":<25} {"CPU %":<10}')

    # Вывод информации о процессах
    for process in processes:
        print(f'{process.info["pid"]:<10} {process.info["name"]:<25} {process.info["cpu_percent"]:<10.2f}')

print_processes()
while True:
    if (input() == "u"):
        print_processes()
    
