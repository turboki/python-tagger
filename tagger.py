import csv, glob, re, sys, argparse

parser = argparse.ArgumentParser(description='Simple Text File Parser')
parser.add_argument('--path', action="store", dest='path', default='.')
parser.add_argument('--csv', action="store", dest='csv', default='source.csv')
parser.add_argument('--appendType', action="store", dest='type', default='')
parser.add_argument('--appendValue', action="store", dest='value', default='<false>')
parser.add_argument('--reg', action="store", dest='reg', default='FF\d{5}')
parser.add_argument('--live', action="store_true", dest='live')
args = parser.parse_args()

with open(args.csv, mode='r') as infile:
    reader = csv.reader(infile)
    headers = next(reader, None)
    if args.type == 'dynamic' and args.value in headers:
        mydict = {rows[0]:'<' + rows[headers.index(args.value)] + '>' for rows in reader}
    else:
        mydict = {rows[0]:args.value for rows in reader}

for file in glob.glob(args.path + '/*.txt'):
    print 'DEBUG: checking file {0}'.format(file)
    repValue = args.value
    hasCode = False
    code = ''
    with open(file, 'r+') as f:
        for line in f:
            match = re.search(args.reg, line)
            if match:
                code = match.group()
                if code in mydict:
                    hasCode = True
                    if args.type == 'dynamic':
                        repValue = mydict[code]
                
        if hasCode == True :
            print 'DEBUG: Fount code {0} in {1}'.format(code, file)
            if args.live == True :
                print 'DEBUG: Appending {0}'.format(repValue)
                f.write('\n' + repValue)
            else :
                print 'DEBUG: Dry run - would append {0}'.format(repValue)
        f.close()