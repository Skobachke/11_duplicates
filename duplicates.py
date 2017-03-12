import os

def are_files_duplicates(file_path1, file_path_2):
    if file_path1 != file_path_2:
        if os.path.split(file_path1)[1] == os.path.split(file_path_2)[1]:
            if os.path.getsize(file_path1) == os.path.getsize(file_path_2):
                return True

def file_tree(directory):
    path_list = []
    for i in os.walk(directory):
        for j in i[2]:
            path_list.append(os.path.join(str(i[0]), str(j)))
    return path_list

if __name__ == '__main__':
    directory = input('Введите путь к папке: ')
    equal = 0
    if directory:
        all_path_list = file_tree(directory)
        for i in range(len(all_path_list)-1):
            for j in range(i+1,len(all_path_list)):
                if are_files_duplicates(all_path_list[i], all_path_list[j]):
                    equal += 1
                    print('{}. Совпадение файла ({}) и ({})!'.format(equal, all_path_list[i], all_path_list[j]))
        if equal == 0:
            print ('Совпадения не найдены!')
    else:
        print('Введите путь!')