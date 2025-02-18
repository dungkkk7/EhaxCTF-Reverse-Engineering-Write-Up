import time

def modify_score():
    while True: 
      time.sleep(0.04)  # Chờ đợi một khoảng thời gian ngắn
      with open(r'C:\Users\dungv\Downloads\score.txt', 'w') as f:
        f.write('-1')  # Ghi giá trị -1 vào file

# Chạy script này trong một terminal riêng
modify_score()