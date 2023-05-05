# func fileName 'visitor.txt' non-exist -> create

import os

if os.path.exists('visitors.txt'):
    with open('visitors.txt', 'r') as f:
        count = int(f.read())
    count += 1
    with open('visitors.txt', 'w') as f:
        f.write(str(count))
else:
    with open('visitors.txt', 'w') as f:
        f.write('0')