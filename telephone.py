def reformat(tel):
    tel = tel.replace('-', '')
    tel = tel.replace('(', '')
    tel = tel.replace(')', '')
    if len(tel) == 7:
        tel = '8495' + tel
    if tel == 8:
        tel = tel[0] + '495' + tel[1:]
    tel = tel.replace('+7', '8')
    if tel[0] == '7':
        tel = '8' + tel[1:]
    return tel


try:
    tel1 = str(input())
    tel2 = str(input())
    tel3 = str(input())
    tel4 = str(input())
except ValueError:
    print("ERROR!")
    exit(-1)
tel1 = reformat(tel1)
tel2 = reformat(tel2)
if tel1 == tel2:
    print('Yes')
else:
    print('No')
tel3 = reformat(tel3)
if tel1 == tel3:
    print('Yes')
else:
    print('No')
tel4 = reformat(tel4)
if tel1 == tel4:
    print('Yes')
else:
    print('No')
