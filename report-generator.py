#! /usr/bin/env python3
import csv
import urllib.request
from datetime import datetime

def url_2_csv(url, filename):
  urllib.request.urlretrieve(url, filename)

def csv_2_dicts(csv_file):
  with open(csv_file) as f:
    dicts = [{key: value for key, value in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]
  return dicts  

def report_builder(filename, names, head_count, incs):
  my_ip = urllib.request.urlopen("https://api.ipify.org/").read().decode('utf8')
  with open(filename, 'w') as f:
    f.write("Report Creted On " + datetime.now().strftime("%m/%d/%Y") + " from " + str(my_ip) + "\n\n")
    f.write("Total number of employees: " + str(head_count) + "\n\n") 
    f.write("Company names that contain the word Inc:" + "\n")
    for name in sorted(incs):
      f.write("* " + name + "\n")   
    f.write("\nAll names, sorted:" + "\n")
    for name in sorted(names):
      f.write("* " + name + "\n")
 
def main():
  url_2_csv("https://media.githubusercontent.com/media/datablist/sample-csv-files/main/files/organizations/organizations-100.csv", "/tmp/source-file.csv")
  dicts = csv_2_dicts("/tmp/source-file.csv")
  company_names = []
  head_count = 0
  incs = []
  for i in dicts:
    company_names.append(i['Name'])
    head_count += int(i['Number of employees'])
    if ' inc' in i['Name'].lower():
      incs.append(i['Name'])

  with open("/tmp/names.txt", 'w') as f:
    for name in company_names:
      f.write(name + "\n")

  with open("/tmp/employee_count.txt", 'w') as f:
    f.write("Total number of employees: " + str(head_count) + "\n")
  
  with open("/tmp/lines-with-inc.txt", 'w') as f:
    for name in incs:
      f.write(name + "\n")
  
  report_builder("/tmp/final-report.txt", company_names, head_count, incs)

if __name__ == "__main__":
  main()
