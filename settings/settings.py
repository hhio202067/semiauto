# coding: utf-8

import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(os.environ.get("PYPATH"), ".env")
load_dotenv(dotenv_path)

TPS = os.environ.get("TWITTER_PASS")
TID = os.environ.get("TWITTER_ID")