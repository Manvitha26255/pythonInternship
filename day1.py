class Instagram:
    def __init__(self, title, description, creator_name, location):  
        self.title = title
        self.description = description
        self.creator_name = creator_name  
        self.location = location      
        self.likes = 0
        self.comments = []

    def display_title(self):
        print("The title of the reel is", self.title)

    def display_description(self):
        print("The description of the reel is", self.description)

    def display_creator(self):
        print("The creator of the reel is", self.creator_name)

    def display_location(self):
        print("The location of the reel is", self.location)
    
    def display_likes(self):
        print("The likes of the reel is", self.likes)

    def liked(self):
        self.likes += 1

    def disliked(self):
        if self.likes > 0:
            self.likes -= 1

    def display_comments(self):
        print("The comments of the reel is", self.comments)
    
    def commented(self, comment):
        self.comments.append(comment)

    def del_last_comment(self):
        if self.comments:
            self.comments.pop()
reel1 = Instagram("dancing", "dancing with friends", "abc", "bengaluru")
reel1.disliked()     
reel1.liked()        
reel1.commented("nice video")
reel2 = Instagram("finance minister conference","finance minister conference with friends","xyz", "kerala")
reel1.liked()        
reel2.liked()       
reel1.disliked()     

reel1.display_likes()
reel2.display_likes()

reel1.commented("good")
reel1.del_last_comment()

reel1.display_comments()
reel2.display_comments()

print(id(reel1))
print(id(reel2))
