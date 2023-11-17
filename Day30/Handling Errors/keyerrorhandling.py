facebook_posts = eval(input())

total_likes = 0
for post in facebook_posts:
    try:
        total_likes += post['Likes']
    except KeyError as e:
        print(f"the key {e} does not exist")

print(total_likes)
