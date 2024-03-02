
import string, praw


API_SECRET = "ebzQ-2SQfmdtpetKI6mvHGxdRdnZ7w"
API_CLIENT = "uncXIpkUVmB1BAJopPcKWQ"

class Alias:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=API_CLIENT,
            client_secret=API_SECRET,
            user_agent='Rudra-CIDE by /u/Neat_Task4167'
        )
        self.found = {}

    def check_redit(self, key, user: str):
        alphabets = string.ascii_lowercase+string.digits
        self.found[user] = []
        for char in alphabets:
            username = f"{user}{char}"
            try:
                redditor = self.reddit.redditor(username)
                data = self.track_user_activity(key, user)
                if not data.success:
                    self.found[user].append(username)
            except Exception as e:
                pass
        return self.found

    def track_user_activity(self, key, user: str):
        try:
            results = []
            user = self.reddit.redditor(user)
            # Fetch user's submissions
            for submission in user.submissions.new():
                if key.lower() in submission.title.lower() or key.lower() in submission.selftext.lower():
                    results.append((submission.title, submission.url, submission.author.name))
            # Fetch user's comments
            for comment in user.comments.new():
                if key.lower() in comment.body.lower():
                    results.append((comment.body, comment.permalink, comment.author.name))
            return {'success': True, 'data': results}
        except Exception:
            return {'success': False}



alias = Alias()

print(alias.check_redit("Hi", "rudra"))