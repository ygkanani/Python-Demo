import requests
from bs4 import BeautifulSoup

# make request to get website data from URL
res = requests.get('https://news.ycombinator.com/news')

# parse response with BeautifulSoup
soup = BeautifulSoup(res.text, 'html.parser')

# get all story links
links = soup.select('.titlelink')

# get subtext of links
subtext = soup.select('.subtext')


def sort_stories_by_votes(hnlist):
    # return sorted news list by vote count in reverse order
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []

    # iterate through links using enumerate to generate index
    for idx, item in enumerate(links):
        # get news title text
        title = item.getText()

        # get news URL
        href = item.get('href', None)

        # get vote count for news
        vote = subtext[idx].select('.score')

        # if vote count for news is found
        if len(vote):
            # convert vote count text to integer
            points = int(vote[0].getText().replace(' points', ''))
            # if vote count for news is greater than 99, append news in list
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


print(create_custom_hn(links, subtext))
