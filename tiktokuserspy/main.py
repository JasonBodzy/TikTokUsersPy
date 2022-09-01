import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import traceback
import config

import pygsheets
import json

# Presets from tiktok
account_followers_xpath = config.account_followers_xpath
total_likes_xpath = config.total_likes_xpath
account_bio_xpath = config.account_bio_xpath

recent_video_xpath = config.recent_video_xpath
arrow_xpath = config.arrow_xpath
video_bio_xpath = config.video_bio_xpath
comments_xpath = config.comments_xpath
date_xpath = config.date_xpath
likes_xpath = config.likes_xpath

xbutton_xpath = config.xbutton_xpath
video_div_xpath = config.video_div_xpath
recent_views_1_xpath = config.recent_views_1_xpath


class User:
    def __init__(self, name, bio, followers, total_likes, total_videos, videos):
        self.name = name
        self.followers = followers
        self.total_likes = total_likes
        self.total_videos = total_videos
        self.videos = videos
        self.bio = bio

    def to_string(self):
        s = "Name: {0}\nFollowers: {1}\nTotal Likes: {2}\nTotal Videos: {3}\nBio: {4}\n".format(self.name,
                                                                                                self.followers,
                                                                                                self.total_likes,
                                                                                                self.total_videos,
                                                                                                self.bio)
        for i in range(len(self.videos)):
            s += ("----------Video {0}----------\n".format(i + 1))
            s += (self.videos[i].to_string())
        return s


class Video:
    def __init__(self, views, bio, comments, likes, date):
        self.views = views
        self.bio = bio
        self.comments = comments
        self.likes = likes
        self.date = date

    def to_string(self):
        return ("Bio: {0}\nDate: {1}\nViews: {2}\nLikes: {3}\nComments: {4}\n".format(self.bio, self.date, self.views,
                                                                                      self.likes, self.comments))


class TikTokScraper:
    driver = webdriver

    def scrape_user(self, name):
        try:
            PATH = "./chromedriver"
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--mute-audio")
            chrome_options.add_argument("--incognito")
            driver = webdriver.Chrome(PATH, options=chrome_options)
            driver.delete_all_cookies()
            driver.minimize_window()
            driver.get("http://tiktok.com/@" + name + "/")
            driver.minimize_window()

            followers = driver.find_element(By.XPATH, account_followers_xpath).text
            total_likes = driver.find_element(By.XPATH, total_likes_xpath).text
            recent_video_views = driver.find_element(By.XPATH, recent_views_1_xpath).text
            account_bio = driver.find_element(By.XPATH, account_bio_xpath).text
        except:
            traceback.print_exc()
            print("Error scraping user, either has 0 videos or is private account")
            driver.quit()
            return User("Error", "Error Scraping this user", 0, 0, 0, [])

        has_more_videos = True;
        number_of_videos = 0
        videos = []
        try:
            recent_video = driver.find_element(By.XPATH, recent_video_xpath)
            recent_video.click()
            number_of_videos += 1
            while has_more_videos == True:
                video_bio = driver.find_element(By.XPATH, video_bio_xpath).text
                comments = driver.find_element(By.XPATH, comments_xpath).text
                date = driver.find_element(By.XPATH, date_xpath).text
                likes = driver.find_element(By.XPATH, likes_xpath).text
                v = Video(bio=video_bio, comments=comments, date=date, likes=likes, views=0)
                videos.append(v)
                arrow = driver.find_element(By.XPATH, arrow_xpath)
                arrow.click()
                number_of_videos += 1
        except Exception:
            #traceback.print_exc()
            has_more_videos = False

        xbutton = driver.find_element(By.XPATH, xbutton_xpath)
        xbutton.click()

        video_div = driver.find_element(By.XPATH, video_div_xpath)

        views = []
        vid_strings = video_div.text.splitlines()
        for i in range(len(vid_strings)):
            if (vid_strings[i][0].isdigit()) and (
                    vid_strings[i][len(vid_strings[i]) - 1].isdigit() or vid_strings[i][
                len(vid_strings[i]) - 1] == 'M' or
                    vid_strings[i][len(vid_strings[i]) - 1] == 'K'):
                views.append(vid_strings[i])

        for i in range(len(views)):
            videos[i].views = views[i]

        driver.quit()
        user = User(name=name, followers=followers, total_likes=total_likes, total_videos=number_of_videos,
                    videos=videos,
                    bio=account_bio)
        return user


gsheets = pygsheets.authorize(service_file='./creds.json')
sheet = gsheets.open('TikTokData')
worksheet = sheet[0]
while True:
    username = (worksheet.get_value((1, 3)))
    while (username == "NULL"):
        username = (worksheet.get_value((1, 3)))
        time.sleep(0.5)

    scraper = TikTokScraper()

    user = scraper.scrape_user(username)

    #worksheet.update_value((2, 3), user.to_string())
    worksheet.update_value((2, 3), json.dumps(user, default=lambda o: o.__dict__))
    worksheet.update_value((1, 3), "NULL")

def sheet_write():

    worksheet.clear("B1", "B200")

    worksheet.update_value((2, 2), user.followers)
    worksheet.update_value((3, 2), user.total_likes)
    worksheet.update_value((4, 2), user.bio)

    for i in range(len(user.videos)):
        worksheet.update_value((6 * i + 5, 2), "Video " + str(i))
        worksheet.update_value((6 * i + 6, 2), user.videos[i].bio)
        worksheet.update_value((6 * i + 7, 2), user.videos[i].date)
        worksheet.update_value((6 * i + 8, 2), user.videos[i].views)
        worksheet.update_value((6 * i + 9, 2), user.videos[i].likes)
        worksheet.update_value((6 * i + 10, 2), user.videos[i].comments)

