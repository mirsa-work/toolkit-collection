
# Find Broken URLs

## Overview

The `url_find_broken.py` script is designed to check the status of URLs listed in a CSV file and categorize them based on their HTTP response codes. This tool is useful for identifying broken or problematic URLs, which can be particularly helpful in website maintenance, content auditing, or SEO tasks.

## Features

- **Checks URL Status**: Sends a HEAD request to each URL in the provided CSV file to check its status.
- **Categorizes URLs**: 
  - URLs are grouped based on their HTTP response codes.
  - Separate CSV files are generated for each group of URLs by response code.
- **Progress Tracking**: Displays a progress bar while processing URLs.
- **Error Handling**: Logs any URLs that cause errors during processing.

## Setup

### Prerequisites

Make sure you have Python installed. The following Python packages are required:

- `pandas`
- `requests`
- `tqdm`

You can install the required packages using pip:

```bash
pip install pandas requests tqdm
```

### Directory Structure

Ensure your CSV file with URLs is placed in the same directory as the script:

```
toolkit-collection/
└── python-scripts/
    └── url-find-brokan/
        ├── url_find_broken.py
        └── urls.csv
```

## Usage

1. Prepare a CSV file named `urls.csv` containing a column named `url` with the URLs you want to check.
2. Run the script:

   ```bash
   python url_find_broken.py
   ```

3. After execution, the script will generate separate CSV files for each HTTP response code (e.g., `response_404.csv` for 404 errors).

### Customization

You can modify the script to check for specific response codes or to use a different method of checking URLs (e.g., GET requests instead of HEAD requests) by editing the `requests.head(url, allow_redirects=True)` line.

## Output

The script generates CSV files based on the HTTP response codes of the URLs:

- **`response_404.csv`**: Contains URLs that returned a 404 Not Found error.
- **`response_500.csv`**: Contains URLs that returned a 500 Internal Server Error.
- **`response_<status_code>.csv`**: Contains URLs that returned other HTTP status codes.

## Troubleshooting

- If a URL causes an error during processing, the script will print the error message.
- Ensure that the `urls.csv` file is correctly formatted with a column named `url`.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributions

Contributions are welcome! Please open an issue or submit a pull request with any improvements or bug fixes.
