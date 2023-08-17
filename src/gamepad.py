from evdev import InputDevice, categorize, ecodes

gamepad= InputDevice('/dev/input/event4')
print(gamepad)

for event in gamepad.read_loop():
	print(categorize(event))
