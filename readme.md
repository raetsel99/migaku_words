# migaku_words

This is a quick an dirty script to allow you to import your known or learning workds into the Migaku dictionary from a source other than anki.

Once you have generated your file use the Import from Backup option in the Migaku Words List screen. (Be sure to take a backup before you run the import just in case)

## usage example

```
python3 migaku_words.py -i Migaku_Word_List_fr_2022_12_19.json -c known_words.csv -j Migaku_import.json -s 2
Data written to Migaku_import.json. Be sure to backup Migaku before importing
```

## arguments
```
  -h, --help            show this help message and exit
  -i JSON_INPUT, --json_input JSON_INPUT
                        Option source file of existing backup to append to
  -c CSV_FILE, --csv_file CSV_FILE
                        Source file of csv file of words to add
  -j JSON_OUTPUT, --json_output JSON_OUTPUT
                        Destination file for output
  -s STATUS, --status STATUS
                        Status for all words in CSV file,1=learning, 2=known
  -d, --debug           Show before and after and words being added
```