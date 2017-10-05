from matplotlib.patches import Circle, Rectangle, Arc
import matplotlib.pyplot as plt

def draw_pitch(ax=None, color='white', bg_color=None, lw=0.75, x_label='', y_label=''):
    pitch_width = 68.0
    pitch_length = 105.0
    goal_size = 7.32

    # if no axes is provided, set standard
    if ax is None:
        ax = plt.gca()

    penalty_area = Rectangle((0, pitch_width / 2 - 16.5 - goal_size / 2), 16.5, 40.3,
                             fill=0, edgecolor=color, linewidth=lw)

    penalty_area_r = Rectangle((pitch_length - 16.5, pitch_width / 2 - 16.5 - goal_size / 2), 16.5, 40.3,
                               fill=0, edgecolor=color, linewidth=lw)

    gk_area = Rectangle((0, pitch_width / 2 - 5.5 - goal_size / 2), 5.5, 18.32,
                        fill=0, edgecolor=color, linewidth=lw)

    gk_area_r = Rectangle((pitch_length - 5.5, pitch_width / 2 - 5.5 - goal_size / 2), 5.5, 18.32,
                          fill=0, edgecolor=color, linewidth=lw)

    penalty_circle = Arc((11, pitch_width / 2), 18.3, 18.3,
                         theta1=308, theta2=52, linewidth=lw, color=color, fill=False)

    penalty_circle_r = Arc((pitch_length - 11, pitch_width / 2), 18.3, 18.3,
                           theta1=126, theta2=234, linewidth=lw, color=color, fill=False)

    penalty_spot = Circle((11, pitch_width / 2), radius=0.25, color=color, linewidth=0)

    penalty_spot_r = Circle((pitch_length - 11, pitch_width / 2), radius=0.25, color=color, linewidth=0)

    goal = Rectangle((-0.5, pitch_width / 2 - goal_size / 2), 0.5, goal_size, facecolor=color, linewidth=lw)

    goal_r = Rectangle((pitch_length, pitch_width / 2 - goal_size / 2), 0.5,
                       goal_size, facecolor=color, linewidth=lw)

    outer_pitch = Rectangle((0, 0), pitch_length, pitch_width,
                            fill=0, edgecolor=color, linewidth=lw)
    left_side_pitch = Rectangle((0, 0), pitch_length / 2, pitch_width,
                                fill=0, edgecolor=color, linewidth=lw)

    bottom_corner = Arc((0, 0), 2, 2, theta1=0, theta2=90, linewidth=lw, color=color, fill=False)
    top_corner = Arc((0, pitch_width), 2, 2,
                     theta1=270, theta2=360, linewidth=lw, color=color, fill=False)

    bottom_corner_r = Arc((pitch_length, 0), 2, 2, theta1=90, theta2=180, linewidth=lw, color=color, fill=False)
    top_corner_r = Arc((pitch_length, pitch_width), 2, 2,
                       theta1=180, theta2=270, linewidth=lw, color=color, fill=False)

    centre_spot = Circle((pitch_length / 2, pitch_width / 2), radius=0.25, color=color, linewidth=0)

    kick_off = Circle((pitch_length / 2, pitch_width / 2),
                      radius=9.15, color=color, fill=False, linewidth=lw)

    pitch_elements = [penalty_area, penalty_area_r, gk_area, gk_area_r, goal, goal_r,
                      outer_pitch, kick_off, left_side_pitch, bottom_corner,
                      top_corner, penalty_circle, penalty_circle_r, penalty_spot,
                      penalty_spot_r, centre_spot, top_corner_r, bottom_corner_r]

    # draw all elements on the axes
    for element in pitch_elements:
        ax.add_patch(element)

    # turn of grid
    ax.grid(False)
    ax.set_facecolor(bg_color)
    ax.set(xlabel=x_label, ylabel=y_label)

