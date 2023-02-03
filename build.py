
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
def apply_template(page):
    
    template = open("./templates/base.html").read()
    input_content = open(page["filename"]).read()
    updated_title = page["title"]

    new_content = template.replace("{{content}}", input_content)
    new_page = new_content.replace("{{title}}", updated_title)
    return new_page

# Replaces link placeholders in template to allow site to be "active"
def apply_active_link(new_page, page):
    if page["title"] == "Jake Ritter | Home":
        return new_page.replace("{{home_link_active}}", " active")
    elif page["title"] == "Jake Ritter | Blog":
        return new_page.replace("{{blog_link_active}}", " active")
    else:
        print(">>>> " + page["title"] + " <<<< has not been updated")
        return new_page

# Finishes and writes updated pages
def main(page, new_page):
    output = page["output"]
    open(output, "w+").write(new_page)
    print("LINK ACTIVE FOR " + page["title"])

# Runs the functions and pushes out the site we want
for page in pages:
    new_page = apply_template(page)
    new_page = apply_active_link(new_page, page)
    main(page, new_page)

