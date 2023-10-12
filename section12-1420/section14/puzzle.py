import os
import shutil
# print(os.getcwd())
# path_file = "C:\\Users\\WIN 10\\Desktop\\Python\\practice\\section12-1420\\section14"
# shutil.unpack_archive("unzip_me_for_instructions.zip",path_file,"zip")
# with open("extracted_content/Instructions.txt") as f:
#   content = f.read()
#   print(content)
import re
pattern = r"\d{3}-\d{3}-\d{4}"

def search(file,pattern =pattern):
  with open(file, "r") as file:
    text = file.read()
  
  if re.search(pattern, text):
    return re.search(pattern, text)
  else:
    return ""

import os
results = []

for folder,sub_folders,files in os.walk(os.getcwd() + "\\extracted_content"):
  
  for f in files:
    full_path = folder+"\\"+f
    results.append(search(full_path))

for r in results:
  if r !="":
    print(r.group())