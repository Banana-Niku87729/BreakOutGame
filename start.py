#!/usr/bin/env python3

import os
import subprocess

# 仮想環境のPythonインタプリタのパス
venv_python = os.path.join(os.path.dirname(__file__), 'venv', 'bin', 'python3')

# 実行するPythonスクリプトのパス
script_path = os.path.join(os.path.dirname(__file__), 'blockout.py')

# ログファイルのパス
log_file = os.path.join(os.path.dirname(__file__), 'execution.log')

# ファイルの存在確認
if not os.path.isfile(venv_python):
    raise FileNotFoundError(f"The virtual environment Python interpreter does not exist: {venv_python}")

if not os.path.isfile(script_path):
    raise FileNotFoundError(f"The script file does not exist: {script_path}")

# 仮想環境内でPythonスクリプトを実行
try:
    with open(log_file, 'w') as f:
        result = subprocess.run([venv_python, script_path], stdout=f, stderr=subprocess.STDOUT)
        if result.returncode != 0:
            print(f"Script failed with return code {result.returncode}. Check the log file for details.")
        else:
            print("Script executed successfully.")
except Exception as e:
    print(f"An error occurred: {e}")