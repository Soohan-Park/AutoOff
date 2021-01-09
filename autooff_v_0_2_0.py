import autolib.Component as comp
import autolib.Command as comm

import tkinter as tk


class AutoOff(tk.Frame):
  master = None
  timer = None
  
  labelInput = None
  labelRestTime = None

  entryInput = None

  textStatus = None

  btnStart = None
  btnStop = None
  btnExit = None


  def __init__(self, master=tk.Tk()):
    super().__init__(master)
    self.master = master

    # Setting
    self.master.geometry('300x100')
    self.master.title('AUTO OFF (ver. {}'.format(__name__[-5:].replace('_', '.')))

    # Set Components
    self.setComponents()

    # Grid
    self.setGrid()
  
  def setComponents(self):
    self.labelInput = comp.label(self.master, '시간 설정')
    self.labelRestTime = comp.label(self.master, '남은 시간')

    self.entryInput = comp.entry(self.master)

    self.textStatus = comp.label(self.master, '시간을 설정해주세요!')

    self.btnStart = comp.button(self.master, 'Start', 'green', lambda: comm.start(self.textStatus, self.entryInput.get(), self.timer))
    self.btnStop = comp.button(self.master, 'Stop', 'red', lambda: comm.stop(self.textStatus, self.timer))
    self.btnExit = comp.button(self.master, 'Exit', 'blue', self.master.destroy)
  
  def setGrid(self):
    comm.grider(self.labelInput, 0, 0)
    comm.grider(self.labelRestTime, 1, 0)
    
    comm.grider(self.entryInput, 0, 1)

    comm.grider(self.textStatus, 1, 1)

    comm.grider(self.btnStart, 2, 0)
    comm.grider(self.btnStop, 2, 1)
    comm.grider(self.btnExit, 2, 2)