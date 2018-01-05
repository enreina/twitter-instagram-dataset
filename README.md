# twitter-instagram-dataset
Scripts to build dataset of users from both Instagram and Twitter

## Requirements
1. Python & PHP (we used Python 2.7 and PHP 5.6)
2. [instagram-php-scraper](https://github.com/postaddictme/instagram-php-scraper)

	It is already required in the `composer.json` file, so all you have to do is
    ```
    composer install
    ```
    
2. [python-twitter](https://github.com/bear/python-twitter)
  
    To install using pip:
    ```
    pip install python-twitter
    ``` 
  
3. [FacePlusPlus Python SDK](https://github.com/FacePlusPlus/facepp-python-sdk)

	Place the `facepp.py` in the same folder

## How to use the scripts
1. Go to [http://apps.twitter.com](http://apps.twitter.com) and create an app to obtain consumer key, consumer secret, access token, and access_token_secret. Fill these four values in `search.py`
2. Run the following lines in a sequential order in your Terminal or Command Prompt
```
python search.py
python aggregate_users.py
python detect_age.py
php getMediaByUrl.php
python assemble_dataset.py
```

  Each line can be stopped when you already have enough processed data. The output(s) that are important are:
  * `users_instagram.json`: raw data in JSON format
  * `users.csv`: processed data in CSV (only contains features which are mentioned in the paper)

## Direct Download of Dataset
Because the dataset contains privacy sensitive information of users, if you would like to request the full dataset file, please send an email to [e.a.rizkiasri@student.tudelft.nl](mailto:e.a.rizkiasri@student.tudelft.nl) stating your purpose of using the dataset.
