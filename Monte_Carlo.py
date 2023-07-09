# Importing Packages
import numpy as np
import matplotlib.pyplot as plt

# Initializing the variables as given in question
timesteps = 30
starting_price = 600
volatility = 0.02
max_simulations = 5000

# Introducing the 2-d array which stores all the prices of 31 days and 5000 simulations
all_prices = np.empty((0,31),np.float16)




for i in range(max_simulations):
    prices_each_sim = np.array([starting_price])#Initialising the array which stores the prices for each simulation of 30 days
    
    
    append_price_val = prices_each_sim[0]*(1+np.random.normal(0,volatility))#Calulating the next day price from previous day price
    prices_each_sim = np.append(prices_each_sim,[append_price_val], axis = 0)
    
    for j in range(timesteps-1):
       
        append_price_val = prices_each_sim[j+1]*(1+np.random.normal(0,volatility))#Calulating the next day price from previous day price
        prices_each_sim = np.append(prices_each_sim,[append_price_val], axis=0)
     
        
    all_prices = np.append(all_prices,[prices_each_sim],axis = 0)#Storing the prices of each simulation into the 2-d array as rows
    
    plt.subplot(2,1,1)
    plt.plot(all_prices[i,:])
    plt.xlabel('Day No.')
    plt.ylabel('Stock Price')
    plt.title('Paths by Monte Carlo Simulations')


print("Prediction of 30th Day stock price from Monte-Carlo Simulations is : " , (all_prices[:,30].sum(axis=0))/max_simulations)
plt.subplot(2,1,2)
plt.hist(all_prices[:,30],100)#Plotting the histogram
plt.xlabel('Stock prices')
plt.ylabel('No. of Occurences')
plt.title('Distribution of Final Stock Price')
plt.tight_layout()
plt.savefig("Monte-Carlo graphs.png")
plt.show()