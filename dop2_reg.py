import re


def get_content(s, open_teg, end_teg):
    return s.replace(open_teg, '').replace(end_teg, '')


def get_yaml_content(file):
    tab = 0
    yaml_content = []
    for row in file:
        row_strip = row.strip()
        tab_in_this_line = tab * '\t'
        open_teg = re.findall(r'<[a-zA-Z_]*>', row_strip)
        end_teg = re.findall(r'</[a-zA-Z_]*>', row_strip)
        if open_teg and end_teg:
            content = get_content(row_strip, open_teg[0], end_teg[0])
            yaml_content.append(f'{tab_in_this_line}{open_teg[0][1:-1]}: {content}')
        elif open_teg:
            none_end_teg = '</' + open_teg[0][1:]
            content = get_content(row_strip, open_teg[0], none_end_teg)
            tab += 1
            yaml_content.append(f'{tab_in_this_line}{open_teg[0][1:-1]}: {content}')
        elif end_teg:
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
