""" What will be the length of following set S:
s = Set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?"""
s=set()
s.add(20)
s.add(20.0)
s.add('20')
print(s)
print(f" length of s ={len(s)}") # 20 is equal to 20.0 so the length will be 2

