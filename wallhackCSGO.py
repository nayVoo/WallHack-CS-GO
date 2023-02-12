import pymem
import keyboard

dwEntityList = 0x4DFFF04
dwGlowObjectManager = 0x535A9D8
m_iGlowIndex = 0x10488

pm = pymem.Pymem('csgo.exe')
clientcatch = pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll

isclicker = False

def set_clicker():
	global isclicker
	if isclicker:
		isclicker = False
		print ('Wh on')
	else:
		isclicker = True
		print ('Wh off')
keyboard.add_hotkey ('Alt + Z', set_clicker)

def main():
	while True:
		if isclicker:
			None

		else:
			
			if keyboard.is_pressed('end'):
				exit (0)
			glow = pm.read_int(clientcatch + dwGlowObjectManager)

			for i in range(0, 32):
				entity = pm.read_int(clientcatch + dwEntityList + i *0x10)
				if entity:
					entityglowing = pm.read_int(entity+m_iGlowIndex)

					pm.write_float(glow + entityglowing * 0x38 + 0x8, float(0))
					pm.write_float(glow + entityglowing * 0x38 + 0xC, float(1))
					pm.write_float(glow + entityglowing * 0x38 + 0x10, float(0))
					pm.write_float(glow + entityglowing * 0x38 + 0x14, float(1))
					pm.write_int(glow + entityglowing * 0x38 + 0x28, 1)
if __name__ == '__main__':
	main()
