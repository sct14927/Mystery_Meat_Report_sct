#!/bin/bash

# Define the output .fasta file.
finaloutput="all_sample_sequences.FASTA"

# Define a counter; to check that all sample files are present.
checker=0

# Remove old copies of the output if present in the directory.
rm -f "$finaloutput"

# First we will add an ID for Sample A to the output file
echo ">[organism=Sample_A]" >> "$finaloutput"
           
# Now we shall count, clean and concatenate the files for Sample A:
# Start a for loop.
for file in ./raw_sequences/sampleA_part*.FASTQ; do

# Count the number of Sample A files present
if [ -e "$file" ]; then
	checker=$((checker + 1))
fi

# Select all text from the file, excluding the line starting with @, then remove the .fastq quality data, then remove the + sign, and finally remove any spaces.
	org=$(grep -v '^@' "$file" | sed '/^[IH#123456789].*/d' | sed '/+/d' | tr -d ' ')
# Remove new lines and append the resulting string to the output file.
	echo "$org" | tr -d '\n' >> "$finaloutput"
# The for loop is complete.
done

# Add a newline in the output for the next sample, and add next sample ID.
echo "" >> "$finaloutput"
echo "" >> "$finaloutput"
echo ">[organism=Sample_B]" >> "$finaloutput"

# Repeat steps (done for Sample A) for Sample B:
for file in ./raw_sequences/sampleB_part*.FASTQ; do

if [ -e "$file" ]; then
	checker=$((checker + 1))
fi

	org=$(grep -v '^@' "$file" | sed '/^[IH#123456789].*/d' | sed '/+/d' | tr -d ' ')
	echo "$org" | tr -d '\n' >> "$finaloutput"
done

echo "" >> "$finaloutput"
echo "" >> "$finaloutput"
echo ">[organism=Sample_C]" >> "$finaloutput"

# Repeat steps (done for Sample A) for Sample C:
for file in ./raw_sequences/sampleC_part*.FASTQ; do

if [ -e "$file" ]; then
	checker=$((checker + 1))
fi

	org=$(grep -v '^@' "$file" | sed '/^[IH#123456789].*/d' | sed '/+/d' | tr -d ' ')
	echo "$org" | tr -d '\n' >> "$finaloutput"
done

echo "" >> "$finaloutput"
echo "" >> "$finaloutput"
echo ">[organism=Sample_D]" >> "$finaloutput"

# Repeat steps (done for Sample A) for Sample D:
for file in ./raw_sequences/sampleD_part*.FASTQ; do
if [ -e "$file" ]; then
	checker=$((checker + 1))
fi

	org=$(grep -v '^@' "$file" | sed '/^[IH#123456789].*/d' | sed '/+/d' | tr -d ' ')
	echo "$org" | tr -d '\n' >> "$finaloutput"
done

# Add two newlines to make room for reference sequences when they are concatenated.
echo "" >> "$finaloutput"
echo "" >> "$finaloutput"

#Check how many or if all sample files were present and included in output
if [ $checker -eq 0 ]; then
	echo "None of the sample files were located. Please check that you are in the correct directory and that the sample files haven't been moved."
elif [ $checker -lt 11 ]; then
	echo "One or more of the samples could not be located. Please check that you are in the correct directory and that the sample files haven't been moved."
else
	echo "The sample sequences have been succesfully saved in a new file called all_sample_sequences.fasta."
fi
