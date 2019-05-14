# Given 2 collections of numbers of equal len find and delete the
# dublicates and return a collected collection.

# [1, 2, 3, 4] & [3, 4, 5, 6] => [1, 2, 3, 4, 5, 6]

# Use the folowing approach to solve the problem
# 1. Be sure you understand the question, ask for a clearification.
# 2. Think out loud, this is good at interviews and good at and exams!
# 3. Think it through before you start coding and tell about your thoughts
# 4. Code it, and again tell what you are doing.
# 4. Test it at the end, does it work
#	* think about the edge cases (empty collection, 1 in the collection)

# You should be able to think of 2-3 solutions for this problem.
# Some nicer than others, some maybe faster than others.
# Try to code them all (2-3 solutions) and decide which one you like the most and why.


def find_duplicates(l1, l2):

    # copy the lists
    list_1 = l1[:]
    list_2 = l2[:]

    # go from large index to low index

    for i in range(len(l1)):
        for j in range(len(l2), 0):
            if l1[i] == l2[j]:
                l2.pop(j)

    return l1+l2
