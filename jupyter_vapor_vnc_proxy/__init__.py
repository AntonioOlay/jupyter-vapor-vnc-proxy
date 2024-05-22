import os
import os.path

def setup_vapor_desktop():

    uid=os.getuid()

    WEBSOCKET=8900+1000+uid
    print(WEBSOCKET)

    home = os.getenv("HOME")
    config_path = '.jupyter/config_novnc.sh'
    full_path = os.path.join(home, config_path)
    logopath = '.jupyter/VAPOR_LOGO.png'
    if os.path.exists(full_path) == False:
    	print("El archivo config_novnc.sh no se encuentra en la ruta:", home + "/.jupyter")


    path = 'novnc/?resize=remote&reconnect=1&autoconnect=1&port=' + str(WEBSOCKET)
    
    return {
        'command': [full_path],
        'port': WEBSOCKET,
        'timeout': 30,
	'absolute_url': False,
        #'mappath': {'/': '/mw_lite.html'},
        'new_browser_window': True,
        'launcher_entry': {
            'title': 'VAPOR VNC DESKTOP',
	    'path_info': path,
            'icon_path': os.path.join(home, logopath)
        }
    }