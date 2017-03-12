import os

def are_files_duplicates(file_path1, file_path_2):
    if file_path1 != file_path_2:
        if os.path.split(file_path1)[1] == os.path.split(file_path_2)[1]:
            if os.path.getsize(file_path1) == os.path.getsize(file_path_2):
                return True

if __name__ == '__main__':
    directory = input('Введите путь к папке: ')
    equal = 0
    pathlist = []
    if directory:
        for i in os.walk(directory):
            for j in i[2]:
                pathlist.append(os.path.join(str(i[0]), str(j)))
        for i in range(len(pathlist)-1):
            for j in range(i+1,len(pathlist)):
                if are_files_duplicates(pathlist[i], pathlist[j]):
                    equal += 1
                    print('{}. Совпадение файла ({}) и ({})!'.format(equal, pathlist[i], pathlist[j]))
        if equal == 0:
            print ('Совпадения не найдены!')
    else:
        print('Введите путь!')