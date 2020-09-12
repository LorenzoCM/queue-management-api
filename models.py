from flask_sqlalchemy import SQLAlchemy
from twilio.rest import Client
db = SQLAlchemy()

class Queue:

    def __init__(self):
        self._queue = [{
            "name": "Hello",
            "phone": "+56951231650"
        }]
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        self._mode = 'FIFO'
        self.account_sid = "AC9907bdc4f5d736096af4306c58db7586"
        self.auth_token = "13236848ff64db96fa4aa2dff5ea81d5"
        self.client = Client(self.account_sid, self.auth_token)

    def enqueue(self, item):
        queue_size = len(self._queue)
        self._queue.append(item)
        message = "You are now in the queue, there are {} people before you".format(queue_size)
        self.sendMessage(item["phone"], message)        
        
    def dequeue(self):
        if len(self._queue) > 0:
            item = None
            if self._mode == 'FIFO':
                item = self._queue.pop(0)
            else:
                item = self._queue.pop()
            message = "Thanks for waiting  {}! it is your turn now".format(item["name"])
            self.sendMessage(item["phone"], message)
            return True        
        else:
            return False

    def get_queue(self):
        return self._queue

    def size(self):
        return len(self._queue)

    def sendMessage(self, phone, body):
        print(phone, body)
        self.client.messages.create(
            to = phone,
            from_ = "+12144270027",
            body = body
        ) 