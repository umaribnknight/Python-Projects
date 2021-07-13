

import shutil
import os
import tkinter  


## User can check and select files

def check_files(self):
    result = []
    for path, subfolder, filename in os.walk(self.sourcePath):
        for i in filename:
            filepath = os.path.join(path, i)
            if os.path.getmtime(filepath) >= self.lastTrans or os.path.getctime(filepath) >= self.lastTrans:
                result.append(filepath)
    copy_files(self, result)


def copy_files(self, result):
    """Copies all files in result list to destPath folder.
    Args:
        An iterable series of paths.
    """    
    for filepath in result:
        shutil.copy(filepath, self.destPath)
    messagebox.showinfo(title="Success!", message="All files modified or created\nsince " + time.ctime(self.lastTrans) +
                                                  " in:\n" + self.sourcePath + "\nhave successfully been copied to:\n" +
                                                  self.destPath)
    update_db(self)
    refresh_label(self)

## file source and destination
def source_select(self):
    self.sourcePath = filedialog.askdirectory()
    self.sourceEntry.delete(0, END)
    self.sourceEntry.insert(0, self.sourcePath)
    

def dest_select(self):
    self.destPath = filedialog.askdirectory()
    self.destEntry.delete(0, END)
    self.destEntry.insert(0, self.destPath)

if __name__ == "__main__":
    pass
    
