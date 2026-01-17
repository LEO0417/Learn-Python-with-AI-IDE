# timer_v2.py
# 这个脚本是经过“意图纠偏”后生成的“正确”示例
# 它使用了 time.sleep(1) 来实现每秒停顿

import time

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)  # 这一行就是实现“停顿 1 秒”的关键

print("Time's up!")
