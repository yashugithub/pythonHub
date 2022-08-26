import time
import unittest
import logging
import requests
from cachecontrol import CacheControl
from ResponseFormatter import responseFormatter

class Test_CacheControl(unittest.TestCase):
    def test_cahceControl(self):

        logging.basicConfig(format="%(asctime)s %(levelname)-8s %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S",
                            level=logging.DEBUG)
        logger = logging.getLogger()

        base_url = "http://njrusmc.net/cache"
        test_list = [
            "zero128k_public60.test",  # Cache-Control: public, max-age=60
            "zero128k_nostore.test"    # Cache-Control: nostore
        ]

        # For each file, run two GET requests, and use the logger to print the out
        # the relevant information as requests are processed
        for test_file in test_list:
            # Assemble the complete URL to feed into the HTTP GET request
            url = f"{base_url}/{test_file}"

            # Create the cached session object, which automatically interprets
            # caching-related headers (requests doesn't do it natively)
            cached_sess = CacheControl(requests.session())

            # Print information from first run, include key headers
            logger.info("First GET to %s", url)
            resp = cached_sess.get(url)
            resp.raise_for_status()
            responseFormatter(resp, dump_body=False)
            print(f"\n\n{'*' * 80}\n\n")

            # Slight delay just to show the cache time countdown
            # print information from second run, but focus is on background debugs
            time.sleep(2)
            logger.info("Second GET to %s", url)
            resp = cached_sess.get(url)
            resp.raise_for_status()
            responseFormatter(resp, dump_body=False)
            print(f"\n\n{'*' * 80}\n\n")






if __name__ == '__main__':
    unittest.main()
