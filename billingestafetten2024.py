"""
Presentera TioKommaTvå:s tider i Billingestafetten 2024
"""

def to_seconds(s):
    sl = reversed(s.split(':'))
    out_sum = 0
    for k, b in enumerate(sl):
        out_sum += int(b)*60**k
    return out_sum

def from_seconds(t, hours = False):
    s = t % 60
    if hours:
        m = t // 60 % 60
        h = t // 3600
        return f'{h:d}:{m:02d}:{s:02d}'
    else:
        m = t // 60
        return f'{m:d}:{s:02d}'

    return f'{sec}'
    out_sum = 0
    for k, b in enumerate(sl):
        out_sum += int(b)*60**k
    return out_sum

indata_str = "07:50 75 7:50 75	15:34 82 7:44 83	16:37 82 1:03 93	26:44 94 10:07 99	28:14 95 1:30 100	38:59 96 10:45 100	40:25 96 1:26 101	47:45 94 7:20 62	48:38 94 0:53 46	57:38 92 9:00 76	58:33 92 0:55 64	1:05:33 91 7:00 54	1:06:32 91 0:59 69	1:14:01 88 7:29 61	1:14:49 88 0:48 28	1:20:28 86 5:39 26	1:21:16 86 0:48 39	1:27:42 84 6:26 57	1:28:34 84 0:52 70"
indata_list = indata_str.split()
dict_list = []
for k, record in enumerate(indata_list):
    m = k // 4
    r = k % 4
    if r == 0:
        d = {'cum_time': to_seconds(record)}
        dict_list.append(d)
    elif r == 1:
        d['cum_pos'] = int(record)
    elif r == 2:
        d['lap_time'] = to_seconds(record)
    elif r == 3:
        d['lap_pos'] = int(record)

'''
for item in dict_list:
    print(item)
'''

print('\t\tVarv 1\t\t\t\tVarv 2\t\t\t\tHela rundan')
print('\t\ttid\ttempo\t# varv\t# tot\ttid\ttempo\t# varv\t# tot\ttid\ttempo')
for k, runner in enumerate(("Erica", "Niclas", "Mostafa", "Stefan", "Yohannes")):
    if k == 0:
        lap1_time = dict_list[0]['lap_time']
        lap2_time = dict_list[1]['lap_time'] + dict_list[2]['lap_time']
        lap1_pos_lap = dict_list[0]['lap_pos']       
        lap2_pos_lap = dict_list[2]['lap_pos']       
        lap1_pos_cum = dict_list[0]['cum_pos']       
        lap2_pos_cum = dict_list[2]['cum_pos']       
    else:
        lap1_time = dict_list[4*k - 1]['lap_time'] + dict_list[4*k]['lap_time']
        lap2_time = dict_list[4*k+1]['lap_time'] + dict_list[4*k + 2]['lap_time']
        lap1_pos_lap = dict_list[4*k]['lap_pos']       
        lap2_pos_lap = dict_list[4*k+1]['lap_pos']       
        lap1_pos_cum = dict_list[4*k]['cum_pos']       
        lap2_pos_cum = dict_list[4*k+1]['cum_pos']       
    total_time = lap1_time  + lap2_time
    print(f'{runner.ljust(12)}\t'\
        f'{from_seconds(lap1_time)}\t'\
        f'{from_seconds(round(lap1_time/1.5))}\t'\
        f'{lap1_pos_lap}\t'\
        f'{lap1_pos_cum}\t'\
        f'{from_seconds(lap2_time)}\t'\
        f'{from_seconds(round(lap2_time/1.5))}\t'\
        f'{lap2_pos_lap}\t'\
        f'{lap2_pos_cum}\t'\
        f'{from_seconds(total_time)}\t'\
        f'{from_seconds(round(total_time/3))}'
    )
total_time = dict_list[-1]['cum_time']
print(f'Totalt\t\t\t\t\t\t\t\t\t\t{from_seconds(total_time, hours = True)}\t{from_seconds(round(total_time/15))}')


