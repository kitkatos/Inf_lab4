def get_content(s, open_teg, end_teg):
    return s.replace(open_teg, '').replace(end_teg, '')


def get_open_teg(s):
    c = -1
    if s[1] != '/':
        for i in s:
            c += 1
            if i == '>':
                return s[:c+1]
    else:
        a = s.replase('/', '')[2:]
        for i in a:
            c += 1
            if i == '>':
                return s[:c+1]


def get_end_teg(s):
    return f'</{get_open_teg(s)[1:]}'


def get_yaml_content(file):
    tab = 0
    yaml_content = []
    for row in file:
        row_strip = row.strip()
        tab_in_this_line = tab * '\t'
        if (row_strip[0] == '<') and (row_strip[1] not in "?/"):
            open_teg = get_open_teg(row_strip)
            end_teg = get_end_teg(row_strip)
            content = get_content(row_strip, open_teg, end_teg)
            if open_teg in row_strip:
                tab += 1
            if end_teg in row_strip:
                tab -= 1
            yaml_content.append(f'{tab_in_this_line}{open_teg[1:-1]}: {content}')
        else:
            if (row_strip[0] == '<') and (row_strip[1] == '/'):
                tab -= 1
    return '\n'.join(yaml_content)

def clean_yaml():
    with open('C:/Users/kit67/Downloads/inf_lab/schedule_yaml.yml', 'w', encoding='utf-8'):
        pass


clean_yaml()
xml_file = open(input(), encoding='utf-8')  # inf.xml
yaml_file = open('outf.yml', 'w', encoding='utf-8')
print(get_yaml_content(xml_file))
yaml_file.write(get_yaml_content(xml_file))
