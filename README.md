# Git Annotator - @since and @author annotations Adder
Mini-Project for Python 3.5+ on linux (for 95 points)

Avner Elizarov (304848484)
Oded Greenberg (200464956)


## Short Description
This project's goal is to create a **simple-to-use** plugin that is **easily installed**, which allows users to add @since and @author tags "automatically" in *.java source files. Currently, the plugin is designed to insert mentioned tags only in files where they are not yet present, and only for the top-level class defined in the *.java file.

## Long Description
The plugin receives 2 optional arguments - a since argument and an author argument. For example, specifying the argument "--since" will add a @since annotation to the javadoc of all top level java classes contained in the current project, which don't already have this annotation (e.g. @since). when followed by a value (for example,  "--since today") this value will follow the annotation (e.g. @since today). If no value is specified then a default value is used. 
Default values are:
 - @since: Currnet date in the format dd-mm-yyyy.
 - @author: Username of currently logged-in user.

The user must specify at least one argument (since and/or author) for the plugin to do something. For each top level java class contained in the project, a javadoc is created (if it doesn't exist) and the annotations specified as arguments to the plugin are added to it (if they aren't already present) with the given values (or the default ones in case a value wasn't specified).

The main difficulty in the project was finding the javadoc (only) of the top level java classes and inserting the annotations appropriately. To solve that, we used regular expressions, with a modifier to indicate for "un-greedy" matching of patterns.
Another difficulty was placing the javadoc correctly in cases where no javadoc previously existed.
To do that, we located the class definition using regular expressions and added the java doc before the definition.

The plugin is installed using a standard Makefile, and runs as a Git "command" from within a terminal - as simple and straightforward as "$ git annotator --since 1.7 --author myself".

## The Alogorithm
1. parse the command line and extract the arguments.
2. For each java file in the current project:
    1. Find the javadoc of the top level class defined in the file.
        1. If javadoc doesn't exist, create an empty one.
    2. Add the tags specified in the arguments with the values given (or default ones).
    3. rewrite the file with the updated javadoc in it's appropriate location.


## Pre-requisites
1. Linux, preferably Ubuntu 12.04+
2. Python 3.5+

## Installation
1. Download the git-annotator.tar.gz file to any local directory.
2. Untar the file: "$ tar zxf git-annotator.tar.gz"
3. Install using the supplied Makefile: "$ sudo make install" - The sudo is essential!!

## Usage
1. Open a terminal and 'cd' to the project's root directory (containing the '.git' directory)
2. To get detailed usage information printed back in the terminal, use the '-h' flag, e.g: run "$ git annotator -h"
3. To add a '@since' tag (annotation):
- $ git annotator --since [SINCE] where SINCE can be an arbitrary value (w/o whitespaces)
4. To add a '@author' tag (annotation):
- $ git annotator --author [AUTHOR] where SINCE can be an arbitrary value (w/o whitespaces)


## Examples
A few short examples for input files can be found under the tests directory.
To check the examples you should create a git project ("$ git init") and copy the input files into the directory.
You can put some of the files in a sub direcetory under the main directory (all nested directories are checked). 
Open a terminal, 'cd' to the root git directory you created and type one of the following commands (each command is followed by its output and an explanation):
- "$ git annotator --since" :
    ```
	Adding since = 24-1-2017
	Processing file './test/AuthorTag.java'... @since => 24-1-2017 
	Processing file './test/ImportsAndAnnotationNoJavadoc.java'... @since => 24-1-2017
	Processing file './test/AllTags.java'... skipping
	Processing file './test/NoTagsWithJavadoc.java'... @since => 24-1-2017
	Processing file './test/SinceTag.java'... skipping
	Processing file './test/NoJavadoc.java'... @since => 24-1-2017
	Done
    ```

    - AllTags.java had all tags defined so it's javadoc hasn't changed.
    SinceTag.java had the @since tag defined so it's javadoc hasn't changed.
    - NoTagsWithJavadoc.java and AuthorTag.java had javadoc but didn't have the @since tag defined so it was added with the defualt value (current date) since no value was given.
    - ImportsAndAnnotationNoJavadoc.java and NoJavadoc.java didn't have javadoc at all so javadoc with the @since tag was added with the defualt value (current date).

- "$ git annotator --since today" :
    ```
	Adding since = today
	Processing file './test/AuthorTag.java'... @since => today 
	Processing file './test/ImportsAndAnnotationNoJavadoc.java'... @since => today
	Processing file './test/AllTags.java'... skipping
	Processing file './test/NoTagsWithJavadoc.java'... @since => today
	Processing file './test/SinceTag.java'... skipping
	Processing file './test/NoJavadoc.java'... @since => today
	Done
    ```

    - Same as before with a value defined by the user ("today") instead of the default value (current date).

- "$ git annotator --author" :
    ```
	Adding author = oded
	Processing file './test/AuthorTag.java'... skipping
	Processing file './test/ImportsAndAnnotationNoJavadoc.java'... @author => oded
	Processing file './test/AllTags.java'... skipping
	Processing file './test/NoTagsWithJavadoc.java'... @author => oded 
	Processing file './test/SinceTag.java'... @author => oded 
	Processing file './test/NoJavadoc.java'... @author => oded 
	Done
    ```

    - AllTags.java had all tags defined so it's javadoc hasn't changed.
    AuthorTag.java had the @author tag defined so it's javadoc hasn't changed.
    - NoTagsWithJavadoc.java and SinceTag.java had javadoc but didn't have the @author tag defined so it was added with the defualt value (Username of currently logged in user - "oded" ).
    - ImportsAndAnnotationNoJavadoc.java and NoJavadoc.java didn't have javadoc at all so javadoc with the @author tag was added with the defualt value.

- "$ git annotator --author Avner" :
    ```
    Adding author = Avner
	Processing file './test/AuthorTag.java'... skipping
	Processing file './test/ImportsAndAnnotationNoJavadoc.java'... @author => Avner
	Processing file './test/AllTags.java'... skipping
	Processing file './test/NoTagsWithJavadoc.java'... @author => Avner 
	Processing file './test/SinceTag.java'... @author => Avner 
	Processing file './test/NoJavadoc.java'... @author => Avner 
	Done
    ```

    - Same as before with a value defined by the user ("Avner") instead of the default value.

## GitHub repository
https://github.com/odedgr/plugin