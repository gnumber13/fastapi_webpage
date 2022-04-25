import yaml

with open('config.yaml.py', 'r') as file:
    my_data = yaml.safe_load(file)

menu_list = my_data['menu']

print(menu_list)
for menu_item in menu_list:
    print(menu_item['name'], menu_item['html_file'])
