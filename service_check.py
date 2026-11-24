import argparse
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


def report_status(status):
    if status == 200:
        print("Service responded successfully")
    elif status == 503:
        print("Service is unavailable")
    elif status == 404:
        print("Requested page or resource was not found")
    elif status == 500:
        print("Service encountered an internal server error")
    else:
        print(f"Service returned status {status}")


parser = argparse.ArgumentParser(description="Check an HTTP endpoint.")
parser.add_argument("url", help="HTTP or HTTPS URL to check")
url = parser.parse_args().url

try:
    with urlopen(url, timeout=5) as response:
        report_status(response.status)
        raise SystemExit(0 if 200 <= response.status < 300 else 1)
except HTTPError as error:
    report_status(error.code)
    raise SystemExit(1)
except URLError:
    print("Could not connect to the service")
    raise SystemExit(1)