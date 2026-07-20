print('Ram Filler\n----------\n\nThis program will fill RAM in chunks.\n')
input('Enter to fill ram : ')
data = []
print('Filling ram...')
try:
    while True:
        data.append('0' * (50 * 1024 * 1024)) # 50 MB chunks
except MemoryError:
    print("Out of memory!")
