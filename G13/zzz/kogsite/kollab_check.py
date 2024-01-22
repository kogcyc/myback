from collections import defaultdict

# Define the UserSession class
class UserSession:
    def __init__(self, session_id, urls):
        self.session_id = session_id
        self.urls = urls

# Create some sample user sessions
session1 = UserSession(1, ["url1", "url2", "url3"])
session2 = UserSession(2, ["url1", "url4", "url5"])
session3 = UserSession(3, ["url2", "url3", "url4"])
session4 = UserSession(4, ["url1", "url2", "url3"])
session5 = UserSession(5, ["url1", "url5", "url4"])

# Put the user sessions in a list
user_sessions = [session1, session2, session3, session4, session5]

# Create a dictionary to store the co-occurrence counts
url_counts = defaultdict(lambda: defaultdict(int))

# Iterate over the user sessions and increment the co-occurrence counts
for session in user_sessions:
    urls = session.urls
    for i in range(len(urls)):
        for j in range(i+1, len(urls)):
            url_counts[urls[i]][urls[j]] += 1
            url_counts[urls[j]][urls[i]] += 1

# Normalize the co-occurrence counts to get the URL-URL similarity scores
url_similarities = defaultdict(lambda: defaultdict(int))
for url1, related_urls in url_counts.items():
    for url2, count in related_urls.items():
        url_similarities[url1][url2] = count / float(len(user_sessions))

# Get the top 5 URLs that are most likely to appear in a session with "url1"
url1_similarities = url_similarities["url1"]
top_urls = sorted(url1_similarities, key=url1_similarities.get, reverse=True)[:5]
print("Top 5 URLs that are most likely to appear in a session with url1:", top_urls)
