#3
import re

f = open('Indonesia.txt', 'r', encoding='latin1')
r = r'di\s[\w\.-]+'
string3 = re.findall(r, f.read())
print(string3)
print ("-------------------------------------------------------------------------")

