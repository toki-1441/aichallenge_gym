from gym.envs.registration import register
register(
	id='aic-v0',
	entry_point='aic_gym.envs:AICEnv',
	)