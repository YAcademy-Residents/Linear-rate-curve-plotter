import matplotlib.pyplot as plt

# Set start and end points of each curve
# To get the curve data for Compound and Aave
# mouse over the graph on their UIs
# Compound: https://app.compound.finance/markets?market=v2
# Aave: https://app.aave.com/markets/?marketName=proto_mainnet

# There are 3 key points:
# 1. y-intercept (0% utilization ratio)
# 2. kink point (usually near 80% utilization ratio)
# 3. max rate at 100% utilization ratio
plt.plot([0,90,100],[5,10,20], label='Demo')
plt.plot([0,80,100],[0,5,32], label='Compound')
plt.plot([0,80,100],[0,5,80], label='Aave')

# Set text
plt.title('DAI Borrow Rate Protocol Comparison')
plt.xlabel('Utilization Ratio')
plt.ylabel('Borrow Interest Rate')

# Show legend and plot
plt.legend()
plt.show()
