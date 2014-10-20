from xbmcswift2 import Plugin


plugin = Plugin()


@plugin.route('/')
def index():
    items = [
        {'label': 'Elgen Nutag 96.9', 'path': 'rtmp://67.138.108.218/live/Elgennutag live=true', 'is_playable': True,},
        {'label': 'Mongoliin Undesnii Radio', 'path': 'rtmp://202.21.117.233/fm106/livestream live=true', 'is_playable': True,},
        {'label': 'Mgl Radio 102.1', 'path': 'http://209.105.250.73:8080;', 'is_playable': True,},
    ]
    return items


if __name__ == '__main__':
    plugin.run()
