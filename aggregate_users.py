import pickle, json, os

files = os.listdir('./output_chunks')
keys = ["id","name","screen_name","description","followers_count","friends_count","listed_count","favourites_count","statuses_count","created_at"]

for file in files:
	results = pickle.load(open('./output_chunks/' + file))

	users = []
	for result in results:
		if "Instagram" in result.source:
			user = {}
			user["instagram_url"] = result.urls[0].expanded_url
			user['profile_image_twitter'] = result.user.profile_image_url.replace("_normal", "")
			for key in keys:
				user[key] = getattr(result.user, key)
			users.append(user)

	for user in users:
		with open('users_full.json','a') as f:
			json.dump(user, f)
			f.write('\n')

	print(file + " ...done!")