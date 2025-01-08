import pyautogui as pygui
import pyperclip as pyclip
import pynput
import time

# while True:
# 	print(pygui.position())

temp_pos = None
search_pos = (1555, 186)
copy_begin_pos = (1470, 263)
copy_end_pos = (1875, 968)
terminal_pos = (334, 978)

def on_click(x, y, button, pressed):
	if pressed:
		global temp_pos
		temp_pos = (x, y)
		print(f'Mouse clicked at ({x}, {y}) with {button}')
		return False

# with pynput.mouse.Listener(on_click=on_click) as listener:
# 	listener.join()
# 	search_pos = temp_pos
# with pynput.mouse.Listener(on_click=on_click) as listener:
# 	listener.join()
# 	copy_begin_pos = temp_pos
# with pynput.mouse.Listener(on_click=on_click) as listener:
# 	listener.join()
# 	copy_end_pos = temp_pos

# print(search_pos, copy_begin_pos, copy_end_pos)
# input('Press enter to continue...')

# pygui.moveTo(search_pos, duration=1)

def print_char(single_char):
    pyclip.copy(single_char)
    pygui.hotkey('ctrl', 'v')

file_name = 'input.txt'
text_res = ''
with open(file_name, 'r', encoding='utf-8') as file_obj:
	for single_line in file_obj:
		for single_char in single_line:
			print('\033[31m【' + single_char + '】\033[0m')

			pygui.click(search_pos)
			pygui.hotkey('backspace')

			pygui.click(search_pos)
			print_char(single_char)
			pygui.press('enter')
			time.sleep(1)
			
			pygui.moveTo(copy_begin_pos)
			pygui.dragTo(copy_end_pos, duration=0.2)
			pygui.hotkey('ctrl', 'c')
			clip_content = pyclip.paste()

			clip_parts = clip_content.split('\r\n\r\n')
			clip_cnt = 0
			for single_part in clip_parts:
				if not len(single_part):
					continue

				clip_cnt += 1
				print(f'\033[36mPart {clip_cnt}:\033[0m')

				# single_part = u'【' + single_part
				single_part = single_part.replace(single_char, '\033[93m' + single_char + '\033[0m')
				print(single_part)

				if clip_cnt == 5:
					break

			pygui.click(search_pos)
			pygui.hotkey('backspace')
			pygui.click(terminal_pos)
			
			while True:
				save_part = int(input('Save part id: '))
				if save_part < 1 or save_part > clip_cnt:
					print('Such id doesn\'t exist.')
				else:
					break

			single_part = clip_parts[save_part - 1]
			# text_res = text_res + u'【' + single_part.replace(single_char, '\033[93m' + single_char + '\033[0m')
			text_res = text_res + single_part.replace(single_char, '\033[93m' + single_char + '\033[0m') + '\n\n'

print(f'\033[104m------RESULT------\033[0m')
print(text_res)