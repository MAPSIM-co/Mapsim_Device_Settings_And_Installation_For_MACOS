import os
import subprocess
import sys
import platform
from dotenv import load_dotenv  # برای بارگذاری متغیرهای محیطی از فایل .env

# بارگذاری متغیرهای محیطی از فایل .env
load_dotenv()

# تنظیمات
github_url = "https://github.com/Mpouransari/Mapsim_Device.git"  # لینک به سورس کد در GitHub
download_path = "/Users/mpouransari/Downloads/Mapsim_Device"  # مسیر برای دانلود سورس کد (در macOS)
bash_file_path = os.path.expanduser("~/Desktop/run_program.sh")  # مسیر برای ذخیره فایل شل در دسکتاپ کاربر

# دریافت توکن از فایل .env
github_token = os.getenv("GITHUB_TOKEN")  # خواندن توکن از فایل .env

if not github_token:
    print("توکن GitHub یافت نشد. لطفاً مطمئن شوید که فایل .env به درستی تنظیم شده است.")
    sys.exit(1)

# نصب Python اگر نصب نشده باشد
def install_python():
    # چک کردن اینکه Python نصب است یا نه
    try:
        subprocess.run(["python3", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Python قبلاً نصب شده است.")
    except subprocess.CalledProcessError:
        print("Python نصب نشده است. در حال نصب Python ...")
        if platform.system() == "Darwin":
            # نصب Python با استفاده از Homebrew
            subprocess.run(["brew", "install", "python"], check=True)
            print("Python با موفقیت نصب شد.")
        else:
            print("این اسکریپت فقط در macOS کار می‌کند.")
            sys.exit(1)

# دانلود سورس کد از GitHub
def download_code():
    print(f"در حال دانلود سورس کد از {github_url} ...")
    # از Git برای دانلود سورس کد استفاده می‌کنیم و توکن را در URL گیت‌هاب وارد می‌کنیم
    auth_url = github_url.replace("https://", f"https://{github_token}@")
    subprocess.run(["git", "clone", auth_url, download_path], check=True)
    print(f"کد با موفقیت در {download_path} دانلود شد.")

# ایجاد فایل شل
def create_bash_file():
    bash_content = f"""
    #!/bin/bash
    python3 {download_path}/Mapsim_Device_Assistance_Bot.py
    """
    with open(bash_file_path, 'w') as bash_file:
        bash_file.write(bash_content)
    print(f"فایل شل در دسکتاپ با مسیر {bash_file_path} ایجاد شد.")
    
    

# اجرای مراحل نصب
def install():
    install_python()  # نصب Python اگر نیاز باشد
    download_code()   # دانلود سورس کد
    create_bash_file()  # ایجاد فایل شل
    print("نصب با موفقیت انجام شد. اکنون می‌توانید با کلیک بر روی فایل شل برنامه را اجرا کنید.")
    
    # اعطای مجوز اجرایی به فایل
    print(f"اعطای مجوز اجرایی به فایل شل از مسیر: {bash_file_path}")
    subprocess.run(["chmod", "+x", bash_file_path], check=True)
    
    # اجرای خودکار فایل شل پس از نصب
    #print(f"در حال اجرای فایل شل از مسیر: {bash_file_path}")
    #subprocess.run(["/bin/bash", bash_file_path], check=True)


if __name__ == "__main__":
    install()