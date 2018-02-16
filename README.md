Context
=======

You have a big file and you want to extract information from it, and correlate them
with 3rd party services. You get a new file every 5 min.

Processing all that in one single process will take too much time,

This file is text, so you can read it easily but the content is made of multiline blocks.

Use the `validate.sh` script to make sure the files tou generate are the same as the source files.


Step 1
------

Figuring out a separator write a file split it in 10 independent files of the same-ish size

Tools required:
* `vim` (look at the file -> find a separator)
* `grep` (figure out how many entries we have
* `wc` (count the amout of blocks)
* `bc` (compute things -> amout of blocks /file)

Write some code to do that.

Step 2
------

Rewrite it, but better:
* function with parameters (`source_file_name`, `separator`, `output_name`)
* make it a script (see `__main__`, `__name__`)

Step 3
------

What about the file gets lot bigger? Or the size fluctuates?
    (i.e we need to dynamically figure out how many blocks we want in each file)

Or we want to split it in more/less files?
    (i.e. we have more CPUs at hand and can process more files at once)

Python modules
* `re` (regex, replaces `grep`)

Method:
* `len` (replaces `wc`)

1. count the total amount of blocks (in another method)
2. Divide it by the number of files
3. Update the `file_split` method accordingly


Step 4
------

Do we care about the number of entries? Or the number of files?

===> Update your code to be able to pass a number of file as parameter


Step 5
------

We're getting there. Let's do some refactoring now to make the code more pythonesque.

* use the `with open ... as ...:` syntax when possible
* Use format instead of concatenating text
* Use `round` on entries_per_file
* Add some logging (see the `logging` module)
* Use `argparse` to make the script more flexible

Step 6
------

Let's think a bit how we can make this code more efficient.

Why do we compute the mount of entries? Do we need that? What about using the size of the file instead?

Methods:
* `file.seek`
* `file.tell`


Step 7
------

Let's make it better:
* Only open the source file once
* Open as binary file

Step 8
------

* Fetch new files when there is something available
    * http://data.ris.ripe.net/rrc00/latest-bview.gz
    * ===> http://docs.python-requests.org/en/master/api/#requests.head & Last-Modified

* Use the library to generate text files:
    * https://bitbucket.org/ripencc/bgpdump/downloads/ (Installation details: https://bitbucket.org/ripencc/bgpdump/wiki/Home.wiki#!building)

    ```
    sh ./bootstrap.sh
    make
    ./bgpdump -T
    ```

    ./bgpdump -O ../data/latest-bview.txt  ../data/original/latest-bview.gz

Step 9 ++
---------

If you're fast and bored:
* Make it a class (with comments)
* Yield pseudo files (`BytesIO`) instead of writing the files on the disk

