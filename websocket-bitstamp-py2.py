
from websocket import WebSocketApp
from json import dumps, loads
import io

# -*- coding: utf-8 -*-
URL = u"wss://ws.bitstamp.net"


def on_message(_, message):
    """Callback executed when a message comes.

    Positional argument:
    message -- The message itself (string)
    """
    get_data = loads(message)
    if get_data[u"data"] != {}:
        json1 = unicode(dumps(get_data, indent=4, sort_keys=True, default=str))
        with io.open(u'order_book.json', u'a', encoding=u'utf-8') as f:
            f.write(json1)


        string = u'(' + str(get_data[u"data"][u"timestamp"]) + u') ' + str(get_data[u"data"][u"id"]) + u': ' + str(get_data[u"data"][u"amount"]) + u' BTC @ ' + str(get_data[u"data"][u"price"]) + u' USD ' + str(get_data[u"data"][u"type"])
        print string
    print


def on_open(socket):
    """Callback executed at socket opening.

    Keyword argument:
    socket -- The websocket itself
    """

    params = {
                u"event": u"bts:subscribe",
                u"data": {
                    u"channel": u"live_trades_btcusd"
                }
            }
    send_param = dumps(params)
    socket.send(send_param)


def main():
    """Main function."""
    ws = WebSocketApp(URL, on_open=on_open, on_message=on_message)
    ws.run_forever()
    print

if __name__ == u'__main__':
    main()