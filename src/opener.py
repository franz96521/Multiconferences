from src.telmex import Telmex
from src.zoom import Zoom
from src.goto import GoTo
import threading

class Opener:
    def __init__(self):
        self.types = {
            "telmex": Telmex(),
            "zoom": Zoom(),
            "goto": GoTo()          
        }        

    def get_class(self, url):
        for key in self.types.keys():
            if key in url:
                return self.types[key]           
        return None
    
    def open_conference(self, url, id):
        conference = self.get_class(url)
        if conference:
            thread = threading.Thread(target=conference.open_conference, args=(url, id))
            thread.start()
        else:
            raise ValueError(f"Conference not found for {url}")
        