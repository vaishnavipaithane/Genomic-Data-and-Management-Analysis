##Data Sorting and Extraction

import os

folder_path = 'C:/Users/vaish/Desktop/Miniprojects/G1/File Search & Extract'

#list directories in the folder path

os.listdir(folder_path)

#for loop to get directories within each folder

for folder in os.listdir(folder_path):
    file_path = os.path.join(folder_path, folder)
    print(f"Contents of {file_path}:")
    for item in os.listdir(file_path):
        print(item)
    print()
    
#use glob to search for fasta (.fa) files

import glob

fa_files = glob.glob(str(folder_path) + "/**/*.fa", recursive= True)
print(fa_files)

#copy fasta (.fa) files to a new location

import shutil
    
destination= r'C:/Users/vaish/Desktop/Miniprojects/G1/Fasta'
for item in fa_files:
    shutil.copy(item, destination)
    
#Extract the first line from each fasta file and record it in a text file

Path = 'C:/Users/vaish/Desktop/Miniprojects/G1/Fasta/'
file_list = os.listdir(Path)
for item in file_list:
    #if item.endswith(".fa"):
    with open(Path + item, 'r') as f:
        first_line = f.readline()
        print(first_line)
        new_file= open('C:/Users/vaish/Desktop/Miniprojects/G1/Fasta/new.txt', 'a')
        new_file.write(first_line)
        new_file.close()

## Data Analysis

#Generate details of each folder in a summary CSV file, including the number of files and the list of files present in each folder
#This involves traversing through directories, counting files, and compiling a summary report.    
    
folder_path = 'C:/Users/vaish/Desktop/Miniprojects/G1/File Search & Extract'
dic = {}

for dirpath, dirnames, filenames in os.walk(folder_path):
    # Use os.path.relpath to get the relative path from folder_path
    relative_dir = os.path.relpath(dirpath, folder_path)
    dic[relative_dir] = filenames

f = open('C:/Users/vaish/Desktop/Miniprojects/G1/File Search & Extract/dic.csv', 'w')
f.write('File Name: Documents\n')
for p in dic:
    f.write(p + ': ' + ', '.join(dic[p]) + '\n')
f.close()

#Identify the vcf file that is smallest in size, read it into a tabular format.

import pandas as pd

folder_path = 'C:/Users/vaish/Desktop/Miniprojects/G1/File Search & Extract'
os.listdir(folder_path)

vcf_files = glob.glob(str(folder_path) + "/**/*.vcf", recursive= True)
print(vcf_files)

size_of_files = [
    (vcf_file, os.stat(vcf_file).st_size)
    for vcf_file in vcf_files
]

print(size_of_files)
vcf_df = pd.DataFrame(size_of_files)

#Filter for variants in chromosome 21.

def read_vcf(file: str) -> pd.DataFrame:
    num_header = 0
    with open(file) as f:
        for line in f.readlines():
            if line.startswith("##"):
                num_header += 1
            else:
                break
    
    vcf = pd.read_csv(file, sep="\t", skiprows=num_header)
    vcf = vcf.rename({"#CHROM": "CHROM"}, axis=1)
    return vcf

vcf = read_vcf('C:/Users/vaish/Desktop/Miniprojects/G1/File Search & Extract/FTGD/data.vcf')
vcf2= vcf[vcf["FILTER"] == "multiallelic"]
vcf3= vcf2[vcf2["CHROM"] == "chr21"]
vcf3


###Data Visulization

#Bar plot

import matplotlib.pyplot as plt

counts = vcf2['CHROM'].value_counts()
print(counts)
    
plt.figure(figsize=(10, 6))
counts.plot.bar(x='CHROM', y='count',
                xlabel= 'CHROMOSOME', ylabel='COUNT', 
                title='Count of variants on each chromosome', rot=0)
plt.xticks(rotation=45, ha='right')




    
    
    
    
    
    




