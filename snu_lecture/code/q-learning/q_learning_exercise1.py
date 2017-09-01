from environment import Env
import random

if __name__ == "__main__":
    env = Env()

    for episode in range(10):
        print('episode ' + str(episode) + ' ----------------')
        env.reset()

        while True:
            env.render()
            # 랜덤하게 행동을 선택 (상, 하, 좌, 우)
            action = random.choice([0, 1, 2, 3])
            # 한 스텝 환경에서 진행
            state, reward, done = env.step(action)
            print('state: ', state, ' action: ', action, ' reward: ', reward)

            if done:
                break
