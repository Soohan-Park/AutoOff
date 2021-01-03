import tkinter as tk
import os
import threading


class AutoOff(tk.Frame):
  TIME = None
  TIMER = None

  def __init__(self, master=tk.Tk()):
    super().__init__(master)
    self.master = master

    # Setting
    self.master.geometry('300x100')
    self.pack()

    #Set Component
    self.timeBox()
    self.restTimeBox()
    self.startBtn()
    self.stopBtn()
    self.programOff()

  # Components
  def timeBox(self):
    self.labelSetTime = tk.Label(self, text='n초 뒤 종료')
    self.time = tk.Entry(
      self,
      textvariable=str
    )

    self.labelSetTime.grid(row=0, column=0)
    self.time.grid(row=0, column=1)
  
  def restTimeBox(self):
    self.labelRestTime = tk.Label(self, text='남은 시간: ')
    self.restTime = tk.Label(self, text='{}초 남음'.format(self.TIME))

    self.labelRestTime.grid(row=1, column=0)
    self.restTime.grid(row=1, column=1)
  
  def startBtn(self):
    self.start = tk.Button(
      self,
      text='Start',
      fg='green',
      command=self.start
    )

    self.start.grid(row=2, column=0)
  
  def stopBtn(self):
    self.stop = tk.Button(
      self,
      text='Stop',
      fg='red',
      command=self.stop
    )

    self.stop.grid(row=2, column=1)
  
  def programOff(self):
    self.quit = tk.Button(
      self,
      text='Exit',
      fg='blue',
      command=self.master.destroy
    )

    self.quit.grid(row=2, column=2)
  

  # Logics
  def start(self):
    if self.checkTime(self.time.get()):
      seconds = self.time.get()

      if any(seconds):
        os.system('shutdown -s -f -t {}'.format(seconds))
        self.TIME = int(seconds)
        self.timer()
      else:
        self.setRestTime('올바른 시간을 입력해주세요!', 'red')
  
  def stop(self):
    os.system('shutdown -a')
    self.setRestTime('자동 종료 취소')
    self.TIME = -1
  
  
  # Functions
  def setRestTime(self, msg, fg='black'):
    self.restTime['text'] = msg
    self.restTime['fg'] = fg
  
  def checkTime(self, _time):
    return True if _time.isnumeric() else False
  

  # Threading
  def timer(self):
    self.TIME -= 1
    if self.TIME > 0:
      self.setRestTime('{}초 남음'.format(self.TIME))
      self.TIMER = threading.Timer(1, self.timer).start()