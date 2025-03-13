#Task2: Generate logistic curve
#Nt = K / (1 + (2.71828**(-r*t)))where Nt is the population size at generation (time) t, K is the carrying capacity, r is the growth rate and t is the generation(time)
def logistic_curve(Nt, cycle, r=0.2, K = 1000, lag_range= 5, exp_range = 15):#lag_range and exp_range are random values to simulate the number of generations fpr the lag phase and exponential phase respectively
    population_size = {}
    for cycles in range (1, cycle+1):#"cycle + 1" is to meet the actual generation time, cycles is the same as time or generation
        if cycles <= lag_range:# The first five generations should represent the lag phase, where populatioon size (N) is more or less constant as microbes are getting adapted to their environment
            logistic_growth = Nt
            population_size.update({cycles : logistic_growth})
        elif cycles > lag_range and cycles <= exp_range and logistic_growth < 600:#The next seven generations  represent the exponential (log) phase. Another criteria for exponential growth is that population size (N) should be less than the carrying capacity at a value of 600
            exp_growth = Nt * 2.71828**(r*cycles)# 2.718282 is the value for "e"
            #Check if the exponential growth is greater than 80% of the carrying capacity (800). If it is, use the logistic formula. If not, calculate the exponential phase using the exponential formula
            if exp_growth > 800:
                logistic_growth = K / (1 + (2.71828**(-r*cycles)))
                population_size.update({cycles : logistic_growth})
            else:
                logistic_growth = exp_growth
                population_size.update({cycles : logistic_growth})
        elif cycles > exp_range and logistic_growth <= 800:# if after 12 generations, the population size is way below the carrying capacity at an estimated figure of less than 800, continue in the exponential phase. If not, move to the stationary phase
            exp_growth = Nt * 2.71828**(r*cycles)
            #Check if value is greater than carrying capacity. If it is, use the logistic formula. If not, calculate the exponential phase using the exponential formula
            if exp_growth > K:
                logistic_growth = K / (1 + (2.71828**(-r*cycles)))
                population_size.update({cycles : logistic_growth})
            else:
                logistic_growth = exp_growth
                population_size.update({cycles : logistic_growth})
        elif cycles > exp_range and logistic_growth > 800:#If the population size is close to the carrying capacity, i.e greater than 800, use the logistic growth model to simulate the stationary phase
            logistic_growth = K / (1 + (2.71828**(-r*cycles)))
            if logistic_growth >= K:#If a value is more than or equal to the carrying capacity, end the code
                print(f"For generation {cycles}, the population size is {logistic_growth} which is equal to the carrying capacity 'K' of the population\n\n")
                break
            else:
                population_size.update({cycles : logistic_growth})
    print(f"The Generation time : Population size is given as {population_size}")
    return Nt
    return r
    return K
    return logistic_growth
example = logistic_curve(50, 500)
