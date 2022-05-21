### 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности
# duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры:

# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек
duration = int(input("Введите количество секунд: "))
if duration < 60:
    print(str(duration) + "сек")
elif duration < 60 * 60:
    print(str(duration // 60) + (" мин.") + str(duration % 60) + (" сек."))
elif duration < 24 * 60 * 60:
    print(str(duration // 3600) + " ч." + str(duration % 3600 // 60) + " мин." + str(duration % 60) + " сек.")
else:
    print(str(duration // 86400) + " д " + str(duration % 86400 // 3600) + " ч." +
          str(duration % (24 * 3600) % 3600 // 60) + " мин." + str(duration % 60) + " сек.")
