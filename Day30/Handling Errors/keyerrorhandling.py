facebook_posts = eval(input())

total_likes = 0
try:
    total_likes = {post['Likes'] for post in facebook_posts}
except KeyError as e:
    print(f"the key {e} does not exist")

print(total_likes)
