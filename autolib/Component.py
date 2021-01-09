import tkinter as tk

"""
LABEL
"""
def label(master, msg):
  return tk.Label(master, text=msg)


"""
ENTRY
"""
def entry(master):
  return tk.Entry(master, textvariable=str)


"""
BUTTON
"""
def button(master, msg, font_color, command):
  return tk.Button(master, text=msg, fg=font_color, command=command)
