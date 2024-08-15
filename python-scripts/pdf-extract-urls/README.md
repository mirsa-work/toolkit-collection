
# PDF Extract URLs

## Overview

The `pdf_extract_urls.py` script is designed to extract all URLs from PDF files located in a specified directory. It filters out specific URLs based on predefined patterns and categorizes them into different CSV files. This tool is useful for anyone needing to analyze or review URLs embedded in multiple PDF files, with the ability to exclude certain types of URLs.

## Features

- **Extracts URLs**: Retrieves all referenced URLs from PDF files in a specified directory.
- **Excludes Specific URLs**: Filters out URLs based on exact matches or regular expressions.
- **Categorizes URLs**: 
  - `unique_urls.csv`: Contains all unique URLs that are not excluded.
  - `file_url_map.csv`: Maps each PDF file to its extracted URLs.
  - `excluded_urls.csv`: Lists URLs that match the exclusion patterns.
  - `unique_excluded_urls.csv`: Contains unique URLs that were excluded.
- **Progress Tracking**: Displays the progress of PDF processing using a progress bar.
- **Error Handling**: Logs any files that fail during processing and prints error details.

## Setup

### Prerequisites

Make sure you have Python installed. The following Python packages are required:

- `pdfx`
- `tqdm`

You can install the required packages using pip:

```bash
pip install pdfx tqdm
```

### Directory Structure

Ensure your PDFs are stored in a directory named `input` within the same directory as the script:

```
toolkit-collection/
└── python-scripts/
    └── pdf-extract-urls/
        ├── pdf_extract_urls.py
        └── input/
            ├── your-pdf-file-1.pdf
            ├── your-pdf-file-2.pdf
            └── ...
```

## Usage

1. Place your PDF files in the `input` directory.
2. Run the script:

   ```bash
   python pdf_extract_urls.py
   ```

3. After execution, the script will generate the following CSV files:
   - `unique_urls.csv`
   - `file_url_map.csv`
   - `excluded_urls.csv`
   - `unique_excluded_urls.csv`

### Customization

You can modify the exclusion patterns within the script by editing the `exclude_patterns` list. These patterns are defined using regular expressions.

```python
exclude_patterns = [
    re.compile(r"^(https?://)?(www\.)?example\.[a-z]{2,3}/?$"),
    re.compile(r"^https?://video\.example\.[a-z]{2,3}.*"),
    re.compile(r"^mailto:.*"),
    re.compile(r"^file://.*"),
    re.compile(r"^(?!https?://(www\.)?example\.)")
]
```

## Output

The script generates the following CSV files:

- **`unique_urls.csv`**: Contains all unique URLs that do not match any exclusion patterns.
- **`file_url_map.csv`**: Maps each PDF file to the URLs extracted from it.
- **`excluded_urls.csv`**: Contains URLs that match the exclusion patterns.
- **`unique_excluded_urls.csv`**: Contains all unique URLs that were excluded.

## Troubleshooting

- If a PDF file fails to process, the script will log the file name and print the error details.
- Ensure that the `input` directory contains only PDF files.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributions

Contributions are welcome! Please open an issue or submit a pull request with any improvements or bug fixes.
