from fprintx import printx


def simplifyPath(path):
        path_list = [i for i in path.split("/") if i != '']
        path_stack = ['']
        for pl in path_list:
            # print(path_stack)
            if pl == '..':
                if path_stack:
                    path_stack.pop()
                continue
            elif pl == '.':
                continue
            else:
                path_stack.append(pl)
        # printx(path_stack, ['/' + ps for ps in path_stack if ps != ''])
        return "".join(['/' + ps for ps in path_stack if ps != '']) or "/"




print(simplifyPath(path = "/home/"))
print(simplifyPath(path = "/home//foo/"))
print(simplifyPath(path = "/home/user/Documents/../Pictures"))
print(simplifyPath(path = "/../"))
print(simplifyPath( path = "/.../a/../b/c/../d/./"))
print(simplifyPath( path = "/home/../../.."))
