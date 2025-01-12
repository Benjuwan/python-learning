import glob
import time
old = set(glob.glob('*'))
while True:
    time.sleep(3)
    new = set(glob.glob('*'))
    if added := new-old:
        print('Added  :', ' '.join(added))
    if removed := old-new:
        print('Removed:', ' '.join(removed))
    old = new
