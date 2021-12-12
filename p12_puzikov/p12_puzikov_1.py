dirs = [
    ( 'folder1',
        [
            'file1',
            ( 'folder2', 
                [
                    'file2',
                    'file3'
                ] 
            ),
            ( 'folder3', 
                [
                    'file3', 
                    'file4',
                    ('folder4', ['file3'])
                ] 
            ),
            'file5'
        ]
    )
]

# ВАШ КОД ТУТ

cur_path = ['']

def search(cur_dir : [], name : str):
  global cur_path
  if(cur_path[0] == ''):
    cur_path = ['']
  for dir in cur_dir:
    if(isinstance(dir,str)):
      if(dir == name):
        cur_path.append(cur_path[0]+'/'+name)
    else:
      cur_path[0] += '/'
      if(cur_path[0] != '/'):
        cur_path[0] += '/'
      cur_path[0] += dir[0]
      search(dir[1],name)
      while(len(cur_path[0]) > 0 and cur_path[0][len(cur_path[0])-1] != '/'):
        cur_path[0] = cur_path[0][:-1]
      while(len(cur_path[0]) > 0 and cur_path[0][len(cur_path[0])-1] == '/'):
        cur_path[0] = cur_path[0][:-1]
      
  return cur_path[1::1]

# ПЕРЕВІРКА
#print('???')

print(search(dirs, 'file1'))
print(search(dirs, 'file2'))
print(search(dirs, 'file3'))
print(search(dirs, 'file4'))
print(search(dirs, 'file5'))
print(search(dirs, 'file6'))
print(search(dirs, 'folder1'))

assert search(dirs, 'file1') == ['/folder1/file1'], 'Failed test for file1'
assert search(dirs, 'file2') == ['/folder1//folder2/file2'], 'Failed test for file2'
assert search(dirs, 'file3') == ['/folder1//folder2/file3', '/folder1//folder3/file3', '/folder1//folder3//folder4/file3'], 'Failed test for file3'
assert search(dirs, 'file4') == ['/folder1//folder3/file4'], 'Failed test for file4'
assert search(dirs, 'file5') == ['/folder1/file5'], 'Failed test for file5'
assert search(dirs, 'file6') == [], 'Failed test for file6'
assert search(dirs, 'folder1') == [], 'Failed test for folder1'
print('All tests good!')