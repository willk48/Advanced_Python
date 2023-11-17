class data_set:
    def __init__(self, file, lst=[]):
        self.file=file
        self.lst=lst
    
    def write_to(self, items, c=False):
        match c:
            case True:
                file1 = open(self.file, "w")
                file1.writelines(items)
                file1.close
            case False:
                file2 = open(self.file,"a")
                file2.writelines(items)
                file2.close
    
    def read_from(self, lst=[]):
        #file3=open(self.file,"r")
        #lst.append(file3.readlines())
        with open(self.file,"r") as str1:
            lst=str1.readlines()
        str1.close()
        return lst
    
if __name__ == '__main__':
    test=data_set("test_file.txt")
    work=['word\n','otherword\n','nextone\n','stillgoing\n','almost\n','last\n']
    test.write_to(work, True)
    print("Writing to an empty file:")
    print(test.read_from())
    test.write_to(work)
    print("Appending:")
    print(test.read_from())
    test.write_to(work, True)
    print("Clear and overwrite:")
    print(test.read_from())
