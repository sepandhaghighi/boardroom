# Boardroom

----------

## Usage

		
### Proposal

### Initializing
```pycon
>>> from boardroom import Proposal
>>> proposal_1 = Proposal(ref_id = "cHJvcG9zYWw6c3VzaGk6ZGVmYXVsdDpxbXM3a3ljNGtyNmUxZ3NzY3NrNW1wb2VkZmt0dzhvaHFyY2FoM2prN213NzVr")
>>> proposal_1.ref_id
'cHJvcG9zYWw6c3VzaGk6ZGVmYXVsdDpxbXM3a3ljNGtyNmUxZ3NzY3NrNW1wb2VkZmt0dzhvaHFyY2FoM2prN213NzVr'
>>> proposal_1.title
'Buy MemePad - https://memepad.co/ - LaunchPad for Meme coins'
```

#### Update Data
```pycon 
>>> proposal_1.update_data() # Update proposal data
>>> proposal_1.last_update_data # Last data update timestamp
1630932971.748473
```

#### Update Votes
```pycon
>>> proposal_1.update_votes() # Update proposal votes
>>> len(proposal_1.votes)
266
>>> votes_address = list(proposal_1.votes.keys())
>>> votes_address[:5]
['0x9172E788cd829D75E913E53452B49bb43D32bAD4', '0x58a04F65195807bE04317068Bc68c03927E2d064', '0x98071fc469cF2fDCE21C4A9d06DB0BcA1A22a07A', '0x8513d7bA8e43b0Bf27E71CAAA3BE1c66e12871Db', '0x1C35500ed22286Ca91239CFA584C4b8efCB638C5']
>>> proposal_1.votes['0x9172E788cd829D75E913E53452B49bb43D32bAD4']
{'choice': 0, 'power': 1.2708462}
>>> proposal_1.update_votes(limit=10)
>>> len(proposal_1.votes)
10
>>> proposal_1.last_update_votes  # Last votes update timestamp
1630933297.228164
```

#### Update Data + Votes
```pycon
>>> proposal_1.update() # Update proposal votes + data
```