import os

while True:
	print("+++ HDMI Control Center +++")
	print("1. Kolonowanie obrazu")
	print("2. Obraz rozszerzony")
	print("3. Wylaczenie ekranu")
	print("")
	check = int(input("Wybierz opcje: "))

	if check == 1:
		#os.system('xrandr --output eDP1 --mode 1366x768 --scale 1x1 --primary --output HDMI1 --same-as eDP1 --mode 1920x1080 --scale-from 1366x768')
		os.system('xrandr --output HDMI1 --off')
		os.system('xrandr --output HDMI1 --same-as eDP1 --auto --scale-from 1366x768')
	elif check == 2:
		#os.system('xrandr --output eDP1 --auto --output HDMI1 --auto --right-of eDP1')
		os.system('xrandr --output HDMI1 --off')
		os.system(' xrandr --output HDMI1 --right-of eDP1 --auto')
	elif check == 3:
		os.system('xrandr --output HDMI1 --off')
	else:
		break
