# -*- coding: utf-8 -*-
"""Boardroom Proposal objects."""
import datetime
from warnings import warn
from .functions import *
from .errors import UpdateError
from .params import *


class Proposal():

    def __init__(self,ref_id):
        """
        Proposal init method.

        :param ref_id: protocol ref_id
        :type ref_id: str
        """
        self.ref_id = ref_id
        self.votes = {}
        self.last_update_data = None
        self.last_update_votes = None
        try:
            self.update_data()
        except UpdateError:
            warn(PROPOSAL_UPDATE_WARNING)

    def update_data(self,retry_number=2):
        """
        Update proposal data.

        :param retry_number: retry number
        :type retry_number: int
        :return: None
        """
        retry_counter = 0
        api_flag = False
        while(retry_counter<retry_number):
            data = get_proposal(ref_id=self.ref_id)
            if data is not None:
                self.id = data["id"]
                self.title = data["title"]
                self.content = data["content"]
                self.protocol = data["protocol"]
                self.adapter = data["adapter"]
                self.proposer = data["proposer"]
                self.total_votes = data["totalVotes"]
                self.block_number = data["blockNumber"]
                self.start_time = data["startTimestamp"]
                self.end_time = data["endTimestamp"]
                self.state = data["currentState"]
                self.choices = data["choices"]
                self.results = results_convert(data["results"])
                self.last_update_data = datetime.datetime.now().timestamp()
                api_flag = True
                break
            else:
                retry_counter += 1
        if api_flag == False:
            raise UpdateError(PROPOSAL_DATA_UPDATE_ERROR)

    def update_votes(self, limit=None, retry_number=2):
        """
        Update proposal votes.

        :param limit: pagination limit
        :type limit: int
        :param retry_number: retry number
        :type retry_number: int
        :return: None
        """
        self.votes = {}
        if limit is None:
            limit = self.total_votes
        retry_counter = 0
        api_flag = False
        while(retry_counter < retry_number):
            data = get_vote(ref_id = self.ref_id,limit=limit)
            if data is not None:
                for vote in data:
                    self.votes[vote["address"]] = {"power":vote["power"],"choice":vote["choice"]}
                self.last_update_votes = datetime.datetime.now().timestamp()
                api_flag = True
                break
            else:
                retry_counter += 1
        if api_flag == False:
            raise UpdateError(PROPOSAL_VOTES_UPDATE_ERROR)

    def update(self, limit=None, retry_number=2):
        """
        Update proposal data and votes.

        :param limit: pagination limit
        :type limit: int
        :param retry_number: retry number
        :type retry_number: int
        :return: None
        """
        self.update_data(retry_number = retry_number)
        self.update_votes(limit = limit, retry_number = retry_number)




