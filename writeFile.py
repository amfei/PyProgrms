def writeTextToFile(file_path:str, text:str)->int:
    file=None
    try:
        file=open(file_path,"w")
        return file.write(text)
    except OSError:
        print(f"Error! the file can't write in this path {file_path}")
    finally:
        if file!= None:
            file.close()

# Test program 
fileName="myFile.txt"
count= writeTextToFile(fileName,"Hello Amirrrrrr!")

if count != None:
    print(f"character {count} written to {fileName}")
else:
    print(f"Couldent write to {fileName}")


