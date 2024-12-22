# My Domain Search Tool

This tool checks the availability of domain names using the GoDaddy API. It processes a list of domain names from a file (`domains.txt`), verifies their availability, and writes the available domains to another file (`available_domains.txt`).

## Prerequisites

1. **Python**: Ensure you have Python 3.6 or above installed.
2. **Requests Library**: Install the `requests` library if you don’t already have it:
   ```bash
   pip install requests
   ```
3. **GoDaddy API Key and Secret**:
   - Create an account on [GoDaddy Developer](https://developer.godaddy.com/).
   - Obtain an API key and secret for both production and development environments.

## Setup

1. **Clone or Download the Repository**
   - Clone this repository or download the `domain_search.py`, `domains.txt`, and `available_domains.txt` files.

2. **Configure API Keys**
   - Open the `domain_search.py` file.
   - Replace the placeholders `<Go Daddy API-Key>` and `<Go Daddy API-Secret>` with your GoDaddy API credentials.

   ```python
   API_KEY = '<Go Daddy API-Key>'
   API_SECRET = '<Go Daddy API-Secret>'
   ```

3. **Set Environment**
   - Toggle the `USE_PRODUCTION` variable to switch between the production and development environments:
     ```python
     USE_PRODUCTION = False  # Use True for production, False for development
     ```

4. **Prepare Input File**
   - Add the list of domain names (one per line) to `domains.txt`. For example:
     ```
     example1
     example2
     example3
     ```

## Usage

1. **Run the Script**
   Execute the script using the command line:
   ```bash
   python domain_search.py
   ```

2. **Output**
   - The script will check the availability of the domains listed in `domains.txt`.
   - It will print the availability status of each domain to the console.
   - Available domains will be saved to `available_domains.txt` in the format:
     ```
     example1.com is available
     example3.com is available
     ```

## Error Handling

- **403 Error: Access Denied**:
  - Ensure your API key and secret are correct.
  - Verify that your API key has the necessary permissions.

- **Other Errors**:
  - The script will print the error code and message to help you debug the issue.

## Notes

- The tool is configured to check `.com` domains by default. You can modify the domain extension in the script if needed.
- Ensure your API key limits and permissions align with the number of domains you are checking.

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

Enjoy checking domain availability with ease!

