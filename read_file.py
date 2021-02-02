def read_file(file_path :str ) -> [str]:
    file = None
    try:
        file = open (file_path )
    except OSError:
        print(f"Errorrrr! Could not open file in path {file_path}")
    else:
        lines=[]
        for line in file:
            lines.append(line)
        return lines
    finally:
        if file != None:
            file.close()

text = read_file("myFile.txt")
if text!= None:
    print(text)