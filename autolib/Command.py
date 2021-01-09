from . import Thread as th

import os


def grider(target, _row, _col):
  target.grid(row=_row, column=_col)


def start(status, time, timer):
  if time.isnumeric():
    os.system('shutdown -s -f -t {}'.format(time))
    timer = int(time)
    th.tictoc_start(status, timer)
  else:
    __chSts(status, '올바른 시간을 입력해주세요!', 'red')


def stop(status, timer):
  os.system('shutdown -a')
  th.tictoc_stop()
  # __chSts(status, '자동 종료 취소') -> Thread에서 처리


# Private Func.
def __chSts(status, msg, fg='black'):
  status['text'] = msg
  status['fg'] = fg