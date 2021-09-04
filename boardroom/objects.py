# -*- coding: utf-8 -*-
"""Boardroom objects."""
import datetime
from .functions import *


class Proposal():

    def __init__(self,ref_id):
        self.ref_id = ref_id
        self.id = None
        self.title = None
        self.content = None
        self.protocol = None
        self.adaptor = None
        self.proposer = None
        self.total_votes = None
        self.block_number = None
        self.url = None
        self.start_time = None
        self.end_time = None
        self.state = None
        self.choices = None
        self.results = None
        self.last_update_data = None
        self.last_update_votes = None
        self.votes = []

    def update_data(self):
        data = get_proposal(ref_id=self.ref_id)
        if data is not None:
            self.id = data["id"]
            self.title = data["title"]
            self.content = data["content"]
            self.protocol = data["protocol"]
            self.adaptor = data["adaptor"]
            self.proposer = data["proposer"]
            self.total_votes = data["totalVotes"]
            self.block_number = data["blockNumber"]
            self.url = data["externalUrl"]
            self.start_time = data["startTimestamp"]
            self.end_time = data["endTimestamp"]
            self.state = data["currentState"]
            self.choices = data["choices"]
            self.results = data["results"]
            self.last_update_data = datetime.datetime.now().timestamp()

    def update_votes(self):
        data = get_vote(ref_id = self.ref_id)
        if data is not None:
            for vote in data:
                self.votes.append({vote["address"]:{"power":vote["power"],"choice":vote["choice"]}})
            self.last_update_votes = datetime.datetime.now().timestamp()

    def update_all(self):
        self.update_data()
        self.update_votes()




