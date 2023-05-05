def call_counter():
    import os

    if os.path.exists('count.txt'):
        with open('count.txt', 'r') as f:
            # count = int(f.read().strip())
            count = int(f.read())
        count += 1

        with open('count.txt', 'w') as f:
            f.write(str(count))
            print(count)
    else:
        with open('count.txt', 'w') as f:
            f.write('0')
            print('0')
    
call_counter()