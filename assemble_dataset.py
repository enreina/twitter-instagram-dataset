import json
import csv

users = []

with open("users_instagram.json") as file:
	for line in file:
		users.append(json.loads(line))

# select only users with age estimation
users = [x for x in users if 'age_profile_image_twitter' in x]

# group user by youth, young adult, and adult
for user in users:
	user['bio_length'] = len(user['description'])
	if user['age_profile_image_twitter'] <= 25:
		user['age_group'] = 'youth'
	elif user['age_profile_image_twitter'] >= 26 and user['age_profile_image_twitter'] <= 34:
		user['age_group'] = 'young adult'
	else:
		user['age_group'] = 'adult'

keys = ["statuses_count", "followers_count", "friends_count", "favourites_count", "listed_count", "bio_length", "ig_num_posts","ig_bio_length", "ig_followers", "ig_following", "ig_average_received_comments", "ig_total_received_comments", "ig_average_received_likes", "ig_total_received_likes", "age_group"]

# write to csv
with open("users.csv", "wb") as outfile:
	writer = csv.writer(outfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
	writer.writerow(keys)
	for user in users:
		writer.writerow([user[key] for key in keys])
