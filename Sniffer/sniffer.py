import pyshark
import urllib.request
import requests 

capture = pyshark.LiveCapture(interface='any', display_filter='http')

while(True):
    capture.sniff(timeout=1)

    for pacote in capture:
        if (hasattr(pacote.http, "request_full_uri")): 
            link = pacote.http.request_full_uri

            if('.png' in pacote.http.request_full_uri or
            '.jpg' in pacote.http.request_full_uri or
            '.jpeg' in pacote.http.request_full_uri or
            '.gif' in pacote.http.request_full_uri or
            '.bmp' in pacote.http.request_full_uri or
            '.svg' in pacote.http.request_full_uri or
            '.webp' in pacote.http.request_full_uri):
                image_url = link
                fotos = image_url.split("/")[-1]
                r = requests.get(image_url, stream = True)

                if r.status_code == 200:
                    r.raw.decode_content = True
                    with open(str(fotos), 'wb') as f:
                        for imgs in r:
                            f.write(imgs)
