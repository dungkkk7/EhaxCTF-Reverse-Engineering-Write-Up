import os
import sys
import ctypes

# Xác định đường dẫn đến file moves.dll
if getattr(sys, 'frozen', False):
    BASE_PATH = sys._MEIPASS
else:
    BASE_PATH = os.path.dirname(__file__)
dll_path = os.path.join(BASE_PATH, r'C:\Users\dungv\Downloads\math-moves.exe_extracted\moves.dll')

# Load file DLL
movement = ctypes.CDLL(dll_path)
movement.move_up.restype = ctypes.c_double
movement.move_down.restype = ctypes.c_double
movement.move_left.restype = ctypes.c_double
movement.move_right.restype = ctypes.c_double

# Hàm giải mã giá trị
def deobfuscate(value):
    return round(value / 42, 4)

# Tính toán các giá trị
UP_VALUE = deobfuscate(movement.move_up())
DOWN_VALUE = deobfuscate(movement.move_down())
LEFT_VALUE = deobfuscate(movement.move_left())
RIGHT_VALUE = deobfuscate(movement.move_right())

# In ra các giá trị
print("UP_VALUE:", UP_VALUE)
print("DOWN_VALUE:", DOWN_VALUE)
print("LEFT_VALUE:", LEFT_VALUE)
print("RIGHT_VALUE:", RIGHT_VALUE)