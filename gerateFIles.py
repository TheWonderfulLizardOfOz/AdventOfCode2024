import os

for i in range(1, 26):
    path = str(os.getcwd()) + "/Day " + str(i)

    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)

    files = ["/Day" + str(i) + ".py", "/test.txt", "/input.txt"]
    for f in files:
        open(path + f, 'a').close()

    f = open(path + files[0], 'w')
    f.write("import re\nimport math\n\nlines = open(\"input.txt\", \"r\", encoding=\"utf-8\").read().splitlines()\n\n\ndef day{i}p1():\n    return 0\n\n\ndef day{i}p2():\n    return 0\n\n\nprint(day{i}p1())\nprint(day{i}p2())\n".format(i=str(i)))
    f.close()
