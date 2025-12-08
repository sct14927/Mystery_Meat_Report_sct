import os
import warnings
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import BiopythonWarning
warnings.simplefilter('ignore', BiopythonWarning)

# BEFORE YOUR START:
# Please ensure that you have biopython installed prior to running this
# script. Type "pip install biopython" if required.

# Biopython warns the user during sequence translation when a sequence
# is not divisible by 3. This means that the last nucleotides in the
# that sequence will be ignored. This is not an issue for this analysis,
# and therefore the warning was turned off because it might confuse users.

# Before starting, first check whether the required files are present in
# the directory/folder that you have open.

checker = 0


if os.path.isfile('all_sample_sequences.FASTA'):
    checker += 1
else:
    print("The sample sequence file is missing. Please ensure you are in the")
    print("correct directory and have already run the custom BASH script.")

if os.path.isfile('reference_sequences.FASTA'):
    checker += 1
else:
    print("The reference sequence file is missing. Please ensure you are in the")
    print("correct directory and have not moved the file.")

if checker == 2:
    print("The sample and reference sequences have been succesfully combined")
    print("and output as the new file allseq.FASTA")
    print("")

# Create an empty list for storage of the amino acid sequence output.
complete_set_of_sequences = []

# Now create a new file with the sample and reference sequences.
filenames = ['all_sample_sequences.FASTA', 'reference_sequences.FASTA']
with open('all_seq.FASTA', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

# Create a loop to cycle through the individual sequences.
for record in SeqIO.parse("all_seq.fasta", "fasta"):

    # First extract the scientific name of the species. This presumes
    # the title has been given in FASTA format. The species name must
    # be contained within brackets like this [organism=Bos taurus].
    start = record.description.find("[organism=") + len("[organism=")
    end = record.description.find("]", start)
    # Now remove spaces and replace them with underscores.
    latin_name = record.description[start:end].replace(
        " ", "_")

    # Now lets name the variables to be used within the loop.

    # This will represent the individual sequence in each loop.
    dna_seq = record.seq

    # This will store the longest open reading frame (ORF) that is
    # translated.
    long_frame = ""

    # This loop will translate the individual sequences in all three
    # frames.
    for frame in range(3):

        # Translate the sequences, specifying they are mitochondrial
        # DNA (i.e., table = 2) and that it should not exclude stop
        # codons.
        protein = dna_seq[frame:].translate(table=2, to_stop=False)

        # Next split the sequence into open reading frames using the
        # stop codons ("*").
        fragments = str(protein).split("*")

        # Now find which of these represents the longest open reading
        # frame.
        longest_fragment = max(fragments, key=len)

        # This loop will compare the longest fragments for each of the
        # three frames, with the longest being assigned to long_frame.
        if len(longest_fragment) > len(long_frame):
            long_frame = longest_fragment

    # The fragment string must now be converted into a Seq object.
    best_protein = Seq(long_frame)

    # Then create a new SeqRecord for your longest fragment.
    protein_record = SeqRecord(
        best_protein,
        id=latin_name,
        description=latin_name,
    )

    # And append it to your list of translated sequences.
    complete_set_of_sequences.append(protein_record)

    # Finally, write the list to an output file.
    SeqIO.write(complete_set_of_sequences,
                "translated_sequences.FASTA", "fasta")

print("Good news! Your sequences have been translated. They can be")
print("located in the new file translated_sequences.FASTA.")
print("They are now ready for upload to MUSCLE 5 for alignment.")
