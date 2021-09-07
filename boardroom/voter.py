# -*- coding: utf-8 -*-
"""Boardroom Voter object."""
import datetime
from warnings import warn
from .functions import *
from .errors import UpdateError
from .proposal import Proposal
from .protocol import Protocol
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
        self.last_update_data = None
        self.last_update_votes = None
        try:
            self.update_data()
        except UpdateError:
            warn("Object is created but ...")


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

    def reputation(self,cname):
        """
        Calculate reputation of a voter.

        :param cname: protocol cname
        :type cname: str
        :return: reputation score
        """
        vote_list = list(self.votes.keys())
        user_reputation = 0
        for ref_id in vote_list:
            if self.votes[ref_id]["protocol"] == cname:
                proposal_ref_id = self.votes[ref_id]["proposal_refId"]
                proposal = Proposal(ref_id = proposal_ref_id)
                if proposal.state == "executed":
                    choice = self.votes[ref_id]["choice"]
                    user_reputation += proposal.results[choice] / sum(proposal.results.values())
        protocol = Protocol(cname = cname)
        protocol.update_proposals()
        proposals_list = list(protocol.proposals.keys())
        for ref_id in proposals_list:
            if protocol.proposals[ref_id]["proposer"] == self.address and protocol.proposals[ref_id]["state"] == "executed":
                user_reputation += 1
        return user_reputation





