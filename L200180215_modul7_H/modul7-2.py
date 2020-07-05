#2
import re
f = open('Indonesia.txt', 'r', encoding='latin1')
p = r'di[\w\.-]+'
string = re.findall(p, f.read())
print(string)
print ("----------------------------------------------------------------------------")
