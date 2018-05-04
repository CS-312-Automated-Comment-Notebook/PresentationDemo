import nbformat as nbf
import os

spas = 'raeg'  # enter your sudo password here[deprecated]

nb = nbf.v4.new_notebook()


def autoDocGenerator(file, format):
    f = open(file, 'r')
    lx = []
    isCode = False
    for line in f:
        if (line.strip().startswith('#*')) and (not isCode):
            ln = line.lstrip('#*')
            nb['cells'].append(nbf.v4.new_markdown_cell(ln.strip()))
        elif (line.strip().startswith('#*')) and isCode:
            if (len(lx) == 0):
                pass
            else:
                s = ''.join(lx)
                nb['cells'].append(nbf.v4.new_code_cell(s))
                lx[:] = []
                isCode = False
            ln = line.lstrip('#*')
            nb['cells'].append(nbf.v4.new_markdown_cell(ln.strip()))
        elif (line == '\n'):
            if (len(lx) == 0):
                pass
            else:
                s = ''.join(lx)
                nb['cells'].append(nbf.v4.new_code_cell(s))
                lx[:] = []
                isCode = False
        else:
            lx.append(line)
            isCode = True
    if len(lx) != 0:
        s = ''.join(lx)
        nb['cells'].append(nbf.v4.new_code_cell(s))
    nbf.write(nb, file + '.ipynb')
    print(os.path.realpath(file))
    comm = "jupyter nbconvert --to " + format + " '" + os.path.realpath(file) + ".ipynb'"
    os.popen("echo $MYSUDOPASS | sudo -S " + comm, 'w').write(spas)


#autoDocGenerator('usercode.py', 'pdf')
