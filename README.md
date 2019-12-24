# Simple CSV File Tagger

This program is intended to search through a directory of text files, looking for a particular string. If the string is contained in the file, a string is appended to the end of the file.

## Using the script

`python tagger.py --path example/files --csv example/source.csv --appendType dynamic --appendValue CODE`

### Parameters

#### path

Pass in a relative or absolute path where your text files are contained. 

Default: `.`

`python tagger.py --path /Users/me/Documents/text_files`

#### recursive

traverses your directory recursivelly

Default: `false`

`python tagger.py --path /Users/me/Documents/text_files --recursive`

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

By default script prints out all the debug statements without modifying any files. Live flag executes changes.

Default: `false`

`python tagger.py --appendValue <tagged> --live`

`python tagger.py --appendType dynamic --appendValue TITLE --live`

#### dupe

Be default the script will use the first value it finds that matches the key in the source.csv. However if you want to use all values, you can pass in the dupe flag. 

Example:

CSV:
```CSV
CODE,TAG
FF00000,abc
FF00000,123
FF00000,xyz
```

Function:
```python
python tagger.py --appendType dynamic --appendValue TAG --dupe
```

Output:
```
abc,123,xyz
```

#### dupeDelimiter

If using dupe mode, the entries will be joined by a delimiter. By default the delimiter is a comma, but you can use the optional flag dupeDelimiter to pass in any delimiter you want:

Function:
```python
python tagger.py --appendType dynamic --appendValue TAG --dupe --dupeDelimiter ": "
```

Output:
```
abc: 123: xyz
```

Default: `,`

## batchTagger.py

To help with multiple executions of the tagger script, we also have the batchTagger.py script. This script relies on a batch.csv file being passed in that has a NAME and ARGS columns. The column names aren't important but the order is. batchTagger.py will exceute each set of arguments in the batch file. 

Example:

```python
python batchTagger.py --csv example/batch.csv
```

## nefTagger.py

This is a simple utility for adding tags into a nef text file. 

`python nefTagger.py --path example/images --recursive --overwrite --tagBase`

### Parameters

#### path

Pass in a relative or absolute path where your text files are contained. 

Default: `.`

`python nefTagger.py --path example/images`

#### recursive

traverses your directory recursivelly

Default: `false`

`python nefTagger.py --path example/images --recursive `

#### live

By default script prints out all the debug statements without modifying any files. Live flag executes changes.

Default: `false`

`python nefTagger.py --path example/images --recursive --live`

#### tagBase

Flag to switch tagging files in the base directory. By default no files will be changed in the base directory of the path argument.

Default: `false`

`python nefTagger.py --path example/images --recursive --tagBase`

#### overwrite

In an existing `<tag>` is found in the file, the script will skip editing it, unless overwrite is passed in. In this case the tag will be replaced with the directory name. Cannot be used with --merge

Default: `false`

`python nefTagger.py --path example/images --recursive --tagBase --overwrite`

#### merge

In an existing `<tag>` is found in the file, the script will skip editing it, unless merge is passed in. Merge will add the directory name to the exisitng tag. It does not dedupe so you may end up with the same tag repeated.

Default: `false`

`python nefTagger.py --path example/images --recursive --tagBase --merge`