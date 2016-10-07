# from http://blog.yhat.com/posts/11-python-libraries-you-might-not-know.html
# Note: this script requires progressbar 2.2
from progressbar import ProgressBar
import time
pbar = ProgressBar(maxval=10)
for i in range(1, 11):
    pbar.update(i)
    time.sleep(0.5)
pbar.finish()
