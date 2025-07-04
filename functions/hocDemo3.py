

def pdfHandler(fileName):
    print("pdf handler called..",fileName)
    

def ImageHandler(fileName):
    print("Image handler called..",fileName)
    
    

def txtHandler(fileName):
    print("txt handler called..",fileName)    



#call back
def filehandling(cb,fileName):
    print("file handling....")
    cb(fileName) #PDFhANDLERR()


file = "demo.pdf"

if(file.endswith(".txt")):
    filehandling(txtHandler,file)
elif file.endswith(".pdf"):
    filehandling(pdfHandler,file)    
