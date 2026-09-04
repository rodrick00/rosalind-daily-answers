# Rosalind: Computing GC Content
# Input: FASTA-format DNA strings -> Output: ID + GC% of the sequence with highest GC content

def main():
    with open("rosalind_gc.txt") as file:
        fasta_text = file.read()
        dna_dict = parse_fasta(fasta_text)
        best_id,best_gc_percent = highest_gc(dna_dict)
        print(best_id)
        print(best_gc_percent)

def parse_fasta(fasta_text):
    dna_dict = {}
    current_id = ""
    lines = fasta_text.strip().split("\n")
    for every_line in lines:
        every_line = every_line.strip()
        if every_line.startswith(">"):
            current_id = every_line[1:]
            dna_dict[current_id] = ""
        else:
            dna_dict[current_id] += every_line
    return dna_dict

def gc_content(a_dna):
    gc_count = a_dna.count("G")+ a_dna.count("C")
    total_len = len(a_dna)
    percentage = (gc_count/total_len)*100
    round_percentage = round(percentage,6)
    return round_percentage

def highest_gc(dna_dict):
    highest_gc_content_id = ""
    highest_gc_percentage = 0 
    for key,value in dna_dict.items():
        individual_gc_percent= gc_content(value)
        if individual_gc_percent > highest_gc_percentage:
            highest_gc_content_id = key
            highest_gc_percentage = individual_gc_percent
    return highest_gc_content_id,highest_gc_percentage

if __name__ == "__main__":
      main()
        

