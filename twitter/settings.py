# coding: utf-8

import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenvPath = join(os.("../"), ".env")
load_dotenv(dotenvPath)

TPS = os.environ.get("TWITTER_PASS")
TID = os.environ.get("TWITTER_ID")