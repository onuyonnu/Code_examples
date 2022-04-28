from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import re as re

service = Service(executable_path=ChromeDriverManager().install())


driver = webdriver.Chrome(service=service)

driver.get("https://linkedin.com/uas/login")


time.sleep(2)

username = driver.find_element(By.ID, "username")

username.send_keys("")

pword = driver.find_element(By.ID, "password")

pword.send_keys("")

driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)
driver.maximize_window()
# search = driver.find_elements_by_xpath("//input[aria-label='Search']").click()
# search.send_keys("npower canada")
# driver.get("https://www.linkedin.com/search/results/content/?keywords=npower%20canada&origin=SWITCH_SEARCH_VERTICAL&sid=P4p")
time.sleep(20)
#more_posts = driver.find_element(By.ID, "global-nav-typeahead").click()
#print(more_posts, "did it find anything?")
# time.sleep(2)
# get to Search
# search = driver.find_element(
#    By.CLASS_NAME, ("search-global-typeahead__input.always-show-placeholder")).send_keys("" + Keys.ENTER)
# time.sleep(3)
# goes to posts
# driver.find_element(
#    By.XPATH, "//*[@id='search-reusables__filters-bar']/ul/li[2]/button").click()
# time.sleep(2)
driver.get('https://www.linkedin.com/search/results/content/?origin=FACETED_SEARCH&sid=khQ&sortBy="date_posted"')
start = time.time()

# will be used in the while loop
initialScroll = 0
finalScroll = 1000

while True:
    driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")

    initialScroll = finalScroll
    finalScroll += 1000

    # we will stop the script for 3 seconds so that
    # the data can load
    time.sleep(1)
    # You can change it as per your needs and internet speed

    end = time.time()

    # We will scroll for 20 seconds.
    # You can change it as per your needs and internet speed
    if round(end - start) > 20:
        break


job_src = driver.page_source

# Now using beautiful soup
soup = BeautifulSoup(job_src.encode("utf-8"), "lxml")
soup.prettify()
containers = soup.findAll("div", {"class": "occludable-update ember-view"})


post_dates = []
post_texts = []
post_likes = []
post_comments = []
video_views = []
media_links = []
media_type = []
checks = 0
for container in containers:

    try:
        user_name_id = container.find(
            "span", {"class": 'feed-shared-actor__name t-14 t-bold hoverable-link-text t-black'})
        user_name = user_name_id.find("span", {"dir": "ltr"})
        text_box = container.find("div", {"class": "feed-shared-update-v2__description-wrapper"})
        text = text_box.find("span", {"dir": "ltr"})
        new_likes = container.findAll(
            "li", {"class": "social-details-social-counts__reactions social-details-social-counts__item"})
        new_comments = container.findAll(
            "li", {"class": "social-details-social-counts__comments social-details-social-counts__item"})
        # print(text)
        checks += 1
        temp_text = text.text.lower().strip().split()
        # print(user_name.text.strip())
        # if user_name.text.strip() not in post_dates:
        # print(temp_text)
        if "npower" in temp_text:
            post_dates.append(user_name.text.strip())
            post_texts.append(text.text.strip())
            print("Got an npower post")
        elif "jita" in temp_text:
            post_dates.append(user_name.text.strip())
            post_texts.append(text.text.strip())
            print("Got a JITA post")
        elif "#npower" in temp_text:
            post_dates.append(user_name.text.strip())
            post_texts.append(text.text.strip())
            print("Got an #Npower post")
        elif "jda" in temp_text:
            post_dates.append(user_name.text.strip())
            post_texts.append(text.text.strip())
            print("Got a JDA post")
        else:
            continue
        try:
            video_box = container.findAll(
                "div", {"class": "feed-shared-update-v2__content feed-shared-linkedin-video ember-view"})
            video_link = video_box[0].find("video", {"class": "vjs-tech"})
            media_links.append(video_link['src'])
            media_type.append("Video")
        except:
            try:
                image_box = container.findAll("div", {"class": "feed-shared-image__container"})
                image_link = image_box[0].find("img", {
                                               "class": "ivm-view-attr__img--centered feed-shared-image__image feed-shared-image__image--constrained lazy-image ember-view"})
                media_links.append(image_link['src'])
                media_type.append("Image")
            except:
                try:
                    # mutiple shared images
                    image_box = container.findAll("div", {"class": "feed-shared-image__container"})
                    image_link = image_box[0].find(
                        "img", {"class": "ivm-view-attr__img--centered feed-shared-image__image lazy-image ember-view"})
                    media_links.append(image_link['src'])
                    media_type.append("Multiple Images")
                except:
                    try:
                        article_box = container.findAll(
                            "div", {"class": "feed-shared-article__description-container"})
                        article_link = article_box[0].find('a', href=True)
                        media_links.append(article_link['href'])
                        media_type.append("Article")
                    except:
                        try:
                            video_box = container.findAll(
                                "div", {"class": "feed-shared-external-video__meta"})
                            video_link = video_box[0].find('a', href=True)
                            media_links.append(video_link['href'])
                            media_type.append("Youtube Video")
                        except:
                            try:
                                poll_box = container.findAll(
                                    "div", {"class": "feed-shared-update-v2__content overflow-hidden feed-shared-poll ember-view"})
                                media_links.append("None")
                                media_type.append("Other: Poll, Shared Post, etc")
                            except:
                                media_links.append("None")
                                media_type.append("Unknown")

        # Getting Video Views. (The folling three lines prevents class name overlap)
        view_container2 = set(container.findAll(
            "li", {'class': ["social-details-social-counts__item"]}))
        view_container1 = set(container.findAll("li", {'class': [
                              "social-details-social-counts__reactions", "social-details-social-counts__comments social-details-social-counts__item"]}))
        result = view_container2 - view_container1

        view_container = []
        for i in result:
            view_container += i

        try:
            video_views.append(view_container[1].text.strip().replace(' Views', ''))

        except:
            video_views.append('N/A')

        try:
            post_likes.append(new_likes[0].text.strip())
        except:
            post_likes.append(0)
            pass

        try:
            post_comments.append(new_comments[0].text.strip())
        except:
            post_comments.append(0)
            pass

    except:
        pass


# In[42]:


# cleaned_dates = []
# for i in post_dates:
#     d = str(i[0:3]).replace('\n\n', '').replace('•','').replace(' ', '')
#     cleaned_dates += [d]

comment_count = []
for i in post_comments:
    s = str(i).replace('comment', '').replace('s', '').replace(' ', '')
    comment_count += [s]


# In[43]:


# pd.set_option('max_colwidth', 1000)

data = {
    "User": post_dates,
    "Media Type": media_type,
    "Post Text": post_texts,
    "Post Likes": post_likes,
    "Post Comments": comment_count,
    "Video Views": video_views,
    "Media Links": media_links
}


df = pd.DataFrame(data)

df.to_csv("Npower_linkedin.csv", encoding='utf-8', index=False)
time.sleep(30)
print(f"{checks} posts checked this time.")
print(data)
