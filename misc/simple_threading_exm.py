"""
Simple threading example to recognize key presses, input presses in an async
fashion while the main program is still running.
"""
import threading

class KeyThread(threading.Thread):
    def __init__(self, input_cbk=None, name='keyboard-input-thread'):
        self.input_cbk = input_cbk
        super(KeyThread, self).__init__(name=name)
        self.start()
    
    def run(self):
        while True:
            self.input_cbk(input())


counter = 0

def my_cbk(inp):
    print("(%d) Echoing: %s" % (counter, inp))

kthrd = KeyThread(my_cbk)

while True:
    counter += 1
    