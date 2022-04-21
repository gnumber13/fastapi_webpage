import markdown as md

def md_to_html(filename):
    return md.markdown(filename)

print(md_to_html("#heading1") )

