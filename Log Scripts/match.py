import re

log_file_path = r"C:\ios logs\sfbios.log"
regex = '(<property name="(.*?)">(.*?)<\/property>)'

match_list = []
with open(log_file_path, "r") as file:
    for line in file:
        for match in re.finditer(regex, line, re.S):
            match_text = match.group()
            match_list.append(match_text)
            print(match_text)