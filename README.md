# Boardroom

<div align="center">
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3" /></a>
<a href="https://badge.fury.io/py/boardroom"><img src="https://badge.fury.io/py/boardroom.svg" alt="PyPI version" height="18"></a>
</div>

----------

## Overview
This package will help you to work with Boardroom API in Python.

## Installation		

### Source code
- Download [Version 0.1](https://github.com/sepandhaghighi/boardroom/archive/v0.1.zip) or [Latest Source ](https://github.com/sepandhaghighi/boardroom/archive/dev.zip)
- Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` (Need root access)
- Run `python3 setup.py install` or `python setup.py install` (Need root access)				

### PyPI


- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- Run `pip install boardroom==0.1` or `pip3 install boardroom==0.1` (Need root access)

### Easy install

- Run `easy_install --upgrade boardroom` (Need root access)

## Usage
	
### Proposal

#### Initializing
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
>>> proposal_1.update_data()
>>> proposal_1.update_data(retry=5)
>>> proposal_1.last_update_data # Last data update timestamp
1630932971.748473
```

#### Update Votes
```pycon
>>> proposal_1.update_votes()
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
>>> proposal_1.update_votes(limit=10,retry=5)
>>> proposal_1.last_update_votes
1630933297.228164
```

#### Update Data + Votes
```pycon
>>> proposal_1.update()
>>> proposal_1.update(limit=3)
>>> proposal_1.update(limit=3,retry=4)
```

### Protocol

#### Initializing
```pycon
>>> from boardroom import Protocol
>>> protocol_1 = Protocol(cname = "aave")
>>> protocol_1.total_proposals
31
>>> protocol_1.unique_voters
754
```

#### Update Data
```pycon 
>>> protocol_1.update_data()
>>> protocol_1.update_data(retry=5)
>>> protocol_1.last_update_data
1630958815.165922
```

#### Update Proposals
```pycon
>>> protocol_1.update_proposals()
>>> len(protocol_1.proposals)
31
>>> proposals = list(protocol_1.proposals.keys())
>>> proposals[:5]
['cHJvcG9zYWw6YWF2ZTpkZWZhdWx0OjIz', 'cHJvcG9zYWw6YWF2ZTpkZWZhdWx0OjI4', 'cHJvcG9zYWw6YWF2ZTpkZWZhdWx0OjY=', 'cHJvcG9zYWw6YWF2ZTpkZWZhdWx0OjE=', 'cHJvcG9zYWw6YWF2ZTpkZWZhdWx0Ojc=']
>>> protocol_1.proposals["cHJvcG9zYWw6YWF2ZTpkZWZhdWx0OjIz"]
{'total_votes': 24, 'proposer': '0x32a9d6A550C3D89284D5700F7d7758dBc6f0fB2C', 'state': 'executed', 'content': '\n\n## Simple Summary\n\nThis proposes raising the maximum AMPL interest rate to better balance incentives between the borrow and deposit sides of the market.\n\n## Motivation\n\nFollowing [API-12](https://governance.aave.com/t/proposal-add-support-for-ampl/854/8), [AMPL borrowing & depositing](https://app.aave.com/reserve-overview/AMPL-0xd46ba6d942050d489dbd938a2c909a5d5039a1610xb53c1a33016b2dc2ff3653530bff1848a515c8c5) went live on the AAVE v2 market [date=2021-07-24 time=20:22:00 timezone="UTC"].\n\nSince then, there has been a near 100% utilization rate of deposited assets. This suggests the maximum cap of the interest rate curve is not able to reach a high enough value to effectively balance incentives between the borrow side and depositing side of the marketplace.\n\n![Deposit and Borrow APY on AAVE, 7/24/21](../assets/AIP-26/apys.png "Deposit and Borrow APY on AAVE, 7/24/21")\n\nWhile the AMPL spot market is currently in a relatively extreme condition, the AAVE borrowing market should be able to perform efficiently in all market scenarios.\n\n## Specification\n\nWe suggest the following parameters for AAVE\'s default [interest rate model](https://docs.aave.com/risk/liquidity-risk/borrow-interest-rate#interest-rate-model):\n\n- Optimal utilization = 75%\n- Slope1 = 2%\n- Slope2 = 10,000%\n\nThis leads to a piecewise linear curve with two parts and three defining points:\n\n- Borrow Interest(0) = 0% APY\n- Borrow Interest(75) = 2% APY\n- Borrow Interest(100) = 10002 % APY\n\n## Rationale\n\nA higher cap of the borrow interest rate will allow the marketplace to have a more sustainable equilibrium.\n\nSince this will result in overall higher fees coming into the system, in tandem we also suggest lowering the reserve factor from 20% to 10% to incentivize more depositors. This would be submitted as a separate AIP to decouple these two decisions.\n\nWe believe a nonlinear interest curve is healthiest long-term and could likely be used by many other assets as well, however this work can be discussed more in the future.\n\n## Implementation\n\nA deployment of the existing implementation of the Interest Strategy will be used, with the following parameters:\n\n    optimalUtilizationRate: new BigNumber(0.75).multipliedBy(oneRay).toFixed(),\n    baseVariableBorrowRate: new BigNumber(0).multipliedBy(oneRay).toFixed(),\n    variableRateSlope1: new BigNumber(0.02).multipliedBy(oneRay).toFixed(),\n    variableRateSlope2: new BigNumber(100).multipliedBy(oneRay).toFixed(),\n\n[https://etherscan.io/address/0x509859687725398587147Dd7A2c88d7316f92b02#readContract](https://etherscan.io/address/0x509859687725398587147Dd7A2c88d7316f92b02#readContract)\n\n## Copyright\n\nCopyright and related rights waived via [CC0](https://creativecommons.org/publicdomain/zero/1.0/).\n', 'end_time': 1628359654, 'title': 'Raise Maximum Interest Rate on AMPL Market', 'start_time': 1628102256, 'choices': ['NAY', 'YAE'], 'results': {1: 374539.62}}
>>> protocol_1.update_proposals(limit=5)
>>> len(protocol_1.proposals)
5
>>> protocol_1.update_proposals(limit=5,retry=4)
>>> protocol_1.last_update_proposals
1630960429.839166
```

#### Update Voters
```pycon
>>> protocol_1.update_voters()
>>> len(protocol_1.voters)
754
>>> voters = list(protocol_1.voters.keys())
>>> voters[:5]
['0xD34A7095B8aAd4A4A125a2bFaB003A030f319Fc3', '0x865Ba550Cc0E6f3bC82171C42c5a6Ed4Ab975c64', '0x0d64aDd7AA3a19392A8afA3a07dAaF0f7098776D', '0xC2634B9d0A0cFb756cDed34656E09828072A8a9B', '0xCBB08e918e828Bfd46A0E32E3365E80D7502c7D9']
>>> protocol_1.voters["0xD34A7095B8aAd4A4A125a2bFaB003A030f319Fc3"]
{'protocols': [{'totalVotesCast': 1, 'protocol': 'aave', 'lastCastPower': 70.10188, 'totalPowerCast': 70.10188, 'firstVoteCast': 1610181292, 'lastVoteCast': 1610181292}, {'totalVotesCast': 2, 'protocol': 'compound', 'lastCastPower': 1.4661654, 'totalPowerCast': 2.9323308, 'firstVoteCast': 1607418487, 'lastVoteCast': 1607418506}, {'totalVotesCast': 1, 'protocol': 'mantraDao', 'lastCastPower': 80937260000, 'totalPowerCast': 80937260000, 'firstVoteCast': 1613545446, 'lastVoteCast': 1613545446}, {'totalVotesCast': 6, 'protocol': 'rarible', 'lastCastPower': 304.63812, 'totalPowerCast': 1814.8164, 'firstVoteCast': 1600495879, 'lastVoteCast': 1608289668}, {'totalVotesCast': 2, 'protocol': 'uniswap', 'lastCastPower': 200, 'totalPowerCast': 400, 'firstVoteCast': 1602922561, 'lastVoteCast': 1603569382}], 'first_voteCast': 1610181292, 'total_votesCast': 1, 'last_voteCast': 1610181292}
>>> protocol_1.update_voters(limit=5)
>>> len(protocol_1.voters)
5
>>> protocol_1.update_voters(limit=5,retry=4)
>>> protocol_1.last_update_voters
1630960558.200357
```

#### Update Data + Proposals + Voters
```pycon
>>> protocol_1.update()
>>> protocol_1.update(limit=3)
>>> protocol_1.update(limit=3,retry=4)
```

### Voter

#### Initializing
```pycon
>>> from boardroom import Voter
>>> voter_1 = Voter(address="0xd409ceA9dD8dB30504168063953cE1Fa20748cab")
>>> voter_1.last_vote_cast
1625066741
>>> voter_1.protocols
[{'lastCastPower': 147811.42, 'firstVoteCast': 1625066741, 'protocol': 'sushi', 'lastVoteCast': 1625066741, 'totalPowerCast': 147811.42, 'totalVotesCast': 1}]
```

#### Update Data
```pycon 
>>> voter_1.update_data()
>>> voter_1.update_data(retry=4)
>>> voter_1.last_update_data
1630960776.79719
```

#### Update Votes
```pycon
>>> voter_1.update_votes()
>>> len(voter_1.votes)
1
>>> voter_1.votes
{'dm90ZTpzdXNoaTpkZWZhdWx0OnFtczdreWM0a3I2ZTFnc3Njc2s1bXBvZWRma3R3OG9ocXJjYWgzams3bXc3NWs6MHhkNDA5Y2VhOWRkOGRiMzA1MDQxNjgwNjM5NTNjZTFmYTIwNzQ4Y2Fi': {'proposal_refId': 'cHJvcG9zYWw6c3VzaGk6ZGVmYXVsdDpxbXM3a3ljNGtyNmUxZ3NzY3NrNW1wb2VkZmt0dzhvaHFyY2FoM2prN213NzVr', 'protocol': 'sushi', 'power': 147811.42, 'choice': 0, 'proposal_info': {'currentState': 'active', 'startTime': {'timestamp': 1623031200}, 'choices': ['YES', 'YES'], 'endTimestamp': 1684980000, 'events': [], 'title': 'Buy MemePad - https://memepad.co/ - LaunchPad for Meme coins', 'endTime': {'timestamp': 1684980000}, 'startTimestamp': 1623031200}, 'proposal_id': 'QmS7kYC4KR6E1gssCsK5MPoeDfktW8oHqRCaH3jK7mW75K', 'adapter': 'default', 'address': '0xd409ceA9dD8dB30504168063953cE1Fa20748cab'}}
>>> voter_1.last_update_votes
1630960887.87681
>>> voter_1.update_votes(limit=5)
>>> voter_1.update_votes(limit=5,retry=4)
>>> len(voter_1.votes)
1
```

#### Update Data + Votes
```pycon
>>> voter_1.update()
>>> voter_1.update(limit=4)
>>> voter_1.update(limit=4,retry=5)
```

#### Reputation
```pycon
>>> voter_1.reputation("aave")
0
>>> voter_1.reputation("sushi")
0
>>> voter_2 = Voter(address="0xb577935e2E630579e926C1d2201E2C6a8603D70b")
>>> voter_2.reputation("aave")
1
>>> voter_3 = Voter(address="0xA7499Aa6464c078EeB940da2fc95C6aCd010c3Cc")
>>> voter_3.update_votes()
>>> voter_3.reputation("aave")
3.9997581478173947
```
[How is the reputation score calculated?](https://github.com/sepandhaghighi/boardroom/blob/master/REPUTATION.md)