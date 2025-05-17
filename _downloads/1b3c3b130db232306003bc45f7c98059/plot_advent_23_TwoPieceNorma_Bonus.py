"""
Day 23: Two-Piece Normal Distribution with Fanchart
===================================================

"""

###############################################################################

# Author: Dialid Santiago <d.santiago@outlook.com>
# License: MIT
# Description: Advent Calendar 2023

from fanchart.plot import *


probs = [0.05, 0.20, 0.35, 0.65, 0.80, 0.95]

parameters = load_boe_parameters()
history = load_boe_history()
# fan(pars=parameters, probs=probs,
#     historic=history[history.Date >= '2018'],
#     title="CPI inflation projection 2022-Q2"
#           "\nSource: Bank of England")


fig = fan(pars=parameters, probs=probs,
          historic=history[history.Date >= '2019'],
          title="CPI inflation projection 2023-Q3 based on constant interest rates at 5.25%, other policy measures as "
                "announced "
                "\nData Source: Bank of England")

# fig.savefig("23_TwoPieceNormal_Bonus_Fanchart_2023")
