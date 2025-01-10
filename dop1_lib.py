import xmlplain


def get_yaml():
    with open(input(), encoding="utf-8") as inf:  # inf.xml
        root = xmlplain.xml_to_obj(inf, strip_space=True, fold_dict=True)

    with open("outf.yml", "w", encoding="utf-8") as outf:
        xmlplain.obj_to_yaml(root, outf)


def clean_yaml():
    with open('outf.yml', 'w', encoding='utf-8'):
        pass


clean_yaml()
get_yaml()
with open("outf.yml", "r", encoding="utf-8") as file:
    read_file = file.read()
print(read_file)
