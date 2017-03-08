import os

def file_list(directory):
    global equal
    pathlist = []
    for i in os.walk(directory):
        for j in i[2]:
            pathlist.append(os.path.join(str(i[0]), str(j)))

    for i in range(len(pathlist)-1):
        for j in range(i+1,len(pathlist)):
            if pathlist[i] != pathlist[j]:
                are_files_duplicates(pathlist[i], pathlist[j])
    if equal == 0:
        print ('No matches found!')

def are_files_duplicates(file_path1, file_path_2):
    if (os.path.split(file_path1)[1] == os.path.split(file_path_2)[1]) and os.path.getsize(file_path1) == os.path.getsize(file_path_2):
        global equal
        equal += 1
        print ('{}. The match files  {} and {}!'.format(equal, file_path1, file_path_2))

if __name__ == '__main__':
    directory = input('Enter the path:')
    equal = 0
    file_list(directory)