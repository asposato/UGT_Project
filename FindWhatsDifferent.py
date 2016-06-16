lst1 = [line.strip() for line in open("TAIR_Glycosyltransferase_Family_1.csv", 'r')]
print(lst1)
lst2 = [line.strip() for line in open("CoGeBLAST_Glycosyltransferase_Family_1.csv", 'r')]
print(lst2)

lst2clean = []
for n in lst2:
    n2 = str(n.rstrip((',')))
    n2 = str(n2.rstrip(('1')))
    n2 = str(n2.rstrip('mRNA'))
    n2 = str(n2.rstrip('mRNA2'))
    n2 = str(n2.rstrip('.'))
    lst2clean.append(n2)
    
print(lst2clean)

def diff(lst1, lst2clean):
    c = set(lst1).union(set(lst2clean))
    d = set(lst1).intersection(set(lst2clean))
    return list(c - d)
print("The next set are the differences.")
print(diff(lst1, lst2clean))