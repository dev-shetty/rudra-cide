


# base_url = "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q=drug"


import requests, praw
from config import REDDIT_API_CLIENT, REDDIT_API_SECRET
class Search:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=REDDIT_API_CLIENT,
            client_secret=REDDIT_API_SECRET,
            user_agent='Rudra-CIDE by /u/Neat_Task4167'
        )

    def search_world(self, key, query):
        result = {}

    def search_reddit(self, subreddit, query):
        url = 'https://www.reddit.com/subreddits/search.json'
        params = {'q': query, 'limit': 100} 
        headers = {'User-Agent': 'YourBot/1.0'}
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status() 
            data = response.json()
            if 'data' in data and 'children' in data['data']:
                for child in data['data']['children']:
                    subreddit = child['data']['display_name']
                    # print(f"Found in subreddit: {subreddit}")
                    self.search_subreddit_com(subreddit, query)
        except requests.exceptions.RequestException as e:
            return {'success': True, 'message': str(e)}
        
    def search_reddit(self, subreddit, query):
        results = []
        subreddits = self.reddit.subreddit('all').search(query, limit=100)
        for submission in subreddits:
            results.append((submission.subreddit.display_name, submission.title, submission.url))
            # You can access more attributes of submission as needed
            # For example: submission.selftext for self-posts' text content
        return results
    
    def search_subreddit(self, subreddit_name, query):
        subreddit = self.reddit.subreddit(subreddit_name)
        for submission in subreddit.search(query, limit=10):
            print(f"Found in post: {submission.title} ({submission.url})")

    def search_subreddit_com(self, subreddit_name, query):
        subreddit = self.reddit.subreddit(subreddit_name)
        for submission in subreddit.search(query, limit=10):
            print(f"Found in submission: {submission.title} ({submission.url})")
            submission.comments.replace_more(limit=None)
            for comment in submission.comments.list():
                if query.lower() in comment.body.lower():
                    print(f"Found in comment: {comment.body} ({comment.permalink})")
            
    # def search_subreddit_com(self, subreddit_name, query, username):
    #     subreddit = self.reddit.subreddit(subreddit_name)
    #     for submission in subreddit.search(query, limit=10):
    #         submission.comments.replace_more(limit=None)
    #         for comment in submission.comments.list():
    #             if comment.author and comment.author.name == username:
    #                 if query.lower() in comment.body.lower():
    #                     print(f"Found in comment by {username}: {comment.body}")



# if __name__ == "__main__":
#     subreddit_name = input("Enter the string you want to search for: ")
#     query = input("Enter the string you want to search for: ")
#     # username = input("Enter the username you want to search for: ")
#     search = Search()
#     # data = search.search_reddit(subreddit_name, query)
#     data = search.search_reddit(subreddit_name, query)


