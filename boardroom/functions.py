# -*- coding: utf-8 -*-
"""Boardroom functions."""
from .params import *
import requests

def get_protocol(cname="all"):
    """
    Get protocols details.

    :param cname: protocol cname
    :type cname: str
    :return: data as dict
    """
    try:
        api = API_BASE + "/protocols/{0}".format(cname)
        if cname.lower() == "all":
            api = API_BASE + "/protocols"
        response = requests.get(api)
        if response.status_code == 200:
            data_json = response.json()
            return data_json["data"]
        return None
    except Exception:
        return None


def get_proposal(cname,ref_id):
    pass

def get_vote(address,ref_id):
    pass

def get_voter(cname,address):
    pass

def get_stat():
    """
    Get global platform stats.

    :return: data as dict
    """
    try:
        response = requests.get(API_BASE + "/stats")
        if response.status_code == 200:
            data_json = response.json()
            return data_json["data"]
        return None
    except Exception:
        return None



