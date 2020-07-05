#4

import re
f = open('KEI.html', 'r', encoding='latin1')
teks = f.read()
strings = re.findall(r'title="([\w+]+)">', teks)
strings= re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>', teks)
x = []
for y in strings:
    x.append((y[0], float(y[1])))

print(x)
