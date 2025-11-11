from django.db import models

class userProfile(models.Model):
    username = models.CharField(max_length=30, unique=True)
    mail = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.username
    

class tweet(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=280)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(userProfile, on_delete=models.CASCADE, related_name='tweets')
    
    def __str__(self):
        return f"{self.author.username}: {self.content[:50]}"
    

class comment(models.Model):
    content = models.CharField(max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(userProfile, on_delete=models.CASCADE, related_name='comments')
    tweet = models.ForeignKey(tweet, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return f"Comment by {self.author.username} on {self.tweet.id}"
    
    