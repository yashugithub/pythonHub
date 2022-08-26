import unittest
import time
import logging
import requests

class Test_Session(unittest.TestCase):
    def test_sess(self):

        logging.basicConfig(format="%(asctime)s %(levelname)-8s %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S",
                            level=logging.DEBUG)
        logger = logging.getLogger()

        url = "http://njrusmc.net"

        # Issue two HTTP GET requests without using session
        logger.info("Individual, stateless request")
        requests.get(url)
        requests.get(url)

        # Now use a session; setup occurs only once
        logger.info("Long-lived, stateful TCP session")
        sess = requests.session()
        sess.get(url)
        sess.get(url)

if __name__ == '__main__':
    unittest.main()
