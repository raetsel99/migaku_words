import json
import csv
import os
import argparse
from pathlib import Path
import sys

# quick and dirty script to update the words being learned in missingPackagesAndExecutables

def read_json_in(file_in):
    fileIn = open(file_in, 'r')
    return json.loads(fileIn.read())

def import_csv(json_array, file_in, word_status):
    # dummy_data=["test1",2]
    
    with open(file_in, newline='') as csvfile:
        word_reader = csv.reader(csvfile)
        for row in word_reader:
            row.append(word_status)
            json_array.append(row)
     
    return json_array


if __name__ == '__main__':
    # use Path so will work on any OS
    parser = argparse.ArgumentParser(description = "Adds words from csv to a Migaku backup file so it can be imported")
    parser.add_argument('-i','--json_input',type=str,help='Option source file of existing backup to append to')
    parser.add_argument('-c','--csv_file',type=str,help='Source file of csv file of words to add',required=True)
    parser.add_argument('-j','--json_output',type=str,help='Destination file for output',required=True)
    parser.add_argument('-s','--status',type=int,default=2,help='Status for all words in CSV file,1=learning, 2=known')
    args = parser.parse_args()

    # start with a blank array
    migaku_array =[]
    
    # get the input file if present
    if args.json_input:
        agnostic_json_in = Path(args.json_input)
        if os.path.exists(agnostic_json_in):
            migaku_array = read_json_in(agnostic_json_in)
            print(f"json is {migaku_array}")
        else:
            print(f"ERROR E001 could not find file {agnostic_json_in}")
            sys.exit(1)

    if args.status and (args.status <1 or args.status >2):
        print(f"ERROR E002 invalid status {args.status}. 1=learning, 2=known")
        sys.exit(2)
    else:
        word_status = args.status

 

    agnostic_csv_in = Path(args.csv_file)
    if os.path.exists(agnostic_csv_in):
        migaku_array = import_csv(migaku_array,agnostic_csv_in,word_status)
    else:
        print(f"ERROR E003 could not find file {agnostic_csv_in}")
        sys.exit(3)

    print(f"migaku array is now: {migaku_array}")

    agnostic_json_out=Path(args.json_output)
    with open(agnostic_json_out, "w") as write_file:
        json.dump(migaku_array, write_file)

    print(f"Data written to {agnostic_json_out}. Be sure to backup Migaku before importing")





 

