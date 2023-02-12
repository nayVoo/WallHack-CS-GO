import pymem
import keyboard
#OFFSETS 
dwEntityList = () #--> dwEntityList offset
dwGlowObjectManager = () #--> dwGlowObjectManager offset
m_iGlowIndex = () #--> m_iGlowIndex offset

pm = pymem.Pymem('csgo.exe')
clientcatch = pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll

isclicker = False 

def set_clicker():
	global isclicker # global allows us to manage isclicker func even in other program
	if isclicker:
		isclicker = False
		print ('Wh on')
	else:
		isclicker = True
		print ('')
keyboard.add_hotkey ('Alt + Z', set_clicker) # Bind Alt + Z --> turn on, turn off WH (you can use any bund u want)

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
					pm.write_float(glow + entityglowing * 0x38 + 0xC, float(1)) # --> color (1 - green, 2- blue, 3 - red)
					pm.write_float(glow + entityglowing * 0x38 + 0x10, float(0))
					pm.write_float(glow + entityglowing * 0x38 + 0x14, float(1))
					pm.write_int(glow + entityglowing * 0x38 + 0x28, 1) # --> alpha
if __name__ == '__main__':
	main()
