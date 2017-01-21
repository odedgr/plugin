import re
import os
import glob
def extract_javadoc(filename=None):
    """
    Extract the javadoc string from the top-level class in the file.

    :param filename: Name of file from which to extract the javadoc
    :return: Javadoc string from top-level class in given file
    """
    if filename is None:
        print("no filename provided")
        return

    #print('extracting Javadoc from {}'.format(filename))
    pattern_multiline_with_javadoc_upto_class = "(\/\*\*.*?\*\/).*?class"

    with open(filename) as file_content:
        content = file_content.read()

    match = re.search(pattern_multiline_with_javadoc_upto_class, content, re.DOTALL)
    # print(match.group(0))
    # print(match.group(1))
    # print(match.group())
    # match2 = re.search("\/\*\*.*\*\/", match.group(), re.DOTALL)
    # print(match2.group())

    # javadoc = match2.group()
    javadoc = match.group(1)
    #print('Extracted Javadoc:\n {}'.format(javadoc))
    # if re.search("@since", javadoc, re.DOTALL):
    #     print("ALREADY HAS THE @since TAG")
    # else:
    #     print("DOES NOT HAVE THE @since TAG")

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
    print("for file:", file, "- adding_since:", since, ",adding_author:", author)
    # f=open(file,'w')
    # lines=f.readlines()
    # f.close()
    # f=open(file,'w')
    # for line in lines:
    #     newline = "No you are not"
    #     f.write(newline)
    # f.close()



def update_tags(since=None, author=None):
    """
    Adds @since and/or @author tags to the given file .
    :param since: since string to add to the '@since' tag, 'None' if no need to add since
    :param author: author string to add to the '@author' tag, 'None' if no need to add author
    """

    for file in glob.glob('./*.java'):
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
    # jdoc = extract_javadoc('AllTags.java')
    # print('has @since: {}'.format(has_tag(jdoc, '@since')))
    # print('has @author: {}'.format(has_tag(jdoc, '@author')))
    # jdoc = extract_javadoc('NoTags.java')
    # print('has @since: {}'.format(has_tag(jdoc, '@since')))
    # print('has @author: {}'.format(has_tag(jdoc, '@author')))
    update_tags('1.6','Avner')
