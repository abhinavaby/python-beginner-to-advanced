""" Can you change the values inside a list which is contained in set S?
S = {8, 7, 12, "Harry", [1,2]}"""


"""No, because you cannot even create this set in the first place.
 The code will throw a TypeError: unhashable type: 'list' immediately.
 Why This HappensSets only allow hashable items: Elements in a Python set must be immutable (unchangeable),
such as integers, strings, or tuples.Lists are mutable: Because a list can be modified after creation, it is considered unhashable.
Therefore, Git/Python prevents you from putting a list inside a set.How to fix it if you need a collectionIf you want to store a sequence
of numbers inside a set, you must use a tuple instead of a list:"""

# This works perfectly because tuples are immutable (hashable)
S = {8, 7, 12, "Harry", (1, 2)} 