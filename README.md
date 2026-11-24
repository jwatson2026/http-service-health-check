# HTTP Service Health Check

A Python command-line tool that checks an HTTP or HTTPS endpoint. Use it after a deployment or service restart to confirm that the endpoint responds successfully.

## Usage

Requires Python 3. No third-party packages are needed.

```powershell
python service_check.py --help
python service_check.py http://127.0.0.1:8080/
```

Use the address of the service you want to check. The example assumes a local server is listening on port 8080.

## Exit codes

| Code | Meaning |
| --- | --- |
| `0` | The endpoint returned a successful HTTP response (2xx). |
| `1` | The check received an unsuccessful HTTP response or could not connect. |

## Local verification

| Scenario | Observed result |
| --- | --- |
| Server running, root URL requested | Success message and exit code `0` |
| Server running, `/missing-page` requested | Missing-resource message and exit code `1` |
| Server stopped | Connection failure message |
| Server restarted, root URL checked again | Success message confirmed recovery |
