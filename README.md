

Features:

    A user can post tweets.
    A tweet can have only 140 characters.
    A tweet will have date and time of postings.
    A tweet will have user associated.
    Tweets will be fetched in descending order of posting.
    All tweets are public, everyone can see all tweets.
    A user has unique email address.
    User has a name.
    User can soft delete his tweet.
    User can update his tweet.

To run this in your local system :

Clone this repo:

```
git clone https://github.com/saurabhnk-94/twitter.git
```

Get inside the repo, type this is terminal:

```
cd twiiter
```

Create a virtual environment inside the repo:

```
python3 -m venv .venv
```

After that activate the virtual environment by typing:

```
source .venv/bin/activate
```

Next step is to install all the dependencies into your virtual environment:

```
pip3 install -r requuirement.txt
```

Next get into the project directory by typing:

```
cd Twitter
```

Type 3 commands in order before for the project to run:

```
python3 manage.py makemigrations
python3 manage.py migrate
```

Now to access the admin page before running the server create a superuser:

```
python3 manage.py createsuperuser
fill the details :
username: <ur choice>
email: <optional>
password: <password>
confirm password: <confirm the password>
```

After filling all these to run the project:

```
python3 manage.py runserver
```

For UI : Get inside the Javascript directory copy the path of home.html and paste it in the browser.


About the project:

        My project name is Twitter. My app name is twitter_app. There are 2 classes in my app-models: TweetUser and Tweet TweetUser: It has attributes user_name,email_id and is_deleted(default=false). Tweet: user as a foreign key, tweet_box for the tweet, date created, date_updated and is_deleted(default=false) The ordering will be done through the updated date and time field. Rest API is being used and in that we have used function based view. Partial output of UI is done and is running fine. UI is done using JavaScript and html and also css for styling. Summary: Language: Python - version(3.6.8) Framework: Django - version(2.2.7)

