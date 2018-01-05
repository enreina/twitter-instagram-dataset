<?php
require __DIR__ . '/vendor/autoload.php';
// If account is public you can query Instagram without auth
$instagram = new \InstagramScraper\Instagram();
// If account is private and you subscribed to it firstly login
// $instagram = \InstagramScraper\Instagram::withCredentials('username', 'password', '/path/to/cache/folder');
// $instagram->login();

$handle = fopen("users_full_age.json", "r");
if ($handle) {
	$i = 0;
    while (($line = fgets($handle)) !== false) {
        // process the line read.

        $user = json_decode($line, true);
        $instagram_url = $user['instagram_url'];
        try {
	        $media = $instagram->getMediaByUrl($instagram_url);
	        $account = $media->getOwner();
			$account = $instagram->getAccount($account->getUsername());
			if ($account->isPrivate()) {
				continue;
			}
			$user['ig_username'] = $account->getUsername();
	        $user['ig_num_posts'] = $account->getMediaCount();
	        $user['ig_bio'] = $account->getBiography();
	        $user['ig_bio_length'] = strlen($user['ig_bio']);
	        $user['ig_followers'] = $account->getFollowedByCount();
	        $user['ig_following'] = $account->getFollowsCount();

	        $medias = $instagram->getMedias($user['ig_username']);
	        
	        $comments_count = 0;
	        $likes_count = 0;
	       	foreach ($medias as $media) {
	       		$comments_count += $media->getCommentsCount();
	       		$likes_count += $media->getLikesCount();
	       	}

	       	$user['ig_total_received_likes'] = $likes_count;
	       	$user['ig_total_received_comments'] = $comments_count;
	       	$user['ig_average_received_likes'] = $likes_count / count($medias);
	       	$user['ig_average_received_comments'] = $comments_count / count($medias);

	        file_put_contents("users_instagram.json", json_encode($user)."\n", FILE_APPEND);
	        echo "Processed $i users..\n";

        	$i++;
    	} catch(Exception $e) {
    		continue;
    	}
    }

    fclose($handle);
} else {
    // error opening the file.
} 

