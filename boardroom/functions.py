# -*- coding: utf-8 -*-
"""Boardroom functions."""
from .params import *
import requests

def get_protocol(cname="all", limit = None):
    """
    Get protocols details.
    :param cname: protocol cname
    :type cname: str
    :param limit: pagination limit
    :type limit: int
    :return: data as dict
    """
    try:
        api = API_BASE + "/protocols/{0}".format(cname)
        if cname.lower() == "all":
            api = API_BASE + "/protocols"
        if limit is not None:
            api += "?limit={0}".format(limit)
        response = requests.get(api)
        if response.status_code == 200:
            data_json = response.json()
            return data_json["data"]
        return None
    except Exception:
        return None


def get_proposal(cname = None, ref_id = None, limit = None):
    """
    Get proposal details.
    :param cname: protocol cname
    :type cname: str
    :param ref_id: protocol ref_id
    :type ref_id: str
    :param limit: pagination limit
    :type limit: int
    :return: data as dict
    """
    try:
        if cname is None and ref_id is None:
            api = API_BASE + "/proposals"
        if cname is None and ref_id is not None:
            api = API_BASE + "/proposals/" + ref_id
        if cname is not None and ref_id is None:
            api = API_BASE + "/protocols/" + cname + "/proposals"
        if limit is not None:
            api += "?limit={0}".format(limit)
        response = requests.get(api)
        if response.status_code == 200:
            data_json = response.json()
            return data_json["data"]
        return None
    except Exception:
        return None
    

def get_vote(address = None, ref_id = None, limit = None):
    """
    Get vote details.
    :param address:  address
    :type address: str
    :param ref_id:  protocol ref_id
    :type ref_id: str
    :param limit: pagination limit
    :type limit: int
    :return: data as dict
    """
    try:
        if address is None and ref_id is not None:
            api = API_BASE + "/proposals/" + ref_id + "/votes"
        if address is not None and ref_id is None:
            api = API_BASE + "/voters/" + address + "/votes"
        if limit is not None:
            api += "?limit={0}".format(limit)
        response = requests.get(api)
        if response.status_code == 200:
            data_json = response.json()
            return data_json["data"]
        return None
    except Exception:
        return None

def get_voter(cname = None, address = None, limit = None):
    """
    Get vote details.
    :param cname:  protocol cname
    :type cname: str
     :param address:  address
    :type address: str
    :param limit: pagination limit
    :type limit: int
    :return: data as dict
    """
    try:
        if cname is None and address is  None:
            api = API_BASE + "/voters"
        if cname is not None and address is None:
            api = API_BASE + "/protocols/" + cname + "/voters"
        if cname is None and address is not None:
            api = API_BASE + "/voters/" + address
        if limit is not None:
            api += "?limit={0}".format(limit)
        response = requests.get(api)
        if response.status_code == 200:
            data_json = response.json()
            return data_json["data"]
        return None
    except Exception:
        return None 

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

def results_convert(results):
    """
    Convert result to proper format.
    :param results: results
    :type results: list
    :return: converted data as dict
    """
    result_dict = {}
    for item in results:
        result_dict[item["choice"]] = item["total"]
    return result_dict