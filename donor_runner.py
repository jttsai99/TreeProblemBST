# Your solution for the donor problem here
from Trees.src.trees.bst_tree import BST
from Trees.src.donor_prog.donor import Donor
import sys

def get_tree_list(node, l):
    if (node == None):
        return
    get_tree_list(node.left, l)
    l.append(node.value)
    get_tree_list(node.right, l)


def inorder(tree, shoudprint=True):
    l = []
    get_tree_list(tree.root, l)
    if (shoudprint):
        print(l)
    return l


def read_donors(filename):
    f = open(filename, "r")
    donors = []
    for i in f.readlines():
        try:
            arr = i.split(":")
            val1 = arr[0].strip()
            val2 = arr[1].replace(" ", "").strip()
            val2 = int(val2)
            donors.append(Donor(val1, val2))
        except:
            continue
    return donors


donors = read_donors(sys.argv[1])


def make_bst(donations):
    dic = {}
    tree = BST()
    for donation in donations:
        dic[donation.amount] = donation
        tree.add_value(donation.amount)
    return tree, dic


tree, dic = make_bst(donors)
inorderlist = inorder(tree, shoudprint=False)


def printall():
    for value in inorderlist:
        print(dic[value])


def maxdonor():
    maxd = tree.get_max_node()
    print(dic[maxd.value])


def mindonor():
    maxd = tree.get_min_node()
    print(dic[maxd.value])


def donor_with(amt):
    if (amt in dic):
        print(dic[amt])
    else:
        print("No Match")


def donor_with_greater(amt):
    found = False
    for donation in inorderlist:
        if (donation > amt):
            print(dic[donation])
            found = True
            break
    if (not found):
        print("No Match")


def donor_with_less(amt):
    found = False
    inorderlist.reverse()
    for donation in inorderlist:
        if (donation < amt):
            print(dic[donation])
            found = True
            break
    if (not found):
        print("No Match")
    inorderlist.reverse()


def process_args():
    args = sys.argv
    args = args[1:]
    if (len(args) <= 1):
        return
    if (args[1] == "all"):
        printall()
    elif (args[1] == "rich"):
        maxdonor()
    elif (args[1] == "cheap"):
        mindonor()
    elif (args[1] == "who"):
        if (len(args) <= 2):
            return
        if (args[2][0] == "+"):
            donor_with_greater(int(args[2][1:]))
        elif (args[2][0] == "-"):
            donor_with_less(int(args[2][1:]))
        elif (args[2][0].isdigit()):
            donor_with(int(args[2]))


process_args()
