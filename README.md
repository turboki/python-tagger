# Simple CSV File Tagger

This program is intended to search through a directory of text files, looking for a particular string. If the string is contained in the file, a string is appended to the end of the file.

## Using the script

`python tagger.py --path example/files --csv example/source.csv --appendType dynamic --appendValue CODE`

### Parameters

#### path

Pass in a relative or absolute path where your text files are contained. 

Default: `.`

`python tagger.py --path /Users/me/Documents/text_files`

#### csv

Pass in a relative or absolute path where of your source CSV

Default: `source.csv`

`python tagger.py --csv example/source.csv`

#### appendType

If set to 'dynamic' to attempt to pull the tag from the source CSV, where the column is specified by `appendValue`. If the `appendValue` does not exist as a column, it switches to normal tag mode.

Default: `''`

`python tagger.py --appendType dynamic --appendValue CODE`

#### appendValue

String that is appended to the end of the file if matched. 

Default: `<false>`

`python tagger.py --appendValue <tagged>`

`python tagger.py --appendType dynamic --appendValue TITLE`

#### reg

Regular expression string to match in the file. 

Default: `FF\d{5} \\FF00000, FF12345...`

`python tagger.py --appendType dynamic --appendValue CODE --reg ABCDEF\d\d\d\d`

#### live

Prints out all the debug statements without modifying any files. Good to check 

Default: `false`

`python tagger.py --appendValue <tagged> --live true`

`python tagger.py --appendType dynamic --appendValue TITLE`