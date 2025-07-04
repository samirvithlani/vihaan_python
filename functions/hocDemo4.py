

def pdfHandler(fileName):
    print("pdf handler called..",fileName)
    return "PDF open successfully"
    

def ImageHandler(fileName):
    print("Image handler called..",fileName)
    return "Image open successfully"
    
    

def txtHandler(fileName):
    print("txt handler called..",fileName)    
    return "TXT open successfully"



#call back
def filehandling(cb,fileName):
    print("file handling....")
    flag = cb(fileName) #PDFhANDLERR()
    print(flag)


file = "demo.pdf"

if(file.endswith(".txt")):
    filehandling(txtHandler,file)
elif file.endswith(".pdf"):
    filehandling(pdfHandler,file)    
