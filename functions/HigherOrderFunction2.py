

def pdfHandler():
    print("pdf handler called..")
    

def ImageHandler():
    print("Image handler called..")
    
    

def txtHandler():
    print("txt handler called..")    



#call back
def filehandling(cb):
    print("file handling....")
    cb()


file = "demo.pdf"

if(file.endswith(".txt")):
    filehandling(txtHandler)
elif file.endswith(".pdf"):
    filehandling(pdfHandler)    
