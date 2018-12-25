import sys
_RECURSION_LIMIT = 2000

if ( sys.getrecursionlimit() < _RECURSION_LIMIT ) :
  print('System recursion limit was {0}, setting to {1}.'.format(sys.getrecursionlimit(),_RECURSION_LIMIT) )
  sys.setrecursionlimit( _RECURSION_LIMIT )

#----------------------------------------------------------------------
import Tkinter as tk
import tkMessageBox
import widgets
import graphics

#----------------------------------------------------------------------
def onClosing() :
    # if tk.messagebox.askokcancel( "Really Quit?", "Do you really wish to quit?" ) :
    if tkMessageBox.askyesno("Really Quit?", "Do you really wish to quit?" ) :
        tk.Tk().quit()

#----------------------------------------------------------------------
def main() :
  ob_root_window = tk.Tk()
  ob_root_window.protocol( "WM_DELETE_WINDOW", onClosing )

  ob_world = graphics.cl_world()

  widgets.cl_widgets( ob_root_window, ob_world )

  ob_root_window.mainloop()
  print( '... mainloop has exited.' )

if ( __name__ == "__main__" ) :
  main()