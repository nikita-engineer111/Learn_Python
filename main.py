


"""

    ТУТ Я ПРОХОДИЛ ЗАДАНИЯ ПО PYTHON
    ЗАДАНИЯ РАЗДЕЛЕНЫ ДЛИННОЙ СТРОКОЙ КОМЕНТАРИЯ ##########
    ЧТОБЫ ПРОВЕРИТЬ МОИ ОТВЕТЫ,
    РАСКОМЕНТИРУЙТЕ КОД ПОСЛЕ #ANSWER И ЗАПУСТИТЕ СКРИПТ

"""




################################################################
"""
Задание 3.1
Обработать строку ospf_route и вывести информацию в виде:
Protocol: OSPF
Prefix: 10.0.24.0/24
AD/Metric: 110/41
Next-Hop: 10.0.13.3
Last update: 3d18h
Outbound Interface: FastEthernet0/0

ospf_route = "O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
"""
# ANSWER
"""
ospf_route = "O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
zero, prefix, metric, via,next_hop, last_update,o_intrf = ospf_route.split()
answer = f"Protocol: OSPF\n" \
         f"Prefix: {prefix}\n" \
         f"AD/Metric: {str(metric).replace('[','').replace(']','')}\n" \
         f"Next-Hop: {str(next_hop).replace(',','')}\n" \
         f"Last update: {str(last_update).replace(',','')}\n" \
         f"Outbound Interface: {o_intrf}"
print(answer)
"""

################################################################

"""
Задание 3.2
Преобразовать строку MAC с формата XXXX:XXXX:XXXX в XXXX.XXXX.XXXX
MAC = "AAAA:BBBB:CCCC"
"""
# ANSWER
"""
mac = "AAAA:BBBB:CCCC"
mac_handl = mac.replace(':','.')
print(mac_handl)
"""

################################################################

"""
Задание 3.3
Получить из строки CONFIG список VLAN вида ['1', '3', '10', '20', '30', '100'].
CONFIG = "switchport trunk allowed vlan 1,3,10,20,30,100"
"""
# ANSWER
"""
config = "switchport trunk allowed vlan 1,3,10,20,30,100"
vlans = config.split()[-1].split(',')
print(vlans)
"""

################################################################

"""
Задание 3.4
Из строк command1 и command2 получить список VLAN, которые есть и в команде
command1 и в команде command2. Не использовать для решения задачи циклы,
оператор if.
Для данного примера, результатом должен быть список: [1, 3, 100]
command1 = "switchport trunk allowed vlan 1,3,10,20,30,100"
command2 = "switchport trunk allowed vlan 1,3,100,200,300"
"""
# ANSWER
"""
command1 = "switchport trunk allowed vlan 1,3,10,20,30,100"
command2 = "switchport trunk allowed vlan 1,3,100,200,300"
vlans1 = set(command1.split()[-1].split(','))
vlans2 = set(command2.split()[-1].split(','))
intersection = list(map(int,vlans1.intersection(vlans2)))
print(intersection)
"""

################################################################

"""
Задание 3.5
Список VLANS - это список VLANов, собранных со всех устройств сети, поэтому в
списке есть повторяющиеся номера VLAN.
Из списка нужно получить уникальный список VLANов, отсортированный по
возрастанию номеров.
Не использовать для решения задачи циклы, оператор if.
VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
"""
# ANSWER
"""
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
unique_vlans = list(set(vlans))
unique_vlans.sort()
print(unique_vlans)
"""

################################################################

"""
Задание 3.6
Обработать строку NAT таким образом, чтобы в имени интерфейса вместо
FastEthernet было GigabitEthernet.
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
"""
# ANSWER
"""
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
nat = nat.replace('FastEthernet','GigabitEthernet')
print(nat)
"""

################################################################

"""
Задание 3.7
Преобразовать MAC-адрес в двоичную строку (без двоеточий).
MAC = "AAAA:BBBB:CCCC"
"""
# ANSWER
"""
mac = "AAAA:BBBB:CCCC"
mac = mac.split(':')
bin_mac = ''
for i in mac:
    bin_mac += str(bin(int(i,16)))
print(bin_mac)
"""

################################################################

"""
Задание 3.8
Преобразовать IP-адрес (переменная IP) в двоичный формат и вывести вывод
столбцами, таким образом:
первой строкой должны идти десятичные значения байтов
второй строкой двоичные значения
Вывод должен быть упорядочен также, как в примере:
столбцами
ширина столбца 10 символов
Пример вывода:
10 1 1 1
00001010 00000001 00000001 00000001
IP = '192.168.3.1'
"""
# ANSWER
"""
ip = '192.168.3.1'
ip = list(map(int, ip.split('.')))
print('{:} {:10} {:10} {:10}'.format(ip[0], ip[1], ip[2], ip[3]))
print('{:b} {:10b} {:10b} {:10b}'.format(ip[0], ip[1], ip[2], ip[3]))
"""

################################################################

"""
Задание 3.9
Найти индекс последнего вхождения элемента с конца.
Например, для списка num_list, индекс последнего вхождения элемента 10 - 4; для
списка word_list, индекс последнего вхождения элемента 'ruby' - 6.
Сделать решение общим (то есть, не привязываться к конкретному элементу) и
проверить на разных списках и элементах.
Не использовать для решения циклы (for, while) и условия (if/else).
Подсказка: функция len() возвращает длину списка.
num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']
"""
# ANSWER
"""
num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']
word_list.reverse()
f_index = len(word_list) - 1 - word_list.index('python')
print(f_index)
"""

################################################################

"""
Задание 4.2
В этой задаче нельзя использовать условие if и нельзя изменять словарь london_co.
В задании создан словарь с информацией о разных устройствах.
Вам нужно запросить у пользователя ввод имени устройства (r1, r2 или sw1). И
вывести информацию о соответствующем устройстве на стандартный поток вывода
(информация будет в виде словаря).
Пример выполнения скрипта:
$ python task_4_2.py
Enter device name: r1
{'ios': '15.4', 'model': '4451', 'vendor': 'Cisco', 'location': '21 New Globe Walk', '
ip': '10.255.0.1'}

Задание 4.2a
В этой задаче нельзя использовать условие if и нельзя изменять словарь london_co.
Переделать скрипт из задания 4.2 таким образом, чтобы, кроме имени устройства,
запрашивался также параметр устройства, который нужно отобразить.
Вывести информацию о соответствующем параметре, указанного устройства.
Пример выполнения скрипта:
$ python task_4_2a.py
Enter device name: r1
Enter parameter name: ios
15.4

Задание 4.2b
В этой задаче нельзя использовать условие if и нельзя изменять словарь london_co.
Переделать скрипт из задания 4.2a таким образом, чтобы, при запросе параметра,
отображался список возможных параметров.
Вывести информацию о соответствующем параметре, указанного устройства.
Пример выполнения скрипта:
$ python task_4_2b.py
Enter device name: r1
Enter parameter name (ios,model,vendor,location,ip): ip
10.255.0.1

Задание 4.2c
В этой задаче нельзя использовать условие if и нельзя изменять словарь london_co.
Переделать скрипт из задания 4.2b таким образом, чтобы, при запросе параметра,
которого нет в словаре устройства, отображалось сообщение 'Такого параметра нет'.
Попробуйте набрать неправильное име параметра или несуществующий
параметр, чтобы увидеть какой будет результат. А затем выполняйте задание.
Если выбран существующий параметр, вывести информацию о соответствующем
параметре, указанного устройства.
Пример выполнения скрипта:
$ python task_4_2c.py
Enter device name: r1
Enter parameter name (ios,model,vendor,location,ip): io
Такого параметра нет

Задание 4.2d
В этой задаче нельзя использовать условие if и нельзя изменять словарь london_co.
Переделать скрипт из задания 4.2c таким образом, чтобы, при запросе параметра,
пользователь мог вводить название параметра в любом регистре.
Пример выполнения скрипта:
$ python task_4_2d.py
Enter device name: r1
Enter parameter name (ios,model,vendor,location,ip): IOS
15.4
"""
# ANSWER
london_co = {
'r1' : {
'location': '21 New Globe Walk',
'vendor': 'Cisco',
'model': '4451',
'ios': '15.4',
'ip': '10.255.0.1'
},
'r2' : {
'location': '21 New Globe Walk',
'vendor': 'Cisco',
'model': '4451',
'ios': '15.4',
'ip': '10.255.0.2'
},
'sw1' : {
'location': '21 New Globe Walk',
'vendor': 'Cisco',
'model': '3850',
'ios': '3.6.XE',
'ip': '10.255.0.101',
'vlans': '10,20,30',
'routing': True
}
}

device = input(f'Все устройства: {", ".join(list(map(str,london_co.keys())))}\n'
               f'Введите имя нужного устройства: ')
parametr = input(f'Введите параметр устройства ({", ".join(list(map(str,london_co[device.lower()].keys())))}): ')
print(london_co.get(device.lower(), 'Такого устройства нет').get(parametr.lower(), 'Такого параметра нет'))
input()

################################################################

