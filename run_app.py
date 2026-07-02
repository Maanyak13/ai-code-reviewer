import os
import sys
import subprocess

def main():
    subprocess.run([
        sys.executable,
        "-m",
        "streamlit",
        "run",
        "app.py"
    ])

if __name__ == "__main__":
    main()
