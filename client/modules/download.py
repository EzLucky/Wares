import requests
import os
import utils


def run(url):
    try:
        filename = url.split('/')[-1]
        filepath = os.path.join(os.environ['temp'], filename)
        r = requests.get(url, stream=True)
        with open(filepath, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8000):
                if chunk:
                    f.write(chunk)
        utils.send_output("Downloaded: %s -> %s" % (url, filepath))
    except Exception, exc:
        utils.send_output(exc)


def help():
    help_text = """
Usage: download http://example.com/filename
Downloads a file through HTTP.

"""
    return help_text
