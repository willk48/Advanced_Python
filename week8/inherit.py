from read_write_file import data_set

class data_set_dirty(data_set):
    def __init__(self, file, lst=[]):
        data_set.__init__(self,file,lst)
        self.d=False
    #adding functionality of dirty vs clean file
    #dirty files will be ovewritten and clean files will be appended
    #imagining a case where sometimes we want to treat the file as a placeholder for active values
    #sometimes, but also retain the option to keep appending if the process is not over
    #adds the ability for each function later to either keep the list or overwrite
    def write_to(self,items):
        if self.d==False:
            file2 = open(self.file,"a")
            file2.writelines(items)
            file2.close
        else:
            file1 = open(self.file, "w")
            file1.writelines(items)
            file1.close
    def read_from(self, lst=[]):
        return super().read_from()
    

if __name__ == '__main__':
    work=['word\n','otherword\n','nextone\n','stillgoing\n','almost\n','last\n']
    testing=data_set_dirty("test_inherit.txt")
    testing.write_to(work)
    testing.write_to(work)
    print("Should have 2 copies of eveything before setting it to dirty:")
    print(testing.read_from())
    testing.d=True
    testing.write_to(work)
    print("Should now only have 1 copy:")
    print(testing.read_from())