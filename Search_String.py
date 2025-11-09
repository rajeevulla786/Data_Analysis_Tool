This Data Analysis Tool searches for list of the substrings and replace then with Required Substrings

import os
substring_to_search=['XXXX','YYYY']
read_filename='Readfile.txt'
write_filename='Writefile.txt'

table=[]
with open(read_filename,'r') as f:
    for line in f:
	     if "--" not in line:
              list1=line.strip().split()
              for item in substring_to_search:
                  for target in list1:
                      if item.lower() in target.lower():
                          table.append(target.strip("`);"))
dedup_list=list(set(table))
dedup_list.sort()
with open(write_filename,'w') as f:
   for i in dedup_list:
       f.write(i + "\n")
