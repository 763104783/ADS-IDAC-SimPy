# # -*- coding: utf-8 -*-
# import time

# def get_time():
#     time_str = time.strftime("%Y{}%m{}%d{} %X")
#     return time_str.format("年", "月", "日")


# if __name__ == "__main__":
#     print(get_time())
import base64
with open('./static/res/ship1.png', 'rb') as f:
    # f.read()
    # print(f.read())
    b64 = base64.b64encode(f.read())
    print(type(b64))