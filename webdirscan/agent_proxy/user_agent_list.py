
import random
def get_user_agent():
    user_agent_list=[
        {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77'},
        {'......'}
    ]

    return random.choice(user_agent_list)