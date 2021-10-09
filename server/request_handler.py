"""
MAIN THREAD
Handles all the connections, creating new games and requests from clients(s)
"""

import socket
from _thread import *
import pickle