from block_markdown import markdown_to_html
import os
import shutil
import re

def main():
    # Copy static pages to public
    source_dir = 'static'
    content_dir = 'content'
    dest_dir = 'public'
    template_file = 'template.html'
    copy_directory(source_dir, dest_dir)
    generate_pages_recursive(content_dir, template_file, dest_dir)

    # Generate html page
    # markdown_file = 'content/index.md'
    # template_file = 'template.html'
    # dest_file = 'public/index.html'
    # generate_page(markdown_file, template_file, dest_file)
    


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path) # Recreate directory

    dirs = os.listdir(dir_path_content) # copy the files from source dir
    for dir in dirs:
        source_path = os.path.join(dir_path_content, dir)
        dest_path = os.path.join(dest_dir_path, dir)
        if os.path.isfile(source_path):
            updated_file_path = dest_path.split(".")[0] + '.html'
            generate_page(source_path, template_path, updated_file_path)
        else:
            generate_pages_recursive(source_path, template_path, dest_path)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    md = read_file(from_path, "md")
    html_template = read_file(template_path, "html")
    md_html = markdown_to_html(md)
    title = extract_title(md_html)
    html_output = html_template.replace("{{ Title }}", title)
    html_output = html_output.replace("{{ Content }}", md_html)
    with open(dest_path, "w") as file:
        file.write(html_output)


def extract_title(markdown):
    pattern = re.compile(r"<h1>(.+)</h1>")
    html = markdown_to_html(markdown)
    try:
        return re.findall(pattern, html)[0]
    except:
        raise Exception("EXTRACT TITLE ERROR: all pages need at least 1 h1 header.")


def read_file(file_path, extension):
    if file_path.split(".")[1] != extension:
        raise Exception("GENERATE PAGE ERROR: from_path is not a md file.")
    else:
        with open(file_path, "r") as file:
            content = file.read()
        return content


def copy_directory(source_directory, dest_directory):
    if os.path.exists(dest_directory):
        shutil.rmtree(dest_directory) # Remove what is currently in the destination dir
    os.mkdir(dest_directory) # Recreate directory
    
    dirs = os.listdir(source_directory) # copy the files from source dir
    for dir in dirs:
        source_path = os.path.join(source_directory, dir)
        dest_path = os.path.join(dest_directory, dir)
        if os.path.isfile(source_path):
            print(source_path, "is being copied to:", dest_path)

            shutil.copy(source_path, dest_path)

            print("copy complete")
            print("---------------------------------------------------------------------------------------------------------------------")
        else:
            copy_directory(source_path, dest_path)
        
            


if __name__ == "__main__":
    main()