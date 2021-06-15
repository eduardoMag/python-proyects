import win32com.client as com

# set the file path as required on pc
filepath = r"C:\Users\story\Documents\playground\python-proyects\toolhire.xlsx"
fileopen = 1 #1 opens to search filename, 4 opens to search for folder name

app = com.Dispatch("Excel.Application")
app.Visible = True

fd = app.FileDialog(fileopen)
fd.InitialFileName = filepath
fd.Title = "Open the toolhire spreadsheet"

if fd.Show() == -1:
    fd.Execute()
