##The Problem

*Reconciliation* is a term Addepar uses for a set of correctness and
consistency measures applied to the data we receive and use in financial
calculations.

One of the most common reconciliation checks is called *unit reconciliation*,
which answers the question, "does the tranasction history add up to the number
of shares the bank says I have?". For example, if the bank said I had 100
shares of Apple at the end of yesterday, and I bought 20 shares of Apple today,
then we expect the bank to report 120 shares at the end of today. This
surprisingly isn't always the case! The bank may send incomplete data, we may
be parsing it incorrectly, or there may be events like corporate actions or
trade settlement lag that cause an inconsistency.

Unit reconciliation is very important because numbers that don't add up
shouldn't be trusted for any metrics.

##The Input

e.g:

D0-POS
AAPL 100
GOOG 200
Cash 10

D1-TRN
AAPL SL 50 30000
GOOG BY 10 10000

D1-POS
AAPL 50
GOOG 220
Cash 20000

`recon.in` has three sections:

`D0-POS` describes the positions in the account at the end of Day 0. Each
record is a space-separated pair of Symbol and Shares. For example, "AAPL 10"
means 10 shares of AAPL were held at the end of Day 0, and "Cash 122.16"
means we had $122.16 in the account at the end of Day 0.

`D1-TRN` describes the transactions that occured in the account on Day 1.
Each record is a space-separated collection of four items:
Symbol, Transaction Code, Shares, and Total Value. For example,
"AAPL BY 10 6123.21" means 10 shares of AAPL were bought for a total cost of
$6123.21.

`D1-POS` describes the positions in the account at the end of Day 1, and has
the same format as `D0-POS`.

##The Output

e.g.

Cash -10
GOOG 10

The objective is to write a program that produces `recon.out`. Each line should
be a space-separated record indicating a position that fails unit
reconciliation. For example, "AAPL 10" means that the reported shares of AAPL
in `D1-POS` is 10 higher than expected based on the transactions.

[[D1-TRN]
[AAPL, SL, 50, 30000]
[GOOG, BY, 10, 10000]]

[AAPL,SL,50,30000]

def readfile():
    with open("recon.in", "r") as recon:
        arr = []
        for line in recon:
            arr.append(line)
    return arr
   
def recon():
    readfile()
    #dict of stocks
    stocks = {}
    cash = positions[-1][1]
    
    for i in range(1,len(positions)-1):
        stocks[positions[i][0]] = positions[i][1]
    #compute with TRN
    for i in range(1, len(trn)):
        if stocks[trn[i][0]]:
            if trn[i][1] == 'SL':
                stocks[trn[i][1]] -= trn[i][2]
                cash  += trn[i][3]
            else:
                stocks[trn[i][1]] += trn[i][2]
                cash  -= trn[i][3]
        else:
            stocks[trn[i][0]] = trn[i][2]
            cash -= trn[i][3]
    
    #compare stocks to D1-POS
    for i in range(1, len(d1pos)):
        if stocks.get(d1pos[i][0]) != d1pos[i][1]:
            print d1pos[i][0] + abs(stocks.get(d1pos[i][0]) - d1pos[i][1])
    
    recon_cash = cash - d1pos[-1][1]
    print recon_cash
    
            
        
    
    