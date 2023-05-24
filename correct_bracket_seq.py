from itertools import islice
n=7

def rec(s='', stack=''):
    if len(s) == 2*n:
        if not stack:
            yield s
    else:
        yield from rec(s+'(', stack+'(')
        if stack and stack[-1]=='(':
            yield from rec(s+')', stack[:-1])
        yield from rec(s+'[', stack+'[')
        if stack and stack[-1]=='[':
            yield from rec(s+']', stack[:-1])
        

print(next(islice(rec(),8232,None)))