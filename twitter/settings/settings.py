# coding: utf-8

import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join("/Users/hhio6/Desktop/line-semi-auto/semiauto", ".env")
load_dotenv(dotenv_path)

TPS = os.environ.get("TWITTER_PASS")
TID = os.environ.get("TWITTER_ID")