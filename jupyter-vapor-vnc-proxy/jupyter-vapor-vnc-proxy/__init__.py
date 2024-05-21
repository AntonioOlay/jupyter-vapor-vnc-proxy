import os
import os.path

def setup_vapor_desktop():

    uid=os.getuid()

    WEBSOCKET=8900+1000+uid
    print(WEBSOCKET)

    #xfec_path = os.path.abspath("xfec_desk3.sh")
    home = os.getenv("HOME")
    xfec_path = home + '.jupyter/xfec_desk3.sh'
    path = 'novnc/?resize=remote&reconnect=1&autoconnect=1&port=' + str(WEBSOCKET)
    
    return {
        'command': [xfec_path],
        'port': WEBSOCKET,
        'timeout': 30,
	'absolute_url': False,
        #'mappath': {'/': '/mw_lite.html'},
        'new_browser_window': True,
        'launcher_entry': {
            'title': 'VAPOR VNC DESKTOP',
	    'path_info': path,
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'VAPOR_LOGO.png')
        }
    }
