import pyshark
<<<<<<< HEAD
import urllib.request
import requests 
import shutil 

capture = pyshark.LiveCapture(interface='any', display_filter='http')

while(True):
    capture.sniff(timeout=1)

    for i in range(len(capture)):
        if (hasattr(capture[i].http, "request_full_uri") and 
        ('.png' in capture[i].http.request_full_uri or
        '.jpg' in capture[i].http.request_full_uri or
        '.jpeg' in capture[i].http.request_full_uri or
        '.gif' in capture[i].http.request_full_uri or
        '.bmp' in capture[i].http.request_full_uri or
        '.svg' in capture[i].http.request_full_uri or
        '.webp' in capture[i].http.request_full_uri)):
            link = capture[i].http.request_full_uri
            image_url = link
            fotos = image_url.split("/")[-1]

            r = requests.get(image_url, stream = True)

            if r.status_code == 200:
                r.raw.decode_content = True
                with open("Fotos/" + fotos,'wb') as f:
                    shutil.copyfileobj(r.raw, f)
=======

capture = pyshark.LiveCapture(interface='eth0')
capture.sniff(timeout=50)
capture

capture[3]

for packet in capture.sniff_continuously(packet_count=5):
    print("Just arrived:", packet)
>>>>>>> 126e2b45070d96aa3bded2a430eaead0693f731a
