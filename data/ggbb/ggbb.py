#!/usr/bin/env python3

import os
import csv

infile = 'ggbb.csv'
outfile = 'submitted.txt'

def add_entry(entry):
  with open(outfile,'a') as f: f.write(f"{entry}\n")
  print(f"iYour submission has been added to the review queue!	.")

query = os.environ['QUERY_STRING']
if(query):
  add_entry(query)

with open(infile, newline='', encoding='utf-8') as f_in:
  reader = csv.DictReader(f_in)
  for row in reader:
    url = row.get('url','')
    since = row.get('since','')
    checked = row.get('checked','')

    parts = url.split(':70/') or '/'

    host = parts[0]

    t = parts[1][:1]
    if (not t in ['0','1']): t = '1'

    selector = parts[1][1:]
    if (selector == ''): selector = '/'

    separator = '                                           '[len(host):]

    line = f"{t}{host}{separator}{since}  {checked}\t{selector}\t{host}"
    print(line)
