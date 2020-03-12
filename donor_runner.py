# Your solution for the donor problem here
import sys
from typing import List

from Trees.src.trees.bst_tree import BST
from .Trees.src.donor_prog.donor import Donor

def returnBST(filepath)->BST:
    newbst = BST(key=lambda x:x.amount)
    with open(filepath) as inputfile:
        for i in inputfile:
            name, value = i.split(sep=":")
            newdonor = Donor(name, value)
            newbst.add_value(newdonor)
    return newbst

def main():
    donorbst = returnBST(sys.argv[1])
    donorfunctions(donorbst, sys.argv[2])

def donorfunctions(thebst , arg2):
    if arg2 == "rich":
        return getrich(thebst)
    elif arg2 == "cheap":
        return getcheap(thebst)
    elif arg2 == "all":
        return getall(thebst)
    elif arg2 =="who":
        whoval = sys.argv[3]
        return getwho(thebst,whoval)

def getrich(abst):
    maxnode = abst.get_max_node()
    statement = "{} with a donation of {}".format(maxnode.name,maxnode.amount)
    return statement

def getcheap(abst):
    minnode = abst.get_min_node()
    statement = "{} with a donation of {}".format(minnode.name, minnode.amount)
    return statement

def getall(abst):
    pass

def getwho(abst,whovalue):
    if "+" not in whovalue and "-" not in whovalue:
        if abst.get_node(int(whovalue)) == "MissingValueError":
            return "No Match"
        else:
            retrieve = abst.get_node(int(whovalue))
            statement = "{} with a donation of {}".format(retrieve.name, retrieve.amount)
            return statement
    elif "+" in whovalue:
        pass
    elif "-" in whovalue:
        pass


if __name__ == '__main__':
    main()





