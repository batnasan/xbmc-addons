from xbmcswift2 import Plugin


plugin = Plugin()


@plugin.route('/')
def index():
    item = [
            {'label': 'Voice of America', 'path': 'http://voa-28.akacast.akamaistream.net/7/54/322040/v1/ibb.akacast.akamaistream.net/voa-28', 'is_playable': True,},
            {'label': 'BBC World Service', 'path': 'http://bbcwssc.ic.llnwd.net/stream/bbcwssc_mp1_ws-eieuk', 'is_playable': True,},
            {'label': 'BBC 1', 'path': 'http://www.bbc.co.uk/radio/listen/live/r1.asx', 'is_playable': True,},
            {'label': 'BBC 2', 'path': 'http://www.bbc.co.uk/radio/listen/live/r2.asx', 'is_playable': True,},
            {'label': 'BBC 4', 'path': 'http://www.bbc.co.uk/radio/listen/live/r4lw.asx', 'is_playable': True,},
            {'label': 'BBC 5', 'path': 'http://www.bbc.co.uk/radio/listen/live/r5l.asx', 'is_playable': True,},
            {'label': 'BBC 6 Music', 'path': 'mms://wmlive-nonacl.bbc.net.uk/wms/bbc_ami/6music/6music_bb_live_int_eq1_sw1', 'is_playable': True,},
    ]
    return item


if __name__ == '__main__':
    plugin.run()
