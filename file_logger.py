import os
from datetime import datetime

class Logger:
    def __init__(self, log_dir="C:\\ProgramData\\USBMonitorService"):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

    def get_log_path(self):
        now = datetime.now()
        filename = now.strftime("%Y-%m") + "-USBLog.csv"
        return os.path.join(self.log_dir, filename)

    def log_event(self, action, detail):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.get_log_path(), "a", encoding="utf-8") as f:
            f.write(f"{now},{action},{detail}\n")