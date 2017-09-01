from environment import Env
import random

if __name__ == "__main__":
    # 환경과 에이전트 생성
    env = Env()

    for episode in range(10):
        print('episode ' + str(episode) + ' ----------------')
        done = False
        state = env.reset()

        while not done:
            # 랜덤하게 행동 선택
            action = random.choice([0, 1, 2, 3, 4])
            # 선택한 행동으로 환경에서 한 타임스텝 진행
            state, reward, done = env.step(action)

            print('state: ', state, ' action: ', action, ' reward: ', reward)

            if done:
                break
