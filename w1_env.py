
from utils import randn, randInRange, rand_un
import numpy as np

# create global variables
real_vals =  None
current_action = None
this_reward_observation = (None, None, None)
env_steps = None
actionNum = None
env_end = None


# initialization function used to initialize env
def env_init():
	global real_vals,env_steps,env_end,actionNum
	# number of actions used in this bandit problem
	actionNum = 10

	env_end = False
	env_steps = 0

	# create the actual value array for all bandits in this run 
	real_vals = np.zeros(actionNum)


# function to start the env before the env_step
def env_start():
	global real_vals,actionNum

	# using uniform distribution to set the initialized values for each action
	# this value won't be changed in this run 
	for x in range(0,actionNum):
		real_vals[x] = randn(0.0,1.0)


# step function to provide reward on selected actions
def env_step(this_action):
	global env_steps,env_end,real_vals
	# step plus on each time
	env_steps +=1

	# generate reward based on this action's mean and variance
	reward = randn(real_vals[this_action[0]],1.0)

	# check if this is the end the run, if end env_end is true
	if env_steps == 1001:
		env_end	 = True

	# return values
	return (reward, this_reward_observation[1], env_end)
 

# clean up environment
def env_cleanup():
	global env_steps,env_end,this_reward_observation,current_action,actionNum
	return

# meassage funciton for exp to get the actual max reward on each time step
def env_message(mMessage):
	global real_vals
	if mMessage == "1":
		max_actions=[]
		maxVal = real_vals[0]
		for x in range(len(real_vals)):
			if real_vals[x] > maxVal:
				maxVal = real_vals[x]
				max_actions = []
				max_actions.append(x)
			elif real_vals[x] == maxVal:
				max_actions.append(x)

		return max_actions








