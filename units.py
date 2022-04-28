import markdown as md
import os
import yaml

#markdown_dir = "markdown/"
#html_render_dir = "html_renders/"
#templates_dir = "templates/"

def md_to_html(md_content):
    return md.markdown(md_content)

def mdfile_to_html(filename):
    with open(filename, 'r') as md_file:
        md_content = md_file.read()
    html_content = md_to_html(md_content)
    return html_content

def load_yaml_data(filename, dataname):
    with open(filename, 'r') as file:
        my_data = yaml.safe_load(file)
    return my_data[dataname]

def concat_blogs(markdown_path):
    dirlist = os.listdir(markdown_path)

    for item in dirlist:
        extension = os.path.splitext(item)[1]

        if extension == '.d':
            print(extension)
            dirlist_per_blog = os.listdir("markdown/" + item)
            dirlist_per_blog = sorted(dirlist_per_blog, reverse=True)

            blog_html = ""
            for blog_item in dirlist_per_blog:
                with open("markdown/" + item + "/" + blog_item, 'r') as blog_file:
                    item_md = blog_file.read()
                    item_html = md_to_html(item_md)
                    blog_html = blog_html + "<div class='blog_entrie'>" + item_html + "</div>"

                item_basename = get_base_filename(item)

                with open("templates/html_renders/" + item_basename + "_blog.html", 'w') as out_file:
                    out_file.write(blog_html)
                    


def list_files_in_folder(path):
    return os.listdir(path)

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
        html_render_dir = templates_folder + "html_renders/"
        rel_path = markdown_folder + md_file
        html_file = html_render_dir + base_file + ".html"

        print(md_file, html_file)

        html_content = mdfile_to_html(rel_path)

        with open(html_file, 'w') as file:
            file.write(html_content)

