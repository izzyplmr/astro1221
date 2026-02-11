class Observation:
    """
    A class to represent an astronomical observation.
    
    Attributes:
        target_name (str): The name of the observation target.
        filter_name (str): The name of the filter used for the observation.
    """
    
    def __init__(self, target_name, filter_name):
        """
        Initialize an Observation object.
        
        Parameters:
            target_name (str): The name of the observation target.
            filter_name (str): The name of the filter used for the observation.
        """
        self.target_name = target_name
        self.filter_name = filter_name
    
    def start_obs(self):
        """
        Print a message indicating the start of the observation.
        """
        print(f'Starting observation of {self.target_name} in {self.filter_name}')
