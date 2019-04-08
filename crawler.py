import requests
import re
import random
import time

KEY = '11F02A5A2959FEE92ACA1BA3E39AC8CB'

zakhrayseh_id = '76561198064053593'

profile_url = 'https://steamcommunity.com/profiles/'


class User:
    def __init__(self, user_id):
        self._user_id = user_id
        self._is_private = False
        dict_data = self.get_data(user_id)

        if not self._is_private:
            self._username, self._age = self.get_name_and_time(user_id)
            self._level = dict_data.get('Level', 0)
            self._badges = dict_data.get('Badges', 0)
            self._games, self._2_week_activity, self._time_played = self.get_owned_games(user_id)
            self._screenshots = dict_data.get('Screenshots', 0)
            self._videos = dict_data.get('Videos', 0)
            self._workshop = dict_data.get('Workshop', 0)
            self._reviews = dict_data.get('Reviews', 0)
            self._artwork = dict_data.get('Artowork', 0)
            self._groups = dict_data.get('Groups', 0)
            self._friends = dict_data.get('Friends', 0)
            self._all_friend_ids = dict_data.get('All_friend_ids', 0)

    def __str__(self):
        """Returns a readable string"""
        if self._is_private:
            return 'Private profile ' + self._user_id
        return '\t'.join(map(str, [self._username, self._age, self._level, self._badges, self._games, self._2_week_activity,
                           self._time_played, self._screenshots, self._videos, self._workshop, self._reviews,
                           self._artwork, self._groups, self._friends]))

    def __repr__(self):
        """"""
        return 'User('

    @staticmethod
    def get_name_and_time(user_id):
        """retuns name and time of user_id"""
        get_player_summaries = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={0}&steamids={1}".format(
            KEY, user_id)
        data = eval(requests.get(get_player_summaries).text)["response"]["players"][0]
        name = data['personaname']
        age = (time.time() - data["timecreated"]) / 3600 / 24 / 365

        return name, age

    def get_data(self, user_id):
        """Gets data from a user id, data:{level, badge, screenshots, videos, workshop, reviews, artwork, groups,
        friends}
        """
        data_dict = dict()
        page = requests.get(profile_url + user_id).text
        updated_page = page.replace('\n', '').replace('\r', '').replace('\t', '')
        if re.findall('This profile is private|This user has not yet set up their Steam Community', updated_page):
            self._is_private = True
            return data_dict
        level = re.findall('class="friendPlayerLevelNum">.*</span>', updated_page)
        if not level:
            self._is_private = True
            return data_dict
        extracted_level = re.sub('<.*>', '', re.sub('c.*?>', '', level[0]))
        data_dict['Level'] = extracted_level

        marks = {'Badges', 'Reviews', 'Groups', 'Friends', 'Artwork', 'Screenshots', 'Videos', 'Workshop'}

        find = '<span class="count_link_label">.*?</span>&nbsp;<span class="profile_count_link_total">.*?</span>'
        info = re.findall(find, updated_page)

        for data in info:
            extracted_data = re.sub('&nbsp;', ' ', re.sub('<.*?>', '', data))
            separated_data = extracted_data.split(' ')
            if separated_data[0] in marks:
                data_dict[separated_data[0]] = int(separated_data[-1].replace(',', ''))

        friends_link = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={0}&steamid={1}&relationship=friend'.format(
            KEY, user_id)
        friends_dict = eval(requests.get(friends_link).text)
        if not friends_dict:
            self._is_private = True
            return
        friends_data = friends_dict.get('friendslist')
        all_friends = [friends_id.get('steamid') for friends_id in friends_data['friends']]
        data_dict['All_friend_ids'] = all_friends

        return data_dict

    @staticmethod
    def get_owned_games(user_id):
        """Gets data for user_id games and played time for 2 week and all time"""
        games_link = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={0}&steamid={1}&format=json'.format(
            KEY, user_id)
        hours_played_page = eval(requests.get(games_link).text)['response']
        if hours_played_page:
            games = hours_played_page.get('game_count')
            hours_played = sum([game.get('playtime_forever', 0) / 60 for game in hours_played_page['games']])
            two_week_played = sum(game.get('playtime_2weeks', 0) / 60 for game in hours_played_page['games'])
            return games, round(two_week_played), round(hours_played)
        return 0, 0, 0

    def choose_friend(self):
        """Randomly chooses one friend"""
        return self._all_friend_ids[random.randint(0, len(self._all_friend_ids) - 1)]

    def has_no_friends(self):
        """Returns true if profile is private"""
        return self._is_private or not bool(self._all_friend_ids)

profile = User(zakhrayseh_id)
previous_profile = User(zakhrayseh_id)

for_write = open('profile_data.txt', 'w', encoding='utf-8')

for _ in range(100):
    if profile.has_no_friends():
        next_friend = previous_profile.choose_friend()
        profile = User(next_friend)
        if not profile.has_no_friends():
            print(profile, file=for_write)
    else:
        next_friend = profile.choose_friend()
        previous_profile = profile
        profile = User(next_friend)
        if not profile.has_no_friends():
            print(profile, file=for_write)
    print(_)

