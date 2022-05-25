# python cp file
with open('text.txt', 'r') as rf:
  with open('copy_text.txt', 'w') as wf:
    for line in rf:
      wf.write(line)

# python cp binary
with open('test.png', 'rb') as rf:
  with open('copy_test.png', 'wb') as wf:
    for line in rf:
      wf.write(line)

# python cp binary 2
with open('photo1.jpg', 'rb') as rf:
  with open('copy_photo1.jpg', 'wb') as wf:
    chunk_size = 4096
    rf_chunk = rf.read(chunk_size)
    while len(rf_chunk) > 0:
      wf.write(rf_chunk)
      rf_chunk = rf.read(chunk_size)
