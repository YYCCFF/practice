list=["a","b","c"]
result = ""
for x in list:
    result += x
print(result)
    
result=",".join(list)
print(result)

list=["a","b","c",1]
map_result=map(str,list)
result="".join(map_result)
print(result)

import os
list=["/a/","b/","c"]
a = os.path.join(*list)
print(a)
