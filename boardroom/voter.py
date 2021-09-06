# -*- coding: utf-8 -*-
"""Boardroom Voter object."""
import datetime
from .functions import *
from .errors import UpdateError
from .params import *


class Voter():

    def __init__(self, address):
        """
        Voter init method.

        :param address: protocol address
        :type address: str
        """
        self.address = address
        self.votes = {}
        self.update_data()

    def update_data(self):
        """
        Update voter data.

        :return: None
        """
        data = get_voter(address=self.address)
        if data is not None:
            self.address = data["address"]
            self.first_vote_cast = data["firstVoteCast"]
            self.last_vote_cast = data["lastVoteCast"]
            self.total_votes_cast = data["totalVotesCast"]
            self.protocols = data["protocols"]
            self.last_update_data = datetime.datetime.now().timestamp()
        else:
            raise UpdateError(VOTER_DATA_UPDATE_ERROR)

    def update_votes(self, limit=None):
        """
        Update voter votes.

        :param limit: pagination limit
        :type limit: int
        :return: None
        """
        self.votes = {}
        if limit is None:
            limit = self.total_votes_cast
        data = get_vote(address = self.address, limit=limit)
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
                    "proposal_info": vote["proposalInfo"]
                }
            self.last_update_votes = datetime.datetime.now().timestamp()
        else:
            raise UpdateError(VOTER_VOTES_UPDATE_ERROR)


    def update(self):
        """
        Update voter data and votes

        :return: None
        """
        self.update_data()
        self.update_votes()



