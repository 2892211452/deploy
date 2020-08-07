import re
s="gaxx[I]xxefahxxlovexxhoghexxpythonxxghaweoif"
r=re.compile('\[.*?\]')
content=r.findall(s)
print(content)