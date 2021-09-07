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

    def update_data(self):
        """
        Update proposal data.

        :return: None
        """
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
            self.url = data["externalUrl"]
            self.start_time = data["startTimestamp"]
            self.end_time = data["endTimestamp"]
            self.state = data["currentState"]
            self.choices = data["choices"]
            self.results = results_convert(data["results"])
            self.last_update_data = datetime.datetime.now().timestamp()
        else:
            raise UpdateError(PROPOSAL_DATA_UPDATE_ERROR)

    def update_votes(self, limit=None):
        """
        Update proposal votes.

        :param limit: pagination limit
        :type limit: int
        :return: None
        """
        self.votes = {}
        if limit is None:
            limit = self.total_votes
        data = get_vote(ref_id = self.ref_id,limit=limit)
        if data is not None:
            for vote in data:
                self.votes[vote["address"]] = {"power":vote["power"],"choice":vote["choice"]}
            self.last_update_votes = datetime.datetime.now().timestamp()
        else:
            raise UpdateError(PROPOSAL_VOTES_UPDATE_ERROR)

    def update(self):
        """
        Update proposal data and votes.

        :return: None
        """
        self.update_data()
        self.update_votes()




