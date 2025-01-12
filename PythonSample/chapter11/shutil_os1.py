import shutil
import os
shutil.copy('message.txt', 'message2.txt')
os.rename('message2.txt', 'message3.txt')
os.remove('message3.txt')
