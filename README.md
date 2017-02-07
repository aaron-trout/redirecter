# redirecter
`redirecter` is a very small and simple Python application written in
[aiohttp](https://aiohttp.readthedocs.io/) which redirects HTTP requests to
another server of your choice, maintaining the path part of the request.

For example, if you configured the remote server to `http://example.com`, then
a request to `redirecter` at `http://localhost:8000/foo/bar?stuff=things` would
redirect to `http://example.com/foo/bar?stuff=things`.

## Running with Docker
The easiest way to run is with the pre-built Docker image. The configuration is
done via environment variables and should be self explanatory:

```bash
$ docker run --detach --publish 80:8000 --restart always --name redirecter \
    --env "REDIRECTER_TARGET=http://example.com" \
    --env "REDIRECTER_HOST=0.0.0.0" \
    --env "REDIRECTER_PORT=8000" \
    redirecter:latest
```

Note: Do *NOT* include a trailing slash ('/') on the `REDIRECTER_TARGET`
variable; this is not currently handled and will result in a double slash in
the redirected URL.

## Running with Python
If you'd prefer to run with Python directly, rather than inside Docker, then
this is for you:

Prerequisites:
  - Python 3.5+

```bash
$ pip install -r requirements.txt
$ REDIRECTER_TARGET="http://example.com" REDIRECTER_HOST="0.0.0.0" \
    REDIRECTER_PORT="8000" python redirecter.py
```
