# -*- coding: utf-8 -*-
"""Boardroom Protocol object."""
import datetime
from .functions import *


class Protocol():

    def __init__(self, cname):
        self.cname = cname
        self.name = None
        self.total_proposals = None
        self.total_votes = None
        self.unique_voters = None
        self.icons = None
        self.tokens = None
        self.last_update_data = None
        self.last_update_proposals = None
        self.last_update_voters = None
        self.proposals = {}
        self.voters = {}

    def update_data(self):
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

    def update_proposals(self):
        data = get_proposal(cname = self.cname)
        if data is not None:
            for proposal in data:
                self.proposals[proposal["title"]] = {"content":proposal["content"],"choices":proposal["choices"]}
            self.last_update_proposals = datetime.datetime.now().timestamp()

    def update_voters(self):
        data = get_voter(cname = self.cname)
        if data is not None:
            for voter in data:
                self.voters[voter["address"]] = {
                    "first_voteCast":voter["firstVoteCast"],
                     "last_voteCast":voter["lastVoteCast"],
                      "total_votesCast":voter["totalVotesCast"],
                      "protocols":voter["protocols"]
                }
            self.last_update_voters = datetime.datetime.now().timestamp()

    def update_all(self):
        self.update_data()
        self.update_proposals()
        self.update_voters()




