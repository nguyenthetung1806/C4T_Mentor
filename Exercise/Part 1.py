main_list = [{'Quận': 'ST', 'Km2': 11743, 'Dân số': 150300},
         {'Quận': 'BĐ', 'Km2': 9.224, 'Dân số': 247100},
         {'Quận': 'BTL', 'Km2': 43.35, 'Dân số': 333300},
         {'Quận': 'CG', 'Km2': 12.04, 'Dân số': 266800},
         {'Quận': 'ĐĐ', 'Km2': 9.96, 'Dân số': 420900},
         {'Quận': 'HBT', 'Km2': 10.09, 'Dân số': 318000}]

print('Yêu cầu 1:')
list_name = []
for i in main_list:
    list_name.append(i['Quận'])
print(list_name)

list_ppl = []
for i in main_list:
    list_ppl.append(i['Dân số'])
print(list_ppl)

list_km2 = []
for i in main_list:
    list_km2.append(i['Km2'])


print('Yêu cầu 2:')
max_ppl = max(list_ppl)
min_ppl = min(list_ppl)
print('Chỉ số của quận có số dân lớn nhất: {}'.format(max_ppl))
print('Chỉ số của quận có số dân ít nhất: {}'.format(min_ppl))


print('Yêu cầu 3:')
name_max = list_name[list_ppl.index(max_ppl)]
name_min = list_name[list_ppl.index(min_ppl)]
print('Tên số của quận có số dân lớn nhất: {}'.format(name_max))
print('Tên của quận có số dân ít nhất: {}'.format(name_min))


print('Yêu cầu 4:')
list_density = []
for i in range(len(list_name)):
    list_density.append(
        list_km2[i] / list_ppl[i]
    )
print(list_density)
