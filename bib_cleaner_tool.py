import bibtexparser

def load_bib_file(file_path):
    """Load the .bib file and return a BibDatabase object."""
    with open(file_path, 'r') as bib_file:
        bib_database = bibtexparser.load(bib_file)
    return bib_database

def remove_duplicates(bib_database):
    """Remove duplicate entries from the BibDatabase object."""
    unique_entries = []
    seen_titles = set()  # To track titles or another unique field

    for entry in bib_database.entries:
        title = entry.get('title', '').lower().strip()

        if title not in seen_titles:
            unique_entries.append(entry)
            seen_titles.add(title)

    return unique_entries

def save_bib_file(entries, output_file):
    """Save the non-redundant entries to a new .bib file."""
    db = bibtexparser.bibdatabase.BibDatabase()
    db.entries = entries
    
    writer = bibtexparser.bwriter.BibTexWriter()
    with open(output_file, 'w') as bib_file:
        bib_file.write(writer.write(db))

def process_bib_file(input_file, output_file):
    """Process the input .bib file to remove duplicates and save a new file."""
    bib_database = load_bib_file(input_file)
    unique_entries = remove_duplicates(bib_database)
    save_bib_file(unique_entries, output_file)
    print(f"Non-redundant bibliography saved to {output_file}")

# Example usage
if __name__ == "__main__":
    input_bib = input("Enter the path to the .bib file: ")
    output_bib = input("Enter the path to save the non-redundant .bib file: ")
    process_bib_file(input_bib, output_bib)
