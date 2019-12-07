from Tkinter import *
from DWatchGUI import DWatchGUI

if __name__=="__main__":
  root = Tk()
  root.withdraw()
  topLevel = Toplevel(root)
  topLevel.resizable(width="NO", height="NO")
  topLevel.title("DWatch")
  DWatchGUI(topLevel,None)
  root.mainloop()
