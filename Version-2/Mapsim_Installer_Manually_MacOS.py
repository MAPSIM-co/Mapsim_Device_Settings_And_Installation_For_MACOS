import os
import subprocess
import sys
import platform
from dotenv import load_dotenv  

load_dotenv()

github_url = "https://github.com/Mpouransari/Mapsim_Device.git"  
download_path = "/Users/mpouransari/Downloads/Mapsim_Device"  
bash_file_path = os.path.expanduser("~/Desktop/run_program.sh")  

g_t = os.getenv("GT")  

if not g_t:
    print("GitHub token not found. Please ensure that the .env file is correctly set.")
    sys.exit(1)

def install_python():
    try:
        subprocess.run(["python3", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Python is already installed.")
    except subprocess.CalledProcessError:
        print("Python is not installed. Installing Python...")
        if platform.system() == "Darwin":
            subprocess.run(["brew", "install", "python"], check=True)
            print("Python has been successfully installed.")
        else:
            print("This script only works on macOS.")
            sys.exit(1)

def download_code():
    print(f"Downloading the source code from {github_url}...")
    
    auth_url = github_url.replace("https://", f"https://{g_t}@")
    subprocess.run(["git", "clone", auth_url, download_path], check=True)
    print(f"Code has been successfully downloaded to {download_path}.")


def create_bash_file():
    bash_content = f"""
    #!/bin/bash
    python3 {download_path}/Mapsim_Device_Assistance_Bot.py
    """
    with open(bash_file_path, 'w') as bash_file:
        bash_file.write(bash_content)
    print(f"Bash file has been created on the Desktop at {bash_file_path}.")
    

def install():
    install_python()  
    download_code()   
    create_bash_file()  
    print("Installation completed successfully. You can now run the program by clicking on the bash file.")
    
    print(f"Giving executable permissions to the bash file at: {bash_file_path}")
    subprocess.run(["chmod", "+x", bash_file_path], check=True)
    # subprocess.run(["/bin/bash", bash_file_path], check=True)

if __name__ == "__main__":
    install()
