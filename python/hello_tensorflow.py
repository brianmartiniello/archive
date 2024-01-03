#!/usr/bin/python3

"""Test TensorFlow Module"""

import sys
import tensorflow as tf


#
# main
#
def main(argv):
    """ Function main """
    hello = tf.constant("Hello, TensorFlow! - Args (" + str(argv) + ")")
    session = tf.Session()
    print(session.run(hello))


if __name__ == '__main__':
    main(sys.argv[1:])
