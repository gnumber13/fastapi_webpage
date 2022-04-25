import markdown as md
import os
import yaml

def md_to_html(md_content):
    return md.markdown(md_content)

def load_yaml_data(filename, dataname):
    with open(filename, 'r') as file:
        my_data = yaml.safe_load(file)
    return my_data[dataname]

def mdfile_to_html(filename):
    with open(filename, 'r') as md_file:
        md_content = md_file.read()
    html_content = md_to_html(md_content)
    return html_content

def get_base_filename(filename):
    base = os.path.basename(filename)
    return os.path.splitext(base)[0]

def update_html():
    entry_list = load_yaml_data("config.yaml.py", "menu")

    for entry in entry_list:
        md_file = entry['markdown_file']
        md_file = os.path.basename(md_file)

        # strip .py
        base_file = get_base_filename(md_file) 
        # strip .md
        base_file = get_base_filename(base_file) 

        templates_folder = "templates/"
        markdown_folder = "markdown/"
        rel_path = markdown_folder + md_file
        html_file = templates_folder + base_file + ".html"

        print(md_file, html_file)

        html_content = mdfile_to_html(rel_path)

        with open(html_file, 'w') as file:
            file.write(html_content)
