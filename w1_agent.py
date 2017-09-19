

from utils import *

import numpy as np


# create global variables for agent
local_action = None
this_action = None
agent_steps = None
this_initVal = None
this_epsilon = None
this_alpha = 0.1


# initialize agent
def agent_init():
	global prev_action,this_action,estimate_Vals,agent_steps,this_initVal,this_epsilon

	# create a array list to store the updated value of all bandits
	estimate_Vals = np.zeros(10)


	################################
	# set the Q1 and epsilon here!!!!
	this_epsilon = 0.1
	this_initVal = 0.0
	################################


	# initialize other variables using nessesary array or value
	prev_action = np.zeros(1)
	this_action = np.zeros(1)
	this_action[0] = prev_action[0]
	# initialize step, used to check if end of the run
	agent_steps = 0

	# set each element in estimate_val to initial value
	for x in range(len(estimate_Vals)):
		estimate_Vals[x] = this_initVal


# function to start the agent, gives the first randomly selected action
def agent_start(first_observation):
	global estimate_Vals,this_action,prev_action
	# randomly select the first action
	this_action[0] = randInRange(len(estimate_Vals))
	prev_action[0] = this_action[0]

	return this_action


# function to step through for agent, update each previously picked action's value
# also pick a new maximum value action
def agent_step(reward, this_observation):
	# print(reward)
	global prev_action,this_action,estimate_Vals,agent_steps, this_alpha,this_initVal,this_epsilon

	# for Debug process
	# print(estimate_Vals)
	# print("previous picked action is %d") % prev_action[0]
	# print("picked val is %f,actual reward is %f") % (estimate_Vals[prev_action[0]],reward)

	# increment time step by one for debug process
	agent_steps += 1
	# update the previouse action's Q(A) based on reward, and pre_action
	estimate_Vals[prev_action[0]] = estimate_Vals[prev_action[0]] + (this_alpha * (reward - estimate_Vals[prev_action[0]]) )

	# pick the action with currently largest estimated value
	# If not in epsilon situation
	if(rand_un() >= this_epsilon):
		# print  (agent_steps,"in large portion")
		# a list to store possible max actions
		max_nums = []
		max_val = estimate_Vals[0]
		# loop each action value to get the max one/multiple
		for x in range(len(estimate_Vals)):
			if estimate_Vals[x] > max_val:
				max_val	= estimate_Vals[x]
				max_nums = []
				max_nums.append(x)
			elif max_val == estimate_Vals[x]:
				max_nums.append(x)
		# if there are mulitple max values, randomly pick on from those actions
		pickAMax = randInRange(len(max_nums))
		this_action[0]	= max_nums[pickAMax]
		prev_action[0] = this_action[0]
		# return picked action
		return this_action
	# In epsilon situation, randomly select an action
	# print (agent_steps,"in small portion")
	this_action[0] = randInRange(len(estimate_Vals))
	prev_action[0] = this_action[0]

	
	return this_action



#  end the agent
def agent_end(reward):
	return

# clean up agent
def agent_cleanup():
	global local_action,this_action,last_observation,agent_steps,this_initVal,this_epsilon,this_alpha
	return


