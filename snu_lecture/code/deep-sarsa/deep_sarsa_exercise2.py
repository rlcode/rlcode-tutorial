import random
import numpy as np
from environment import Env
from keras.layers import Dense
from keras.optimizers import Adam
from keras.models import Sequential

EPISODES = 1000


# 그리드월드 예제에서의 딥살사 에이전트
class DeepSARSAgent:
    def __init__(self):
        # 에이전트가 가능한 모든 행동 정의
        self.action_space = [0, 1, 2, 3, 4]
        # 상태의 크기와 행동의 크기 정의
        self.action_size = len(self.action_space)
        self.state_size = 15
        self.discount_factor = 0.99
        self.learning_rate = 0.001

        # 탐험 관련
        self.epsilon = 1.
        self.epsilon_decay = .9999
        self.epsilon_min = 0.01

        # 모델 생성

    # 상태가 입력 큐함수가 출력인 인공신경망 생성
    def build_model(self):
        pass

    # 입실론 탐욕 방법으로 행동 선택
    def get_action(self, state):
        pass

    def train_model(self, state, action, reward, next_state, next_action, done):
        state = np.float32(state)
        next_state = np.float32(next_state)

        # 살사의 큐함수 업데이트 식

        # 출력 값 reshape

        # 인공신경망 업데이트


if __name__ == "__main__":
    # 환경과 에이전트 생성
    env = Env()
    agent = DeepSARSAgent()

    global_step = 0
    scores, episodes = [], []

    for e in range(EPISODES):
        done = False
        score = 0
        state = env.reset()
        state = np.reshape(state, [1, 15])

        while not done:
            # env 초기화
            global_step += 1
            if agent.epsilon > agent.epsilon_min:
                agent.epsilon *= agent.epsilon_decay

            # 현재 상태에 대한 행동 선택

            # 선택한 행동으로 환경에서 한 타임스텝 진행 후 샘플 수집

            # 샘플로 모델 학습

            if done:
                # 에피소드마다 학습 결과 출력
                break

        # 100 에피소드마다 모델 저장
