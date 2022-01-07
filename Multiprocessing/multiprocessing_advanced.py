import os
import gym
import torch.multiprocessing as mp

os.environ['OMP_NUM_THREADS'] = '1'

class ParallelEnv:
    def __init__(self, env_id, num_threads):
        names = [str(i) for i in range(num_threads)]

        self.ps = [mp.Process(target=worker, args=(name, env_id)) for name in names]
        [p.start() for p in self.ps]
        [p.join() for p in self.ps]

def worker(name, env_id):
    env = gym.make(env_id)
    episode, max_eps, scores = 0, 10, []
    while episode < max_eps:
        obs = env.reset()
        score, done = 0, False
        while not done:
            action = env.action_space.sample()
            new_obs, reward, done, info = env.step(action)
            score += reward
            obs = new_obs
        scores.append(score)
        print('Episode {} process {} score {:.2f}'.format(episode, name, score))
        episode += 1


if __name__ == '__main__':
    mp.set_start_method('spawn')
    env_id = 'CartPole-v0'
    n_threads = 4
    env = ParallelEnv(env_id, n_threads)
