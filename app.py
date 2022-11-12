import Eel
import os
from queue import Queue


class ChatBot:
    started = False
    userinputQueue = Queue()

    def isUserInput():
        return not ChatBot.userinputQueue.empty()

    def popUserInput():
        return ChatBot.userinputQueue.get()

    def close_callback(route, websockets):
        # if not websockets:
        #     print('Bye!')
        exit()

    @Eel.expose
    def getUserInput(msg):
        ChatBot.userinputQueue.put(msg)
        print(msg)

    def close():
        ChatBot.started = False

    def addUserMsg(msg):
        Eel.addUserMsg(msg)

    def addAppMsg(msg):
        Eel.addAppMsg(msg)

    def start():
        path = os.path.dirname(os.path.abspath(__file__))
        Eel.init(path + r'\web', allowed_extensions=['.js', '.html'])
        try:
            Eel.start('index.html', mode='chrome',
                      host='localhost',
                      port=27005,
                      block=False,
                      size=(350, 480),
                      position=(10, 100),
                      disable_cache=True,
                      close_callback=ChatBot.close_callback)
            ChatBot.started = True
            while ChatBot.started:
                try:
                    Eel.sleep(10.0)
                except:
                    # main thread exited
                    break

        except:
            pass