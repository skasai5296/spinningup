import gym
env = gym.make('CartPole-v0')
#env = gym.make('MountainCar-v0')
#env = gym.make('MsPacman-v0')
print(env.observation_space.high)
print(env.observation_space.low)
for episode in range(10):
    observation = env.reset()
    for t in range(1000):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(
            action)  # take a random action
        if done:
            print('Episode finished after {} steps'.format(t+1))
            break
env.close()
