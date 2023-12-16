import threading

import mock_queue
import email_notification

def startQueue():
    mock_queue.startMockQueue()

def startNotif():
    email_notification.startEmailNotif()

def start():
    try:
        # Create and start the thread that manages the queue
        queuethread = threading.Thread(target=startQueue, args=())
        queuethread.start()

        # Create and start the thread that manages emails
        notifthread = threading.Thread(target=startNotif, args=())
        notifthread.start()
    except Exception:
        sys.exit(1)

start()