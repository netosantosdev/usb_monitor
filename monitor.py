import time
from usb_handler import USBWatcher
from file_logger import Logger

if __name__ == "__main__":
    logger = Logger()
    watcher = USBWatcher(logger)
    watcher.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        watcher.stop()