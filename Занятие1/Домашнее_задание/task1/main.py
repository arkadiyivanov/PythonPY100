speed = 4096  # скорость передачи данных в байтах/cек
time = 120  # время в минутах затраченное на скачивание игры
cost = 5  # стоимость за один мегабайт


speed_in_mb_in_sec = speed / (1024 * 1024)
time_in_sec = time * 60

free_traffic = 10  # количество бесплатного трафика
file_size = time_in_sec * speed_in_mb_in_sec  # размер файла
total_coast = (file_size - free_traffic) * cost  # стоимость файла

print(f'Размер файла в мегабайтах =', file_size)
print(f'За трафик придется заплатить:', total_coast)
