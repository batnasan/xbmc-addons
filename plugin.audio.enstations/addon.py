from xbmcswift2 import Plugin


plugin = Plugin()


@plugin.route('/')
def index():
    item = [
            {'label': 'Voice of America', 'path': 'http://voa-28.akacast.akamaistream.net/7/54/322040/v1/ibb.akacast.akamaistream.net/voa-28', 'is_playable': True,},
    ]
    return item


if __name__ == '__main__':
    plugin.run()
