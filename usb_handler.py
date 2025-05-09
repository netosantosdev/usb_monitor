import psutil
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

class FileEventHandler(FileSystemEventHandler):
    def __init__(self, logger, mount_point):
        self.logger = logger
        self.mount_point = mount_point

    def on_created(self, event):
        self.logger.log_event("Arquivo criado", event.src_path)

    def on_modified(self, event):
        self.logger.log_event("Arquivo modificado", event.src_path)

    def on_deleted(self, event):
        self.logger.log_event("Arquivo deletado", event.src_path)

class USBWatcher:
    def __init__(self, logger):
        self.logger = logger
        self.running = True
        self.observers = {}
        self.monitored_drives = set()
        self.scan_interval = 3  # segundos

    def detect_mount_points(self):
        devices = []
        for part in psutil.disk_partitions():
            if 'removable' in part.opts and part.mountpoint:
                devices.append(part.mountpoint)
        return devices

    def start_file_watcher(self, mount):
        if mount in self.monitored_drives:
            return
        event_handler = FileEventHandler(self.logger, mount)
        observer = Observer()
        observer.schedule(event_handler, mount, recursive=True)
        observer.start()
        self.observers[mount] = observer
        self.monitored_drives.add(mount)
        self.logger.log_event("Monitoramento iniciado em", mount)

    def scan_loop(self):
        while self.running:
            try:
                current = set(self.detect_mount_points())
                new_mounts = current - self.monitored_drives
                for mount in new_mounts:
                    self.start_file_watcher(mount)
            except Exception as e:
                self.logger.log_event("Erro na varredura de dispositivos", str(e))
            time.sleep(self.scan_interval)

    def start(self):
        self.thread = threading.Thread(target=self.scan_loop, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False
        for observer in self.observers.values():
            observer.stop()
            observer.join()
