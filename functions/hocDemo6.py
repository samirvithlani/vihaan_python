

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
    # flag = cb(fileName) #PDFhANDLERR()
    # print(flag)
    # return "file handled successfully.."
    return cb(fileName)


file = "demo.pdf"

ans = None

if(file.endswith(".txt")):
    ans = filehandling(txtHandler,file)
elif file.endswith(".pdf"):
    ans = filehandling(pdfHandler,file)    

print("ans",ans)    
