import keys

def is_chn(a_str):
    return a_str >= u'\u4e00' and a_str <= u'\u9fa5'

chn_char_list = []
for c in keys.alphabetChinese:
    if is_chn(c):
        chn_char_list.append(c)

print(len(chn_char_list))

print(''.join(chn_char_list))

