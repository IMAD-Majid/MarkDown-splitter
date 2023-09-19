targetLoc = input("Path to the large markdown (.md): ")
destination = input("Path to the output folder: ")
splitStart = input("Split start expression: ")
splitStop = input("Split stop expression: ")

def createMD(title, content):
    with open(destination + '\\' + title + ".md", 'w') as f:
        f.write(content)

with open(targetLoc, 'r') as f:
    lines = f.readlines()
    content = ''
    title = ''
    splitting = False
    for line in lines:
        if splitting:
            if splitStop in line:
                splitting = False
                createMD(title, content)
                title = ''
                content = ''
                continue
            content += line
        elif splitStart in line:
            splitting = True
            title = line[len(splitStart):].strip()
            continue

