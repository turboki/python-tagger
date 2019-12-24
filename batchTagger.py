import csv, re, sys, argparse, fnmatch, os, glob

parser = argparse.ArgumentParser(description='Batch Tagger')
parser.add_argument('--csv', action="store", dest='csv', default='batch.csv')
args = parser.parse_args()

with open(args.csv, mode='r') as infile:
    reader = csv.reader(infile)
    headers = next(reader, None)
    for rows in reader:
        k = rows[0]
        v = rows[1]
        print "Executing script: " + k
        print "------------------------------------"
        os.system("python tagger.py " + v)
        print ""