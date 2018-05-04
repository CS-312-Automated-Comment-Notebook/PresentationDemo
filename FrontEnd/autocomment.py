import os
'''from evalast import comment
from autodocgen import autoDocGenerator

        f = open('example.py', 'r')
        code = f.readlines()
        code = "".join(str(x) for x in code)
        print (code)
        commdic = comment(code)'''


def repComms(inputfile,commdic):

    count = 0

    with open(inputfile) as f:

        with open('exn.py', 'w') as f1:

            for line in f:

                count += 1

                if count in commdic:
                    f1.write(line.rstrip('\n') + " # " + commdic[count] + "\n")

                else:
                    f1.write(line)

    os.system('mv exn.py ' + inputfile)

