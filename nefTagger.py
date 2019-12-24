import csv, re, sys, argparse, fnmatch, os, glob, fileinput

parser = argparse.ArgumentParser(description='Simple Text File Parser')
parser.add_argument('--path', action="store", dest='path', default='.')
parser.add_argument('--live', action="store_true", dest='live')
parser.add_argument('--recursive', action="store_true", dest='recursive')
parser.add_argument('--tagBase', action="store_true", dest='tagBase')
parser.add_argument('--overwrite', action="store_true", dest='overwrite')
parser.add_argument('--merge', action="store_true", dest='merge')
args = parser.parse_args()

if (args.merge and args.overwrite):
    print 'ERROR: cannot use both overwrite and merge flags'
    sys.exit()

if args.recursive :
    matches = []
    for root, dirnames, filenames in os.walk(args.path):
        for filename in fnmatch.filter(filenames, '*.txt'):
            matches.append(os.path.join(root, filename))
else:
    matches = glob.glob(args.path + '/*.txt')

regString = "(<year>.+</year>)(<tag>(.+)</tag>)?"
reg = re.compile(regString, re.IGNORECASE)

for file in matches:
    baseDir =  os.path.basename(os.path.dirname(file))
    if ((os.path.dirname(file) == args.path) and (args.tagBase == True)) or (os.path.dirname(file) != args.path):
        print 'DEBUG: checking file {0} in {1}'.format(os.path.basename(file), baseDir)
        with open(file, 'r+') as fd:
            contents = fd.readlines()
            for index, line in enumerate(contents):
                lineReg = re.search(reg, line)
                if lineReg:
                    replacement = lineReg.group(0)
                    if (lineReg.group(2)):
                        if args.overwrite:
                            replacement = '{0}<tag>{1}</tag>'.format(lineReg.group(1), baseDir)
                            print 'DEBUG: Overriding {0} with existing tags {1} with {2} '.format(lineReg.group(0), lineReg.group(3), replacement)
                        elif args.merge:
                            replacement = '{0}<tag>{1},{2}</tag>'.format(lineReg.group(1),lineReg.group(3),baseDir)
                            print 'DEBUG: Merging {0} with existing tags {1} with {2} '.format(lineReg.group(0), lineReg.group(3), replacement)
                        else:
                            print 'DEBUG: Found exiting tags {0}, skipping'.format(lineReg.group(3))
                    else:
                        replacement = '{0}<tag>{1}</tag>'.format(lineReg.group(1),baseDir)
                        print 'DEBUG: Adding tag {0} to {1}'.format(replacement, lineReg.group(0))
                    newLine = line.replace(lineReg.group(0), replacement)
                    if (args.live):
                        contents[index] = newLine
            fd.seek(0)
            fd.writelines(contents)
            fd.close()