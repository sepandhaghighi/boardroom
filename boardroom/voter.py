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
            warn(VOTER_UPDATE_WARNING)


    def update_data(self,retry_number=2):
        """
        Update voter data.

        :param retry_number: retry number
        :type retry_number: int
        :return: None
        """
        api_flag = False
        retry_counter = 0
        while(retry_counter<retry_number):
            data = get_voter(address=self.address)
            if data is not None:
                self.address = data["address"]
                self.first_vote_cast = data["firstVoteCast"]
                self.last_vote_cast = data["lastVoteCast"]
                self.total_votes_cast = data["totalVotesCast"]
                self.protocols = data["protocols"]
                self.last_update_data = datetime.datetime.now().timestamp()
                api_flag = True
                break
            else:
                retry_counter += 1
        if api_flag == False:
            raise UpdateError(VOTER_DATA_UPDATE_ERROR)

    def update_votes(self, limit=None, retry_number=2):
        """
        Update voter votes.

        :param limit: pagination limit
        :type limit: int
        :param retry_number: retry number
        :type retry_number: int
        :return: None
        """
        self.votes = {}
        if limit is None:
            limit = self.total_votes_cast
        api_flag = False
        retry_counter = 0
        while(retry_counter<retry_number):
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
                api_flag = True
                break
            else:
                retry_counter += 1
        if api_flag == False:
            raise UpdateError(VOTER_VOTES_UPDATE_ERROR)


    def update(self, limit=None, retry_number=2):
        """
        Update voter data and votes

        :param limit: pagination limit
        :type limit: int
        :param retry_number: retry number
        :type retry_number: int
        :return: None
        """
        self.update_data(retry_number = retry_number)
        self.update_votes(limit = limit, retry_number=retry_number)

    def reputation(self,cname,retry_number=2):
        """
        Calculate reputation of a voter.

        :param cname: protocol cname
        :type cname: str
        :param retry_number: retry number
        :type retry_number: int
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
        protocol.update_proposals(retry_number = retry_number)
        proposals_list = list(protocol.proposals.keys())
        for ref_id in proposals_list:
            if protocol.proposals[ref_id]["proposer"] == self.address and protocol.proposals[ref_id]["state"] == "executed":
                user_reputation += 1
        return user_reputation





