# -*- coding: utf-8 -*-
"""Boardroom Protocol object."""
import datetime
from .functions import *
from .errors import UpdateError
from .params import *


class Protocol():

    def __init__(self, cname):
        """
        Protocol init method.

        :param cname: protocol cname
        :type cname: str
        """
        self.cname = cname
        self.proposals = {}
        self.voters = {}
        self.update()

    def update_data(self):
        """
        Update protocol data.

        :return: None
        """
        data = get_protocol(cname=self.cname)
        if data is not None:
            self.cname = data["cname"]
            self.name = data["name"]
            self.total_proposals = data["totalProposals"]
            self.total_votes = data["totalVotes"]
            self.unique_voters = data["uniqueVoters"]
            self.icons = data["icons"]
            self.tokens = data["tokens"]
            self.last_update_data = datetime.datetime.now().timestamp()
        else:
            raise UpdateError(PROTOCOL_DATA_UPDATE_ERROR)

    def update_proposals(self, limit=None):
        """
        Update protocol proposals.

        :param limit: pagination limit
        :type limit: int
        :return: None
        """
        self.proposals = {}
        if limit is None:
            limit = self.total_proposals
        data = get_proposal(cname = self.cname, limit = limit)
        if data is not None:
            for proposal in data:
                self.proposals[proposal["title"]] = {"content":proposal["content"],"choices":proposal["choices"]}
            self.last_update_proposals = datetime.datetime.now().timestamp()
        else:
            raise UpdateError(PROTOCOL_PROPOSALS_UPDATE_ERROR)

    def update_voters(self, limit = None):
        """
        Update protocol voters.

        :param limit: pagination limit
        :type limit: int
        :return: None
        """
        self.voters = {}
        if limit is None:
            limit = self.total_votes
        data = get_voter(cname = self.cname, limit = limit)
        if data is not None:
            for voter in data:
                self.voters[voter["address"]] = {
                    "first_voteCast":voter["firstVoteCast"],
                     "last_voteCast":voter["lastVoteCast"],
                      "total_votesCast":voter["totalVotesCast"],
                      "protocols":voter["protocols"]
                }
            self.last_update_voters = datetime.datetime.now().timestamp()
        else:
            raise UpdateError(PROTOCOL_VOTERS_UPDATE_ERROR)

    def update(self):
        """
        Update protocol data, proposals and voters.

        :return: None
        """
        self.update_data()
        self.update_proposals()
        self.update_voters()




