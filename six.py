import numpy as np

grid = np.array([
    [0, 0, 0],
    [0, 1, 0],
])
actions = ["↑", "↓", "←", "→"]
Q = np.zeros((2, 3, 4))

def q_learning(Q, grid, actions, alpha=0.1, gamma=0.9, episodes=2000):
    for episode in range(episodes):
        state = (0, 0)
        done = False
        while not done:
            action = np.argmax(Q[state])
            if np.random.random() < 0.1:
                action = np.random.randint(len(actions))
            next_state, reward, done = take_action(grid, state, actions[action])
            Q[state][action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state][action])
            state = next_state
    return np.argmax(Q, axis=2)

def take_action(grid, state, action):
    i, j = state
    if action == "↑":
        i -= 1
    elif action == "↓":
        i += 1
    elif action == "←":
        j -= 1
    elif action == "→":
        j += 1
    reward = grid[i][j] if 0 <= i < grid.shape[0] and 0 <= j < grid.shape[1] else 0
    done = (reward == 1)
    i = max(0, min(i, grid.shape[0] - 1))
    j = max(0, min(j, grid.shape[1] - 1))
    return (i, j), reward, done


policy = q_learning(Q, grid, actions)
policy=np.array([[actions[j] for j in i] for i in policy])
policy[0][2]='G'
print(policy)
