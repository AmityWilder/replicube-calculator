import ast


def dfs(root: ast.AST) -> set[int] | set[tuple[int, int]] | set[tuple[int, int, int]]:
    fields = {fieldname: value for fieldname, value in ast.iter_fields(root)}
    if type(root) is ast.BinOp:
        op = type(fields['op'])
        left = dfs(fields['left'])
        right = dfs(fields['right'])
        # print(left, op.__name__, right)
        if op is ast.Mult:
            s = set()
            for a in left:
                if type(a) is tuple:
                    x,y = a
                    for z in right:
                        s.add((x, y, z))
                else:
                    x=a
                    for b in right:
                        if type(b) is tuple:
                            y,z = b
                            s.add((x, y, z))
                        else:
                            y=b
                            s.add((x, y))
        elif op is ast.BitOr:
            assert type(left) == type(right)
            s = left.union(right)
        elif op is ast.BitAnd:
            assert type(left) == type(right)
            s = left.intersection(right)
        else:
            raise Exception(op)
        # print(s)
        return s
    elif type(root) is ast.Set:
        s=set()
        prev = None
        is_ellipsis = False
        for elt in fields['elts']:
            elt_fields = {fieldname: value for fieldname, value in ast.iter_fields(elt)}
            if type(elt) is ast.UnaryOp:
                op_fields = {fieldname: value for fieldname, value in ast.iter_fields(elt)}
                assert type(op_fields['op']) is ast.USub
                elt = op_fields['operand']
                elt_fields = {fieldname: value for fieldname, value in ast.iter_fields(elt)}
                elt_fields['value'] *= -1
            if type(elt) is ast.Constant:
                x = elt_fields['value']
                if x is ...:
                    is_ellipsis = True
                elif type(x) is int:
                    # print(x)
                    if is_ellipsis:
                        is_ellipsis = False
                        assert prev is not None
                        for n in range(prev+1, x):
                            print(n)
                            s.add(n)
                    s.add(x)
                    prev = x
                else:
                    raise Exception(x)
            else:
                raise Exception(elt)
        # print(s)
        return s
    else:
        raise Exception(root)


while True:
    s = input()
    if s is None or s == "exit": break
    tree = ast.parse(s)
    tree = next(ast.iter_child_nodes(tree)) # skip Module
    tree = next(ast.iter_child_nodes(tree)) # skip Expr
    s = dfs(tree)
    print(s)
    if s:
        if type(next(iter(s))) is int:
            n = len(s)
        else:
            n = sum((len(xyz) for xyz in s))
        print(n)
