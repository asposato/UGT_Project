list1 = [line.strip() for line in open("TAIR_Glycosyltransferase_Family_1.csv", 'r')]
list2 = [line.strip() for line in open("CoGeBLAST_Glycosyltransferase_Family_1.csv", 'r')]

def diff(list1, list2):
    c = set(list1).union(set(list2))
    d = set(list1).intersection(set(list2))
    return list(c - d)

print(diff(list1, list2))
