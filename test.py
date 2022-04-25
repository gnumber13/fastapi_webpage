import units as un

with open('test.md', 'r') as md_file:
    md_content = md_file.read()


#print(md_content)
html_content = un.md_to_html(md_content)

with open('templates/md_test.html', 'w') as html_file:
    html_file.write(html_content)
