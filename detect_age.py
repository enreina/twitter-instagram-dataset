import pickle, json
from facepp import API, File

users = []
for line in open('users_full.json'):
	users.append(json.loads(line))

# get API Key and API Secret from faceplusplus.com
API_KEY = ''
API_SECRET = ''

api = API(API_KEY, API_SECRET)

i = 1
for user in users:
	print("processing user #" + str(i) + " out of " + str(len(users)))
	i = i + 1
	try:
		res = api.detect(image_url=user['profile_image_twitter'],return_attributes='age')
		faces = res['faces'];
		if (len(faces) > 0):
			user['age_profile_image_twitter'] = faces[0]['attributes']['age']['value']
	except:
		continue
	finally:
		with open('users_full_age.json','a') as f:
			json.dump(user, f)
			f.write('\n')