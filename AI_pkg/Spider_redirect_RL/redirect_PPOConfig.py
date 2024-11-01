from Spider_RL.PPOConfig import PPOConfig

class redirect_PPOConfig:
    """
    The redirect_PPOConfig class encapsulates all configuration parameters for training a redirect PPO model
    for the spider robot. 
    This includes settings related to model creation, loading, training, and environment configuration.

    Attributes:
        LEARNING_RATE (float): The learning rate for the PPO model.
        N_STEPS (int): The number of steps to run in each environment per update.
        BATCH_SIZE (int): The mini-batch size for each gradient update.
        N_EPOCHS (int): The number of epochs for optimizing the PPO model.

        LOAD_MODEL_PATH (str): The file path for loading the PPO model.
        SAVE_MODEL_PATH (str): The file path for saving the PPO model.

        SAVE_MODEL_FREQUENCE (int): The frequency (in timesteps) at which the model is saved during training.
        TOTAL_TIME_STEPS (int): The total number of timesteps for training the PPO model. 
        RESET_REDIRECT_ANGLE_THRESHOLD (float) : The training step terminated threshold for training redirect PPO.
        REDIRECT_INIT_ANGLE (float) : The init spider toward angle for redirect training.
        
        REWARD_CAL_ANGLE_BASELINE (float): The positive and negative threshold for calculating angle reward. When the offset angle is smaller than baseline, angle_reward will be positive and vice versa.
        
        DISTANCE_REWARD_WEIGHT (float) : The weight for calculating distance reward.
        ANGLE_PENALTY_WEIGHT (float): The weight of angle reward.
        TIME_PENALTY_WEIGHT (float): The weight of time penalty.

    Note: 
        n_updates = total_timesteps // (n_steps * n_envs)
    
    """
    
    # Create PPO model
    LEARNING_RATE: float = 0.001
    N_STEPS: int = 1024
    BATCH_SIZE: int = 64
    N_EPOCHS: int = 10

    # Load PPO model
    LOAD_MODEL_PATH: str = "./redirect_Model/PPO_spider_redirect_2024-09-11.pt"
    SAVE_MODEL_PATH: str = "./redirect_Model/PPO_spider_redirect_2024-09-11.pt"
    
    # training PPO model
    SAVE_MODEL_FREQUENCE: int = 1024
    TOTAL_TIME_STEPS: int = 1024 * 128 * 256 * 8
    RESET_REDIRECT_ANGLE_THRESHOLD: float = 2.0 # degrees
    REDIRECT_INIT_ANGLE: float = PPOConfig.RESET_TOWARD_ANGLE_THRESHOLD + 5.0 # During inferencing, the redirect PPO will start with the end of toward PPO.

    # reward parameters
    REWARD_CAL_ANGLE_BASELINE: float = 15.0 # in degrees

    DISTANCE_REWARD_WEIGHT: float = 0.5 # The weight for calculating distance reward.
    ANGLE_PENALTY_WEIGHT: float = 35.0
    TIME_PENALTY_WEIGHT: float = 1.0






