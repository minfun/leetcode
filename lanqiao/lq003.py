data = raw_input('please input num list:')
num_map = {
    '1': 'A',
    '2': 'B',
    '3': 'C',
    '4': 'D',
    '5': 'E',
    '6': 'F',
    '7': 'G',
    '8': 'H',
    '9': 'I',
    '10': 'J',
    '11': 'K',
    '12': 'L',
    '13': 'M',
    '14': 'N',
    '15': 'O',
    '16': 'P',
    '17': 'Q',
    '18': 'R',
    '19': 'S',
    '20': 'T',
    '21': 'U',
    '22': 'V',
    '23': 'W',
    '24': 'X',
    '25': 'Y',
    '26': 'Z',
}
num_list = data.split(',')
print len(num_list)
sorted_num_list = sorted(map(lambda x: int(x), num_list))
print sorted_num_list[0]
print ','.join(map(lambda x: str(x), sorted_num_list))
l = []
for i in num_list:
    if int(i) <= 26:
        l.append(num_map[i])
    else:
        l.append('[bad]')
print ''.join(l)
