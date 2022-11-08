
print("Printing Updates:")

# Pages Directory for updating the site.
pages = [
    {
    "filename": "./content/index.html",
    "output": "./docs/index.html",
    "title": "Jake Ritter | Home",
    },
    {
    "filename": "./content/blog.html",
    "output": "./docs/blog.html",
    "title": "Jake Ritter | Blog",
    },
]


# Preps Pages and starts template creation. Replacing original content.
#def apply_template(input_page):
def apply_template():
    template = open("./templates/base.html").read()
    #input_content = open(input_page["filename"]).read()
    #updated_title = input_page["title"]
    input_content = open(page["filename"]).read()
    updated_title = page["title"]

    new_content = template.replace("{{content}}", input_content)
    new_page = new_content.replace("{{title}}", updated_title)
    return new_page

# Replaces link placeholders in template to allow site to be "active"
def apply_active_link():
    if page["title"] == "Jake Ritter | Home":
        new_home = new_page.replace("{{home_link_active}}", " active")
        return new_home
    elif page["title"] == "Jake Ritter | blog":
        new_blog = new_page.replace("{{blog_link_active}}", " active")
        return new_blog
    else:
        print(">>>> " + page["title"] + " <<<< has not been updated")

# Finishes and writes updated pages
def main():
    output = page["output"]
    
    if output == "./docs/index.html": 
        open(output, "w+").write(new_home)
        print("LINK ACTIVE FOR " + page["title"])   
    elif output == "./docs/blog.html": 
        open(output, "w+").write(new_blog)
        print("LINK ACTIVE FOR " + page["title"])
    else:
        open(output, "w+").write(new_page)

# Runs the functions and pushes out the site we want
for page in pages:
    #apply_template(page)
    new_page = apply_template()
    new_home = apply_active_link()
    new_blog = apply_active_link()
    main()

