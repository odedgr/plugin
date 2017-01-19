import re


def extract_javadoc(filename=None):
    """
    Extract the javadoc string from the top-level class in the file.

    :param filename: Name of file from which to extract the javadoc
    :return: Javadoc string from top-level class in given file
    """
    if filename is None:
        print("no filename provided")
        return

    print('extracting Javadoc from {}'.format(filename))
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
    print(javadoc)
    if re.search("@since", javadoc, re.DOTALL):
        print("ALREADY HAS THE @since TAG")
    else:
        print("DOES NOT HAVE THE @since TAG")

    return javadoc

if __name__ == '__main__':
    extract_javadoc('AllTags.java')
    extract_javadoc('NoTags.java')
