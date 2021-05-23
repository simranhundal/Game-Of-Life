import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# specified grid size
gridsize = 75
gs = gridsize
# fill grid with random initial values with 10% to be on 90% off
vals = [1, 0]
grid = np.random.choice(vals, gs * gs, p=[.1, .9]).reshape(gs, gs)


# function to update board
def update(frame, img, board):
    # get copy of board
    newboard = board.copy()
    for i in range(gs):
        for j in range(gs):
            # count total neighbor using periodic boundary conditions
            total = (board[i, (j - 1) % gs] + board[i, (j + 1) % gs] +
                     board[(i - 1) % gs, j] + board[(i + 1) % gs, j] +
                     board[(i - 1) % gs, (j - 1) % gs] + board[(i - 1) % gs, (j + 1) % gs] +
                     board[(i + 1) % gs, (j - 1) % gs] + board[(i + 1) % gs, (j + 1) % gs])
            # apply conways rules
            if board[i, j] == 1:
                if (total < 2) or (total > 3):
                    newboard[i, j] = 0
            else:
                if total == 3:
                    newboard[i, j] = 1
    # update parameters for animation
    img.set_data(newboard)
    board[:] = newboard[:]
    return img


# create figure
fig, ax = plt.subplots()
ax.set_title("Conway's Game of Life")

img = ax.imshow(grid, cmap='binary')
# create animation by calling update function
ani = animation.FuncAnimation(fig, update, fargs=(img, grid),
                              frames=10,
                              interval=100,
                              save_count=50)

plt.show()
