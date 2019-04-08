import numpy
import matplotlib.pyplot as plt
import tkinter
from tkinter import ttk

info_text = open('profile_data_3.txt', encoding='utf-8')


def regression(x, y):
    """returns the n and k"""
    n, mean_x, mean_y = len(x), numpy.mean(x), numpy.mean(y)
    k = (numpy.sum(x * y) - n * mean_x * mean_y) / (numpy.sum(x * x) - n * mean_x * mean_x)
    return mean_y - k * mean_x, k


def plot_regression_graf(x, y, x_label='', y_label='', picture_name='test'):
    """Scatters all the (x, y) points and draws linear regression line"""
    age_max = max(x)
    age_min = min(x)

    regs = regression(x, y)

    plt.plot(x, regs[0] + regs[1] * x, color='k', zorder=1)
    plt.scatter(x, y)

    plt.scatter([age_min, age_max], [regs[1] * age_min + regs[0], regs[1] * age_max + regs[0]], marker="*")

    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.savefig(picture_name)
    plt.close('all')


age = numpy.array([])
level = numpy.array([])
badges = numpy.array([])
screenshots = numpy.array([])
videos = numpy.array([])
workshop = numpy.array([])
reviews = numpy.array([])
artwork = numpy.array([])
groups = numpy.array([])
friends = numpy.array([])
games = numpy.array([])
two_week_activities = numpy.array([])
all_time_played = numpy.array([])
games_ages = numpy.array([])

for user_text in info_text:
    user = user_text.split('\t')

    age = numpy.append(age, float(user[1]))
    level = numpy.append(level, float(user[2]))
    badges = numpy.append(badges, float(user[3]))
    screenshots = numpy.append(screenshots, float(user[7]))
    videos = numpy.append(videos, float(user[8]))
    workshop = numpy.append(workshop, float(user[9]))
    reviews = numpy.append(reviews, float(user[10]))
    artwork = numpy.append(artwork, float(user[11]))
    groups = numpy.append(groups, float(user[12]))
    friends = numpy.append(friends, float(user[13]))

    if float(user[4]):
        games_ages = numpy.append(games_ages, float(user[1]))
        games = numpy.append(games, float(user[4]))
        two_week_activities = numpy.append(two_week_activities, float(user[5]))
        all_time_played = numpy.append(all_time_played, float(user[6]))

plot_regression_graf(age, level, 'Age', 'Level', 'level.png')
plot_regression_graf(age, badges, 'Age', 'Badges', 'badges.png')
plot_regression_graf(games_ages, games, 'Age', 'Games', 'games.png')
plot_regression_graf(games_ages, two_week_activities, 'Age', 'Two week activity (hours)', 'two week activity.png')
plot_regression_graf(games_ages, all_time_played, 'Age', 'All played time (hours)', 'all time played.png')
plot_regression_graf(age, screenshots, 'Age', 'Screenshots', 'screenshots.png')
plot_regression_graf(age, videos, 'Age', 'Videos', 'videos.png')
plot_regression_graf(age, reviews, 'Age', 'Reviews', 'reviews.png')
plot_regression_graf(age, workshop, 'Age', 'Workshop', 'workshop.png')
plot_regression_graf(age, artwork, 'Age', 'Artwork', 'artwork.png')
plot_regression_graf(age, groups, 'Age', 'Groups', 'groups.png')
plot_regression_graf(age, friends, 'Age', 'Friends', 'friends.png')


def display_estimated_data():
    """Executes when age is inserted and calculates all estimates"""
    input_age = float(inserted_age.get())

    level_regs = regression(age, level)
    estimated_level = level_regs[1] * input_age + level_regs[0]
    level_label.config(text='Level: {0}'.format(round(estimated_level)))

    badge_regs = regression(age, badges)
    estimated_badges = badge_regs[1] * input_age + badge_regs[0]
    badges_label.config(text='Badges: {0}'.format(round(estimated_badges)))

    games_regs = regression(games_ages, games)
    estimated_games = games_regs[1] * input_age + games_regs[0]
    games_label.config(text='Games: {0}'.format(round(estimated_games)))

    two_week_activities_regs = regression(games_ages, two_week_activities)
    estimated_activity = two_week_activities_regs[1] * input_age + two_week_activities_regs[0]
    two_week_activities_label.config(text='2 week activity: {0}'.format(round(estimated_activity)))

    all_time_played_regs = regression(games_ages, all_time_played)
    estimated_all_time_played = all_time_played_regs[1] * input_age + all_time_played_regs[0]
    all_time_played_label.config(text='All played time: {0}'.format(round(estimated_all_time_played)))

    screenshots_regs = regression(age, screenshots)
    estimated_screenshots = screenshots_regs[1] * input_age + screenshots_regs[0]
    screenshots_label.config(text='Screenshots: {0}'.format(round(estimated_screenshots)))

    videos_regs = regression(age, videos)
    estimated_videos = videos_regs[1] * input_age + videos_regs[0]
    videos_label.config(text='Videos: {0}'.format(round(estimated_videos)))

    workshop_regs = regression(age, workshop)
    estimated_workshop = workshop_regs[1] * input_age + workshop_regs[0]
    workshop_label.config(text='Workshops: {0}'.format(round(estimated_workshop)))

    reviews_regs = regression(age, reviews)
    estimated_reviews = reviews_regs[1] * input_age + reviews_regs[0]
    reviews_label.config(text='Reviews: {0}'.format(round(estimated_reviews)))

    artwork_regs = regression(age, artwork)
    estimated_artworks = artwork_regs[1] * input_age + artwork_regs[0]
    artwork_label.config(text='Artworks: {0}'.format(round(estimated_artworks)))

    group_regs = regression(age, groups)
    estimated_groups = group_regs[1] * input_age + group_regs[0]
    groups_label.config(text='Groups: {0}'.format(round(estimated_groups)))

    friends_regs = regression(age, friends)
    estimated_friends = friends_regs[1] * input_age + friends_regs[0]
    friends_label.config(text='Friends: {0}'.format(round(estimated_friends)))


def change_picture(event):
    """Happens when combobox is changes and displays the correct picture"""
    data_type = change_picute_button.get()
    picture.config(file='{0}.png'.format(data_type))


root = tkinter.Tk()

root.option_add("*TCombobox*Listbox*Font", 13)

canvas = tkinter.Canvas(root, width=700, height=500)
canvas.grid(row=1, column=1)

frame_of_data = tkinter.Frame(root)
frame_of_data.grid(row=1, column=0)

question = tkinter.Label(frame_of_data, text='Insert profile age in years (float)', font=13)
question.pack()

inserted_age = tkinter.StringVar()
entry = tkinter.Entry(frame_of_data, textvariable=inserted_age)
entry.pack()

button = tkinter.Button(frame_of_data, text='Generate', command=display_estimated_data, font=13)
button.pack()

level_label = tkinter.Label(frame_of_data, text='Level:', font=13, pady=5)
level_label.pack()

badges_label = tkinter.Label(frame_of_data, text='Badges:', font=13, pady=5)
badges_label.pack()

games_label = tkinter.Label(frame_of_data, text='Games:', font=13, pady=5)
games_label.pack()

two_week_activities_label = tkinter.Label(frame_of_data, text='2 week activity:', font=13, pady=5)
two_week_activities_label.pack()

all_time_played_label = tkinter.Label(frame_of_data, text='All played time:', font=13, pady=5)
all_time_played_label.pack()

screenshots_label = tkinter.Label(frame_of_data, text='Screenshots:', font=13, pady=5)
screenshots_label.pack()

videos_label = tkinter.Label(frame_of_data, text='Videos:', font=13, pady=5)
videos_label.pack()

reviews_label = tkinter.Label(frame_of_data, text='Reviews:', font=13, pady=5)
reviews_label.pack()

workshop_label = tkinter.Label(frame_of_data, text='Workshop:', font=13, pady=5)
workshop_label.pack()

artwork_label = tkinter.Label(frame_of_data, text='Artworks:', font=13, pady=5)
artwork_label.pack()

groups_label = tkinter.Label(frame_of_data, text='Groups:', font=13, pady=5)
groups_label.pack()

friends_label = tkinter.Label(frame_of_data, text='Friends:', font=13, pady=5)
friends_label.pack()

change_picute_button = ttk.Combobox(root, values=['level', 'badges', 'games', 'two week activity', 'all time played',
                                                  'screenshots', 'videos', 'reviews', 'workshop', 'artwork', 'groups',
                                                  'friends'], font=13)
change_picute_button.grid(row=0, column=1, pady=(5, 5), sticky='w')
change_picute_button.bind("<<ComboboxSelected>>", change_picture)

picture = tkinter.PhotoImage(file='basic_picture.png', master=root)
canvas.create_image(0, 0, anchor='nw', image=picture)

root.mainloop()




