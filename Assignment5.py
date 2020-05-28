try:
    f = open("Rutvik.txt", "r")
except:
    print("Error while reading the file")
else:
    p = f.read()
    print(p)
    f.close()


while(1):
    try:
        name = input("Enter the file name")
        f = open(name, "r")
    except:
        print("File does not exist!!")
    else:
        print("Reading the file..")
        data = f.read()
        print(data)
        break
    finally:
        pass