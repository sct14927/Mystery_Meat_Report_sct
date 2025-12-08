# Mystery_Meat_Report_sct

README 

This repository contains the following folders and files:

  * Code and Raw Sequences (folder) = contains BASH and Python scripts, and a folder containing the 12 .FASTQ files representing the four samples.
  * Code and Raw Sequences (zipped folder) = same contents as above.
  * Processed Sequences, Alingment and Tree (folder) = contains two FASTA files (all sequences used in the analysis, and their translation), along with the alignment and phylotree files.
  * Supplementary Tables 1 and 2 (.xlsx file)

IMPORTANT NOTE: To conduct this analysis you are required to have Visual Studio Code installed on your computer, with both Python and BioPython modules installed.

RUNNING THE ANALYSIS:

1) In order to run this analysis for yourself, first download the zipped "Code and Raw Sequences" folder from this repository, and unzip. The contents should include:
  * a folder called 'raw_sequences' containing 12 .FASTQ files
  * a .FASTA file containing reference sequences
  * a .sh BASH script
  * and a .py Python script
3) Open Visual Studio Code and open the folder ("Code and Raw Sequences"). Ensure you are in the correct directory, you should be able to see the contents listed above.
4) Run the BASH script using './BASH_concatenator_script.sh', this combine the sample .FASTQ files into single sequences for each of the samples, and output them together as a new file called 'all_sample_sequences'.
5) Next run the Python script using './Python_Translation_Script.py', this will combine the sample sequences with the reference sequence in a new file ('allseq.FASTA'), translate the longest coding sequences and output them as a new file called 'translated_sequences.FASTA'.
6) Open your browser and go to the following link https://www.ebi.ac.uk/jdispatcher/msa/muscle5. This is MUSCLE 5, a multiple sequence alignner. Upload 'translated_sequences.FASTA' and submit.
7) Download the alignment and .tree file.
8) Upload the .tree file to the Interactive Tree of Life at https://itol.embl.de/ to visualise your tree. Right click on Mitsukurina owstoni and select it as the outgroup.
