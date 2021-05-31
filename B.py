def main():
    
    file_name = input('Enter file name :')

    readFile = open(file_name,'r')
    readlist = readFile.read()
    readFile.close()

    susun(readlist)

def susun(text):
    import re
    text = re.findall(r'\d*\.\d+|\w+',readlist)
    for items in text:   
        if items.isalpha():
            print(items +' - alphabetical string')
        elif items.isdigit():
            print(items +' - integer')
        elif items.isalnum():
            print(items +' - alphanumeric')
        elif items.replace('.','',1).isdigit():
            print(items +' - real numbers ')
    return

if __name__ == "__main__":
    main()
