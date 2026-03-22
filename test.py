from stable_baselines3 import PPO
from env.hospital_env import HospitalEnv

env = HospitalEnv()

model = PPO.load("models/hospital_model")

obs = env.reset()

for i in range(10):
    action, _ = model.predict(obs)

    obs, reward, done, _ = env.step(action)

    print(f"Step {i+1}")
    print("State:", obs)
    print("Action:", action)
    print("Reward:", reward)
    print("----------------------")