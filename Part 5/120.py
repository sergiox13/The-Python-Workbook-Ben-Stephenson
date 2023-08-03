def format_string(lst):

    if len(lst) == 2:
        return f'{lst[0]} и {lst[1]}'
    elif len(lst) > 2:
        s = ''
        for i in range(len(lst)-1):
            s += lst[i] + ', '
        s = s[:-2] + ' и ' + lst[-1]
        return s
    return lst[0]

print(format_string(['яблоки']))
print(format_string(['яблоки', 'апельсины']))
print(format_string(['яблоки', 'апельсины', 'бананы']))
print(format_string(['яблоки', 'апельсины', 'бананы', 'лимоны']))
print(format_string(['яблоки', 'апельсины', 'бананы', 'лимоны', 'ананасы']))