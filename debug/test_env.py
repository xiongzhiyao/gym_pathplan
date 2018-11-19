import gym
import time

env = gym.make('PathHallway-v0')

# test
#for i in range (100):
env.reset()
for _ in range(1000):
	env.reset()
	done = False
	while not done:
		env.render()
		obs, r, done, _ = env.step(env.action_space.sample())
		# print ("reward:", r)
		# print ("obs:", obs)
