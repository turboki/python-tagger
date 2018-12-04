import csv, re, sys, argparse, fnmatch, os, glob

parser = argparse.ArgumentParser(description='Simple Text File Parser')
parser.add_argument('--path', action="store", dest='path', default='.')
parser.add_argument('--csv', action="store", dest='csv', default='source.csv')
parser.add_argument('--appendType', action="store", dest='type', default='')
parser.add_argument('--appendValue', action="store", dest='value', default='<false>')
parser.add_argument('--live', action="store_true", dest='live')
parser.add_argument('--recursive', action="store_true", dest='recursive')
args = parser.parse_args()

with open(args.csv, mode='r') as infile:
    reader = csv.reader(infile)
    headers = next(reader, None)
    if args.type == 'dynamic' and args.value in headers:
        mydict = {rows[0]:'<' + rows[headers.index(args.value)] + '>' for rows in reader}
    else:
        mydict = {rows[0]:args.value for rows in reader}

if args.recursive :
    matches = []
    for root, dirnames, filenames in os.walk(args.path):
        for filename in fnmatch.filter(filenames, '*.txt'):
            matches.append(os.path.join(root, filename))
else:
    matches = glob.glob(args.path + '/*.txt')

for file in matches:
    print 'DEBUG: checking file {0}'.format(file)
    repValue = args.value
    hasCode = False
    code = ''

    with open(file, 'r+') as fd:
        contents = fd.readlines()
        for item in mydict.keys():
            if item in contents[-1]:  # Handle last line to prevent IndexError
                print 'DEBUG: Found code {0} in {1} at end'.format(item, file)
                if args.type == 'dynamic' :
                    repValue = mydict[item]
                if args.live == True :
                    print 'DEBUG: Appending {0}'.format(repValue)
                    contents.append(repValue)
                else :
                    print 'DEBUG: Dry run - would append {0}'.format(repValue)
            else:
                for index, line in enumerate(contents):
                    if item in line and repValue not in contents[index + 1]:
                        print 'DEBUG: Found code {0} in {1} at line {2}'.format(item, file, index + 1)
                        if args.type == 'dynamic' :
                            repValue = mydict[item]
                        if args.live == True :
                            print 'DEBUG: Appending {0}'.format(repValue)
                            contents.insert(index + 1, repValue)
                        else :
                            print 'DEBUG: Dry run - would append {0}'.format(repValue)
                        break
        fd.seek(0)
        fd.writelines(contents)
        fd.close()