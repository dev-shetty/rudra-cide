
import string, praw, time
from config import REDDIT_API_CLIENT, REDDIT_API_SECRET

class Alias:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=REDDIT_API_CLIENT,
            client_secret=REDDIT_API_SECRET,
            user_agent='Rudra-CIDE by /u/Neat_Task4167'
        )
        self.found = {}

    async def check_reddit(self, key, user: str):
        alphabets = string.ascii_lowercase+string.digits
        self.found[user] = []
        users = []
        try:
            redditor = self.reddit.redditor(user)
            users.append(user)
        except Exception as e:
            pass
        for char in alphabets:
            username = f"{user}{char}"
            try:
                redditor = self.reddit.redditor(username)
                users.append(username)
            except Exception as e:
                pass
        for user in users:
            data = await self.check_reddit_data(user, key)
            print(data)
            time.sleep(1)
            if data['success']:
                self.found[user].append(data['data'])
        return self.found
    
    async def check_reddit_data(self, username, key):
        try:
            posts = self.reddit.redditor(username).submissions.new(limit=None)
            data = {}
            data['username'] = username
            data['posts'] = []
            data['comments'] = []
            for post in posts:
                if key in post.selftext:
                    post_data = {
                        'title': post.title,
                        'url': post.url,
                        'text': post.selftext
                    }
                    data['posts'].append(post_data)
            comments = self.reddit.redditor(username).comments.new(limit=None)
            for comment in comments:
                if key in comment.body:
                    comment_data = {
                        'url': comment.submission.url,
                        'text': comment.body
                    }
                    data['comments'].append(comment_data)
            return {'success': True,  'data': data}
        except Exception as e:
            return {'success': False }


alias = Alias()
# print(alias.check_reddit('Lonely_Spell9563', 'buy'))
print(alias.check_reddit_data('Lonely_Spell9563', 'buy'))


