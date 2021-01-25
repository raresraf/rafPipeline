import subprocess
import errno
import json
import os
import re

code_dict = {}


counter = 0
bad_counter = 0
for root, dirs, files in os.walk("../../TheCrawlCodeforces/results_code/"):
    for name in files:
        if '.cpp' not in name.lower():
            continue
        try:
            
            output_name = name[0:-4]

            path=os.path.join(root, output_name)
            print(path)

            if "_" in output_name:
                identifier = output_name.split("_")[0]
            else:
                identifier = output_name
            if not code_dict.get(identifier, None):
                code_dict[identifier] = []
            
            with open(os.path.join(root, name), "r") as f:
                pass
                # data = f.read()
            with open(os.path.join(root, output_name + ".s"), "r") as f:
                pass
                # data_asm = f.read()
            

            code_dict[identifier].append(os.path.join(root, name))

            counter = counter + 1
            print(f"{counter} sources added")
        except Exception:
            print("Not found")

with open('codeforce_lib.json', 'w') as f:
    json.dump(code_dict, f)

