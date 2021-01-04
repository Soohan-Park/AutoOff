from threading import Timer
from time import sleep

THREAD_FLAG = True

def tictoc_start(status, timer):
  global THREAD_FLAG

  Timer(1, lambda: tictoc(status, timer)).start()


def tictoc(status, timer):
  global THREAD_FLAG

  while THREAD_FLAG:
    timer -= 1
    sleep(1)
    status['text'] = '{}분 {}초 남음'.format(timer//60, timer%60)
  
  THREAD_FLAG = True
  status['text'] = '자동 종료 취소'


def tictoc_stop():
  global THREAD_FLAG

  THREAD_FLAG = False