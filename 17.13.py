import re
def xoo(stri):
    m=re.findall('.oo',stri)
    print(m)
xoo('the ghost that says boo haunts the loo')
