list = []
with open('bla.txt', 'r') as file:
  for line in file.readlines():
    if len(line.split(' - ')) >= 4:
      d = dict()
      d['Date'] = line.split(' - ')[0]
      d['Type'] = line.split(' - ')[2]
      d['Message'] = line.split(' - ')[3]
      list.append(d)
print(list)

# https://stackoverflow.com/questions/30627810/how-to-parse-this-custom-log-file-in-python