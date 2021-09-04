# -*- coding: utf-8 -*-
"""Boardroom Voter object."""
import datetime
from .functions import *


class Voter():

    def __init__(self, address):
        self.address = address
        self.first_vote_cast = None
        self.last_vote_cast = None
        self.total_votes_cast = None
        self.protocols = None
        self.next_cursor = None
        self.last_update_data = None
        self.last_update_votes = None
        self.votes = {}

    def update_data(self):
        data = get_voter(address=self.address)
        if data is not None:
            self.address = data["address"]
            self.first_vote_cast = data["firstVoteCast"]
            self.last_vote_cast = data["lastVoteCast"]
            self.total_votes_cast = data["totalVotesCast"]
            self.protocols = data["protocols"]
            self.next_cursor = data["nextCursor"]
            self.last_update_data = datetime.datetime.now().timestamp()

    def update_votes(self):
        data = get_vote(address = self.address)
        if data is not None:
            for vote in data:
                self.votes[vote["refId"]] = {
                    "proposal_refId": vote["proposalRefId"],
                    "protocol": vote["protocol"],
                    "adapter": vote["adapter"],
                    "proposal_id": vote["proposalId"],
                    "address": vote["address"],
                    "power": vote["power"],
                    "choice": vote["choice"],
                    "proposal_info": vote["proposalInfo"],
                    "current_state": vote["currentState"]
                }
            self.last_update_votes = datetime.datetime.now().timestamp()


    def update_all(self):
        self.update_data()
        self.update_votes()



