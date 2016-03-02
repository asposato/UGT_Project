lst1 = [line.strip() for line in open("TAIR_Glycosyltransferase_Family_1.csv", 'r')]
print(lst1) 
                     # takes information from TAIR_Glycosyltransferase_Family_1.csv and prints it to lst1. 

lst2 = [line.strip() for line in open("CoGeBLAST_Glycosyltransferase_Family_1.csv", 'r')]
print(lst2)
                     # takes information from CoGeBLAST_Glycosyltransferase_Family_1.csv and prints it to lst2 

lst2clean = []
for n in lst2:
    n2 = str(n.rstrip((',')))
    n2 = str(n2.rstrip(('1')))
    n2 = str(n2.rstrip('mRNA'))
    n2 = str(n2.rstrip('mRNA2'))
    n2 = str(n2.rstrip('.'))
    lst2clean.append(n2)
    
print(lst2clean)
print("        ATTENTION: The next list are the differences!")

                     # made a new empty list called "lst2clean"
                     # rstrip function is going to take off characters from the right of each item. 
                     # removed extra characters so that lst1 and lst2 had exact same format.

def diff(lst1, lst2clean):
    c = set(lst1).union(set(lst2clean))
    d = set(lst1).intersection(set(lst2clean))
    return list(c - d)

print(diff(lst1, lst2clean))

                     # defined a method "diff" 
                     # set variables equal to lst1 and lst2clean
                     # prints the items that are not in both lists but are in at least one of them

len(diff(lst1, lst2clean))

                     # determines number of nonmatches
import csv

lst3 = diff(lst1, lst2clean)
print(lst3)
with open('UGT_Diff.csv','w') as f:
    wr = csv.writer(f, delimiter=' ', quoting=csv.QUOTE_ALL)
    for val in lst3:
        wr.writerow([val])

# created new list: lst3 which is the differences between lst1 and lst2clean
# you needed to create a blank csv file in Excel. 
# writes the differences to a csv file called "UGT_Diff"
    # for loop writes each item into it's own cell in Excel
# make sure file is closed and not open in two places when trying to write to UGT_Diff
   