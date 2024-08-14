import time
import sys

log_file_path = '/var/log/my_python_app.log'

sys.stdout = open(log_file_path, 'a')
sys.stderr = open(log_file_path, 'a')

while True:
    print("I'm alive")
    time.sleep(5)
