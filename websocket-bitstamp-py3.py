
from websocket import WebSocketApp
from json import dumps, loads
import io




URL = "wss://ws.bitstamp.net"


def on_message(_, message):
    """Callback executed when a message comes.

    Positional argument:
    message -- The message itself (string)
    """
    get_data = loads(message)
    if get_data["data"] != {}:
        json1 = dumps(get_data, indent=4, sort_keys=True, default=str)
        with io.open('order_book.json', 'a', encoding='utf-8') as f:
            f.write(json1)

        string = '(' + str(get_data["data"]["timestamp"]) + ') ' + str(get_data["data"]["id"]) + ': ' + str(get_data["data"]["amount"]) + ' BTC @ ' + str(get_data["data"]["price"]) + ' USD ' + str(get_data["data"]["type"])
        print (string)



def on_open(socket):
    """Callback executed at socket opening.

    Keyword argument:
    socket -- The websocket itself
    """

    params = {
                "event": "bts:subscribe",
                "data": {
                    "channel": "live_trades_btcusd"
                }
            }
    send_param = dumps(params)
    socket.send(send_param)


def main():
    """Main function."""
    ws = WebSocketApp(URL, on_open=on_open, on_message=on_message)
    ws.run_forever()


if __name__ == '__main__':
    main()