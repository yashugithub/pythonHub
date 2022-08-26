
import json
import requests

def responseFormatter(resp, filedir="resp", filename=None, dump_body=True):
    """
    print the key details from a given response. Set dump_body to True to reveal the body content
    in the most appropriate fromat based on the response's Content-Type header.

    :param resp:
    :param fileddir:
    :param filename:
    :param dump_body:
    :return:
    """

    # For context, print the original request
    # ... add a line of dashes of equal length
    header = f"\\{resp.request.method} {resp.request.url}"
    print(header)
    print(len(header) * "-")

    # print the status code and reason, along with the elapsed time
    print(f"Result: {resp.status_code}/{resp.reason}")
    print(f"Elapsed time: {resp.elapsed.microseconds} us")

    # Iterate over all key-value pairs in the headers directory and prints them
    print("HTTP headers:")
    for header_name, header_value in resp.headers.items():
        print(f" -{header_name}: {header_value}")

    # Print the numbers of redirects.If any exists, print out the URL/status
    print(f"HTTP redirect count: {len(resp.history)}")
    for hist in resp.history:
        print(f" - {hist.url} -> {hist.status_code}/{hist.reason}")

    # Optionally dump the body; useful for plain text responses (not files)
    if dump_body:
        # First, determine the content type, defaulting to "html"
        content_type = resp.headers.get("Content-Type", "html")

        # If a file name is not supplied, create a dynamic one using the method name
        # and the in-memory ID of the response object
        if not filename:
            filename = f"{resp.request.method}_{id(resp)}".lower()

        # Define the entire filepath using the directory and name
        filepath = f"{filedir}/{filename}"

        # Based on the content type, create different files
        # Add more options if you want .....
        if "html" in content_type:
            filepath += ".html"
            with open(filepath, "w") as handle:
                handle.write(resp.text)
        elif "json" in content_type:
            filepath += ".json"
            with open(filepath, "w") as handle:
                json.dump(resp.json(), handle, indent=2)

        print(f"HTTP body written to {filepath}")

def main():
    """
    Perform a quick test on the responseFormatter() function
    :return:
    """

    resp = requests.get("http://njrusmc.net")
    resp.raise_for_status()
    responseFormatter(resp, filename="get_nick_website")


if __name__ == '__main__':
    main()

