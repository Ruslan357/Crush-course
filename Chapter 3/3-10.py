rivers = ['Nile', 'Amazon', 'Mississippi', 'Amur', 'Parana']

print(sorted(rivers))
print(sorted(rivers, reverse=True))
rivers.reverse()
rivers.sort()
rivers.sort(reverse=True)

rivers.pop()
rivers.append('Congo')
rivers.insert(3,'Yellow')
del rivers[3]