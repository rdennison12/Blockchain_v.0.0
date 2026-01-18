import time

from pubnub.callbacks import SubscribeCallback
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from backend.app import pubsub_config

pnconfig = PNConfiguration()

pnconfig.subscribe_key = pubsub_config.SUBSCRIBE_KEY
pnconfig.publish_key = pubsub_config.PUBLISH_KEY
pnconfig.user_id = "blockchain-backend-shell"

TEST_CHANNEL = 'TEST_CHANNEL'


class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')


class PubSub():
    """
    Handles the publish/subscribe layer on the application.
    Provides communication between the nodes of the blockchain network.
    """

    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels([TEST_CHANNEL]).execute()
        self.pubnub.add_listener(Listener())

    def publish(self, channel, message):
        """
        Publishes a message to a channel.
        :param channel:
        :param message:
        :return:
        """
        self.pubnub.publish().channel(channel).message(message).sync()


def main():
    pubsub = PubSub()
    time.sleep(1)
    pubsub.publish(TEST_CHANNEL, {'foo': 'bar'})


if __name__ == '__main__':
    main()
