# -*- coding: utf-8 -*-
"""Boardroom Protocol object."""
import datetime
from warnings import warn
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
        self.last_update_data = None
        self.last_update_proposals = None
        self.last_update_voters = None
        try:
            self.update_data()
        except UpdateError:
            warn(PROTOCOL_UPDATE_WARNING)

    def update_data(self, retry_number=2):
        """
        Update protocol data.

        :param retry_number: retry number
        :type retry_number: int
        :return: None
        """
        api_flag = False
        retry_counter = 0
        while(retry_counter < retry_number):
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
                api_flag = True
                break
            else:
                retry_counter += 1
        if api_flag == False:
            raise UpdateError(PROTOCOL_DATA_UPDATE_ERROR)

    def update_proposals(self, limit=None, retry_number=2):
        """
        Update protocol proposals.

        :param limit: pagination limit
        :type limit: int
        :param retry_number: retry number
        :type retry_number: int
        :return: None
        """
        self.proposals = {}
        if limit is None:
            limit = self.total_proposals
        api_flag = False
        retry_counter = 0
        while(retry_counter < retry_number):
            data = get_proposal(cname = self.cname, limit = limit)
            if data is not None:
                for proposal in data:
                    self.proposals[proposal["refId"]] = {
                        "title":proposal["title"],
                        "content":proposal["content"],
                        "choices":proposal["choices"],
                        "proposer":proposal["proposer"],
                        "total_votes":proposal["totalVotes"],
                        "start_time":proposal["startTimestamp"],
                        "end_time":proposal["endTimestamp"],
                        "state":proposal["currentState"],
                        "results":results_convert(proposal["results"])}
                self.last_update_proposals = datetime.datetime.now().timestamp()
                api_flag = True
                break
            else:
                retry_counter += 1
        if api_flag == False:
            raise UpdateError(PROTOCOL_PROPOSALS_UPDATE_ERROR)

    def update_voters(self, limit = None, retry_number=2):
        """
        Update protocol voters.

        :param limit: pagination limit
        :type limit: int
        :param retry_number: retry number
        :type retry_number: int
        :return: None
        """
        self.voters = {}
        if limit is None:
            limit = self.total_votes
        api_flag = False
        retry_counter = 0
        while(retry_counter < retry_number):
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
                api_flag = True
                break
            else:
                retry_counter += 1
        if api_flag == False:
            raise UpdateError(PROTOCOL_VOTERS_UPDATE_ERROR)

    def update(self, limit = None, retry_number=2):
        """
        Update protocol data, proposals and voters.

        :param limit: pagination limit
        :type limit: int
        :param retry_number: retry number
        :type retry_number: int
        :return: None
        """
        self.update_data(retry_number = retry_number)
        self.update_proposals(limit=limit, retry_number=retry_number)
        self.update_voters(limit=limit,retry_number=retry_number)




