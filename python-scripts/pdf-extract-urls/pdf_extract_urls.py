import pdfx
import os
import csv
import re
from tqdm import tqdm
import traceback

# Define the directory containing the PDF files
pdf_directory = "./input"

# Define the output directory for the CSV files
output_directory = "./output"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Define the URLs to exclude (both exact matches and regex patterns)
exclude_patterns = [
    re.compile(r"^(https?://)?(www\.)?example\.[a-z]{2,3}/?$"),  # Exclude www.example.<tld> and www.example.<tld>/ with or without http/https
    re.compile(r"^https?://video\.example\.[a-z]{2,3}.*"),  # Exclude URLs with domain video.example.<tld>
    re.compile(r"^mailto:.*"),  # Exclude mailto: links
    re.compile(r"^file://.*"),  # Exclude file paths
    re.compile(r"^(?!https?://(www\.)?sampledomain\.)")  # Exclude all URLs where the second-level domain is not "example"
]

# Get all PDF files in the directory
file_names = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]

# Sets and lists to store the results
unique_urls = set()
file_url_map = []
excluded_urls_map = []
unique_excluded_urls = set()
failed_files = set()

# Iterate over each file name with progress information
for index, file_name in enumerate(tqdm(file_names, desc="Processing PDFs", unit="file"), start=1):
    file_path = os.path.join(pdf_directory, file_name)
    
    try:
        # Create a PDFx object using the absolute file path
        pdf = pdfx.PDFx(os.path.abspath(file_path))
        
        # Get all referenced URLs in the PDF
        references_list = pdf.get_references()
        
        # Separate included and excluded URLs
        for ref in references_list:
            url = ref.ref
            if any(pattern.match(url) for pattern in exclude_patterns):
                excluded_urls_map.append([file_name, url])
                unique_excluded_urls.add(url)
            else:
                file_url_map.append([file_name, url])
                unique_urls.add(url)

    except Exception as e:
        print(f"Error processing {file_name}: {e}")
        failed_files.add(file_name)
        traceback.print_exc()  # Print the full traceback to understand the root cause

# Write unique URLs to a CSV file
with open(os.path.join(output_directory, 'unique_urls.csv'), 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Unique URLs"])
    for url in sorted(unique_urls):
        writer.writerow([url])

# Write file-to-URL mapping to another CSV file
with open(os.path.join(output_directory, 'file_url_map.csv'), 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["File Name", "URL"])
    for record in file_url_map:
        writer.writerow(record)

# Write excluded URLs to a separate CSV file
with open(os.path.join(output_directory, 'excluded_urls.csv'), 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["File Name", "Excluded URL"])
    for record in excluded_urls_map:
        writer.writerow(record)

# Write unique excluded URLs to a separate CSV file
with open(os.path.join(output_directory, 'unique_excluded_urls.csv'), 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Unique Excluded URLs"])
    for url in sorted(unique_excluded_urls):
        writer.writerow([url])

print("CSV files have been generated in the 'output' directory.")
if failed_files:
    print(f"Failed files: {', '.join(failed_files)}")
