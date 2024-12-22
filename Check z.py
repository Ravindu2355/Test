import requests

def is_file_within_size_limit_from_url(url, size_limit=2 * 1024 * 1024 * 1024):  # 2GB in bytes
    """
    Checks if a file from a URL is smaller than or equal to the specified size limit.

    :param url: The URL of the file.
    :param size_limit: Maximum allowed file size in bytes (default is 2GB).
    :return: True if the file is within the size limit, False otherwise.
    """
    try:
        # Send a HEAD request to fetch headers only
        response = requests.head(url, allow_redirects=True)

        if response.status_code != 200:
            print(f"Error: Unable to access the URL. Status code: {response.status_code}")
            return False

        # Get the 'Content-Length' header, which gives the file size in bytes
        content_length = response.headers.get('Content-Length')
        if content_length is None:
            print("Error: 'Content-Length' header is missing. Cannot determine file size.")
            return False

        file_size = int(content_length)
        if file_size <= size_limit:
            print(f"The file at '{url}' is within the size limit ({file_size} bytes).")
            return True
        else:
            print(f"The file at '{url}' exceeds the size limit ({file_size} bytes).")
            return False

    except requests.RequestException as e:
        print(f"Error: Failed to check file size from URL. Exception: {e}")
        return False


# Example usage
url = input("Enter the file URL: ")
if is_file_within_size_limit_from_url(url):
    print("File size check passed.")
else:
    print("File size check failed.")
