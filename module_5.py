sec = int(input("Введите время в секундах:"))
minute = sec // 60
hour = minute // 60
secund = sec % 60
if sec < 60:
    print("00:00:%02d" % (secund))
elif minute < 60:
    print("00:%02d:%02d" % (minute,secund))
else:
    minute = minute % 60;
print("%02d:%02d:%02d" % (hour,minute,secund))