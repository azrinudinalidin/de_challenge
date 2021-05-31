def main():
    
    #example text = '  abcde   abc123 12345 123.45   def456ghi   123abc456def   75.78  10101  20asde20  visit   malaysia2020    '

    txt = input('Enter text: ')
    print(txt)

    cariString(txt)

    file_name = input('Enter file name :')
    saveFile = open(file_name,'w')
    for i in f:
        saveFile.write(i)
        saveFile.write(',')
    saveFile.close()

def cariString(text):
    import re
    f = re.findall(r'\d*\.\d+|\s*\w*\s+',txt)
    print('f '+str(f))
    return

if __name__ == "__main__":
    main()
