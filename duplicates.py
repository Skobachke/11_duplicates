import os

def are_files_duplicates(file_path1, file_path_2):
    if (os.path.split(file_path1)[1] == os.path.split(file_path_2)[1]) and os.path.getsize(file_path1) == os.path.getsize(file_path_2):
        print (u'Совпадение файлов {} и {}!'.format(file_path1, file_path_2))

if __name__ == '__main__':
    directory = '.'
    contdir, listdir = [], []

    for i in os.walk(directory):
        contdir.append(i)

    for i in contdir:
        for j in i[2]:
            listdir.append(os.path.join(str(i[0]), str(j)))

    for i in range(len(listdir)-1):
        for j in range(i+1,len(listdir)):
            if listdir[i] != listdir[j]:
                are_files_duplicates(listdir[i], listdir[j])