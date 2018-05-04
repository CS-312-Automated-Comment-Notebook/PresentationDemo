import ast

# dictionary storing values of variables
d = dict()
# dictionary storing comments and the line numbers before which they have to be inserted
comm = dict()
binop = {ast.Add: 1, ast.Sub: 2, ast.Mod: 3, ast.Mult: 4, ast.Div: 5, ast.Pow: 6, ast.Gt: 7, ast.Lt: 8, ast.Eq: 9,
         ast.GtE: 10, ast.LtE: 11}


# function to calculate value of a nested binary expression
# works for + , - , / , % , *
def expr(n):
    if type(n) == ast.Num:
        return n.n
    elif type(n) == ast.Name:
        return d[n.id]
    else:
        op = binop[type(n.op)]
        if op == 1:
            return expr(n.left) + expr(n.right)
        elif op == 2:
            return expr(n.left) - expr(n.right)
        elif op == 3:
            return expr(n.left) % expr(n.right)
        elif op == 4:
            return expr(n.left) * expr(n.right)
        elif op == 5:
            return expr(n.left) / expr(n.right)
        elif op == 6:
            return expr(n.left) ** expr(n.right)


def comp(n):
    if type(n) == ast.Compare:
        op = binop[type(n.ops[0])]
        # print(op)
        if op == 7:
            return expr(n.left) > expr(n.comparators[0])
        elif op == 8:
            # print(d[n.left.id] < d[n.comparators[0].id])
            return expr(n.left) < expr(n.comparators[0])
        elif op == 9:
            return expr(n.left) == expr(n.comparators[0])
        elif op == 10:
            return expr(n.left) >= expr(n.comparators[0])
        elif op == 11:
            return expr(n.left) <= expr(n.comparators[0])



def assign(n):
    # checking if variable on left has to store a value
    # adding it to dictionary of variables declared in the program
    # if type(n.targets[0].ctx) == ast.Store:
    #     d[n.targets[0].id] = 0
    # if type(n.value) == ast.Num:
    #     d[n.targets[0].id] = n.value.n
    # elif type(n.value) == ast.Name:
    #     d[n.targets[0].id] = d[n.value.id]
    # if type(n.value) == ast.BinOp:

    # checking if there is a value/variable/expression to be stored in the variable on the left by calling expr()
    d[n.targets[0].id] = expr(n.value)
    comm[n.targets[0].lineno] = "Value of variable " + n.targets[0].id + " was " + str(d[n.targets[0].id])


def printing(n, line):
    comm[line] = "Value printed = " + str(expr(n[0]))

    # if type(n[0]) == ast.Num:
    #     comm[line] = "Value printed = " + str(n[0].n)
    # elif type(n[0]) == ast.Name:
    #     comm[line] = "Value printed = " + str(d[n[0].id])
    # elif type(n[0])

def check(n):
    if isinstance(n, ast.Assign):
        assign(n)
    elif isinstance(n, ast.Expr):
        if n.value.func.id == 'print':
            printing(n.value.args, n.lineno)
    elif isinstance(n, ast.If):
        # print(n, n.test, type(n.body))
        if comp(n.test):
            check(n.body[0])
            # if type(n.body[0]) == ast.Expr:
            #     if n.body[0].value.func.id == 'print':
            #         printing(n.body[0].value.args, n.lineno)
        else:
            check(n.orelse[0])

def comment(cod):
    node = ast.parse(cod)
    x = (ast.dump(node))
    print(x)
    for n in node.body:
        # print(type(n))
        check(n)
        # if isinstance(n, ast.Assign):
        #     assign(n)
        # if isinstance(n, ast.Expr):
        #     if n.value.func.id == 'print':
        #         printing(n.value.args, n.lineno)



    # print(d)
    # print(comm)
    return comm


print(comment('''#* Variable *declaration*
x=8
y= x**8
x = y - (x**5)
print (y+(x%6))
#* **check** statement
if x<y:
    if x == 2:
        print (x)
    else:
        if x > 1:
            x=x+3
'''))
