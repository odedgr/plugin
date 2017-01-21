import re
import os
import glob

def find_javadoc(filename=None):
    """
    Find the javadoc string of the top-level class in the file.

    :param filename: Name of file from which to extract the javadoc
    :return: match object of the javadoc
    """
    pattern_multiline_with_javadoc_upto_class = "(\/\*\*.*?\*\/).*?class"

    with open(filename) as file_content:
        content = file_content.read()

    return re.search(pattern_multiline_with_javadoc_upto_class, content, re.DOTALL)

def find_imports(filename=None):
    """
    Find the top-level class declaration in the file.

    :param filename: Name of file from which to extract the class declaration
    :return: match object of the class declaration
    """
    # pattern_imports = '.*package\s*(.*)$'
    
    pattern_imports = "^[\s]*package.*[\n]?(?![\n\r]{1,2}import)"

    pattern_with_annotations =  "@.*?class"
    # pattern_imports = "^.*?class"

    with open(filename) as file_content:
        content = file_content.read()

    # print("find with annotatins: ", re.search(pattern_with_annotations, content, re.DOTALL).group(0))

    print("find class: \n" + re.search(pattern_imports, content, re.DOTALL).group(0))
    for line in content
    return re.search(pattern_imports, content, re.DOTALL)

def extract_javadoc(filename=None):
    """
    Extract the javadoc string from the top-level class in the file.

    :param filename: Name of file from which to extract the javadoc
    :return: Javadoc string from top-level class in given file
    """
    if filename is None:
        print("no filename provided")
        return

    match = find_javadoc(filename)
    if match is None:
        return None

    javadoc = match.group(1)

    return javadoc


def has_tag(javadoc=None, tag=None):
    if tag is None:
        raise ValueError('No tag supplied')

    if not re.search('@[a-zA-Z]+', tag):
        raise ValueError('invalid tag format')

    if javadoc is None:
        return False

    res = True if re.search(tag, javadoc, re.DOTALL) else False
    return res


def has_since_tag(javadoc=None):
    """
    Check if the given javadoc string contains the '@since' tag or not.

    :param javadoc: string to be searched for the '@since' tag
    :return: True if given javadoc string containts the '@since' tag, 'False' otherwise
    """

    if javadoc is None:
        return False

    return has_tag(javadoc, "@since")


def has_author_tag(javadoc=None):
    """
    Check if the given javadoc string contains the '@author' tag or not.

    :param javadoc: string to be searched for the '@since' tag
    :return: True if given javadoc string containts the '@since' tag, 'False' otherwise
    """

    if javadoc is None:
        return False

    return has_tag(javadoc, "@author")

def add_tags(file=None, javadoc=None, since=None, author=None):
    """
    Adds @since and/or @author tags to the given file .
    :param file: file to add tags to
    :param javadoc: javadoc string from the top-level class in the file
    :param since: since string to add to the '@since' tag, 'None' if no need to add since
    :param author: author string to add to the '@author' tag, 'None' if no need to add author
    """

    # no file specified or no need to add any tags
    if file is None or (since is None and author is None): 
	    print("for file:", file, "not adding tags")
	    return
    if javadoc is None:
        javadoc="/**\n*/\n"
    if since is not None and author is not None:
        javadoc = re.sub("\/\*\*","/**\n * @author " + author + "\n * @since " + since ,javadoc)
    elif since is not None:
        javadoc = re.sub("\/\*\*","/**\n * @since " + since,javadoc)
    else: #author is not None
        javadoc = re.sub("\/\*\*","/**\n * @author " + author ,javadoc)
    with open(file, 'r+') as f:
        java_doc_location = find_javadoc(file)
        original_text = f.read()
        if java_doc_location is None:
            # this is when no java doc is present
            imports = find_imports(file)
            before_doc = original_text[:imports.end()]
            after_doc = original_text[imports.end():]

        else:
            class_def_len = len(java_doc_location.group(0)) - len(java_doc_location.group(1))
            before_doc = original_text[:java_doc_location.start()]
            after_doc = original_text[java_doc_location.end()-class_def_len:]
        text = before_doc + javadoc + after_doc
        f.seek(0)
        f.write(text)
        f.truncate()


def update_tags(since=None, author=None):
    """
    Adds @since and/or @author tags to all files in the current directory recursively.
    :param since: since string to add to the '@since' tag, 'None' if no need to add since
    :param author: author string to add to the '@author' tag, 'None' if no need to add author
    """

    for file in glob.glob('./**/*.java', recursive=True):
		# print(file)
        sinceToUse = since
        authorToUse = author
        jdoc = extract_javadoc(file)
        if (has_since_tag(jdoc)):
			#print("file", file, "has since tag")
            sinceToUse = None
        if (has_author_tag(jdoc)):
            #print("file", file, "has author tag")
            authorToUse = None
        add_tags(file, jdoc, sinceToUse, authorToUse)

if __name__ == '__main__':
    update_tags("1.6", "Avner")
