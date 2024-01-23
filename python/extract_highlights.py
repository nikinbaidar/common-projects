import os
import sys
import sqlite3
import pathlib
import re
from .sioyek import Sioyek, clean_path

LOCAL_DATABASE_FILE = None
SHARED_DATABASE_FILE = None
SIOYEK_PATH = None

SELECT_DOCUMENT_HIGHLIGHTS_QUERY = "SELECT * FROM highlights WHERE document_path = ?"
INSERT_NEW_DOCUMENT_HASH_QUERY = "INSERT INTO document_hash (path, hash) VALUES (?, ?)"

def extract_highlights(sioyek_path, local_database, shared_database, file_path):
    sioyek = Sioyek(sioyek_path, local_database, shared_database)

    # Open SQLite3 databases
    with sqlite3.connect(local_database) as local_db:
        cursor_local = local_db.cursor()

        doc_path = clean_path(file_path)
        doc_dir = os.path.join(os.path.expanduser("~"), "projects/notes/_highlights")
        doc_base_file_name = os.path.basename(doc_path).split('.')[0]
        new_file_name = f"{doc_base_file_name}.txt"
        new_file_path = str(pathlib.Path(doc_dir) / new_file_name).replace('\\', '/')

        doc = sioyek.get_document(doc_path)
        document_highlights = doc.get_highlights()
        if document_highlights != []:
            with open(new_file_path, "w") as file:
                pattern = r'(Highlight of type )([a-z])(:)'
                file.writelines([re.sub(pattern, r'[\2]', str(item)) 
                                 + "\n" * 2 for item in document_highlights])


def main():
    if len(sys.argv) > 1:
        global SIOYEK_PATH, LOCAL_DATABASE_FILE
        SIOYEK_PATH = clean_path(sys.argv[1])
        LOCAL_DATABASE_FILE = clean_path(sys.argv[2])
        SHARED_DATABASE_FILE = clean_path(sys.argv[3])
        file_path = clean_path(sys.argv[4])
        extract_highlights(SIOYEK_PATH, LOCAL_DATABASE_FILE, SHARED_DATABASE_FILE, file_path)

if __name__ == '__main__':
    main()
