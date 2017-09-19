
from rl_glue import *  # Required for RL-Glue
RLGlue("env", "agent")

import numpy as np
import sys

# save result date to local file
def saveResults(data, dataSize, filename):
	with open(filename,"w") as dataFile:
		for i in range(dataSize):
			dataFile.write("{0}\n".format(data[i]))


if __name__ == "__main__":
	numRuns = 2000
	maxStepsInRun = 1000
	result = np.zeros(maxStepsInRun)



	# loop through all the runs
	for i in range (numRuns):

		# initialization for each run
		isTerminal = False
		RL_init()
		RL_start()

		# loop through time steps
		for j in range(maxStepsInRun):
			# perform step
			rl_step_result = RL_step()
			# obtain picked action from agent
			agent_action = rl_step_result[2][0]
			# obtain default optimal action from environment
			env_actions = RL_env_message("1")

			# for debug
			# print(agent_action, env_actions[0])
			# if picked action match with env's max action,
			# add 1 to this time step
			for x in env_actions:
				if x == agent_action:
					result[j] += 1


		print ".\n",
		RL_cleanup()

	# compute the percentage optimal action based on total runs
	for i in range(maxStepsInRun):
		result[i] = result[i]/numRuns

	print ".",
	sys.stdout.flush()

	print "\nDone"

	# save result in dat file
	saveResults(result, maxStepsInRun, "RL_EXP_OUT.dat")





