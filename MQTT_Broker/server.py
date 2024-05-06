from hbmqtt.broker import Broker
import asyncio
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

broker_config = {
    'listeners': {
        'default': {
            'type': 'tcp',
            'bind': '0.0.0.0:1883'  # Bind to all interfaces on port 1883
        }
    },
    'sys_interval': 10,
    'topic-check': {
        'enabled': False
    }
}

# Start the broker
async def start_broker():
    broker = Broker(broker_config)
    await broker.start()

if __name__ == '__main__':
    # Set up event loop to run the broker
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_broker())
    loop.run_forever()
