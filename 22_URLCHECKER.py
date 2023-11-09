import urllib.request
try:
    page_url = "https://www.gettyimages.in/photos/india-empty-roads"
    response = urllib.request.urlopen(page_url)
    # process the response
except urllib.error.HTTPError as e:
    print(f"The server returned an HTTP error {e.code} - {e.reason}")
    # handle the error
