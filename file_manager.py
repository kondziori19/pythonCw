class Filemanager:

    def __init__(self,file_name):
        self.file_name = file_name

    def readfile(self):
        with open(self.file_name) as f:
            print(f.readlines())

    def updatefile(self, tekst):
        file_object = open(self.file_name, 'a')
        file_object.write(tekst)
        file_object.close()