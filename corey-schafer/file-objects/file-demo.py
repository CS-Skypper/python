## not the reccomanded way
# f = open('text.txt', 'r')
# print(f.mode, f.name, f.closed)
# f.close()
## ------

# context manager
with open('text2.txt', 'w') as fi: # entering a file that does not exist as 'w' will create that file, empty; if file exists it will overwrite it. don't want to? just append to the end of file with 'a'
  fi.write('Test')
  fi.seek(0) # set the position back to 0,
  fi.write('R')



with open('text.txt', 'r') as f:
  
  
  # read 100 characters from the file
  size_to_read = 10

  f_contents = f.read(size_to_read)
  print(f_contents, end='')
  f_contents = f.read(size_to_read)
  print(f.tell()) # shows the current position in the file

  f.seek(0) # starts reading again from position 0 of the file

  print(f_contents)
  print(f.tell()) # shows the current position in the file


  # while len(f_contents) > 0: # because .read() return empty string when it reached the end of file
  #   print(f_contents, end='|')
  #   f_contents = f.read(size_to_read)
  # print(f_contents, end='')


  ## pro user, memory efficient
  # for line in f:
  #   print(line, end='')


#  print(f.mode, f.name, f.closed)
#  # f_contents = f.read()
#  f_contents = f.readline()
#  print(f_contents, end='')
#  f_contents = f.readline()
#  print(f_contents, end='')
#  f_contents = f.readlines()
#  print(f_contents)

# print(f_contents) # f_contents it is available from outside the context manager
# print(f.mode, f.name, f.closed)

