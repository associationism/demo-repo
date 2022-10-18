
filename = input("Adjon meg egy fájlnevet: ")

files = {
    "txt" : 'ASCII text file.',
	"doc" : 'Microsoft Word Document',
	"xlsx" : 'Microsoft Excel Document',
	"exe" : 'Windows x86 Executable',
	"zip" : 'File Archive'
}

try:
    data = filename.split('.')
    key = data[-1]
    print(f'Az ön által megadott fájl típusa: {files[key]}')
except:
    print('Ismeretlen fájltípus.')

