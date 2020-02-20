**Description:** You want to analyze the `public` chat messages (like slack public channels) of your team and create sentiment metrics
of the different people on your team. The goal of this project is to analyze the conversations of your team
to ensure they are happy 😃.
​
You will practice in this project:
​
- API (bottle, flask)
- NLTK sentiment analysis
- Docker, Heroku and Cloud databases
- Recommender systems
​
## Project Goals
​
**Main goal**: Analyze the conversations coming from a chat like `slack`
​
- (L1��) Write an API in bottle just to store chat messages in a database like mongodb or mysql.
- (L2��) Extract sentiment from chat messages and perform a report over a whole conversation
- (L3��) Recommend friends to a user based on the contents from chat `documents` using a recommender system with `NLP` analysis.
- (L4��) Deploy the service with docker to heroku and store messages in a cloud database.
- (L5��) Do it real, use slack API to get messages and analyze the messages of our `datamad1019` channel.
  - `https://api.slack.com/`
​
## TODO's - API Endpoints
​
You have to create an api with all this endpoints:
​
### 1. User endpoints
​
- (GET) `/user/create/<username>`
  - **Purpose:** Create a user and save into DB
  - **Params:** `username` the user name
  - **Returns:** `user_id`
- (GET) `/user/<user_id>/recommend`
  - **Purpose:** Recommend friend to this user based on chat contents
  - **Returns:** json array with top 3 similar users
​
### 2. Chat endpoints:
​
- (GET) `/chat/create`
  - **Purpose:** Create a conversation to load messages
  - **Params:** An array of users ids `[user_id]`
  - **Returns:** `chat_id`
- (GET) `/chat/<chat_id>/adduser`
  - **Purpose:** Add a user to a chat, this is optional just in case you want to add more users to a chat after it's creation.
  - **Params:** `user_id`
  - **Returns:** `chat_id`
- (POST) `/chat/<chat_id>/addmessage`
  - **Purpose:** Add a message to the conversation. Help: Before adding the chat message to the database, check that the incoming user is part of this chat id. If not, raise an exception.
  - **Params:**
    - `chat_id`: Chat to store message
    - `user_id`: the user that writes the message
    - `text`: Message text
  - **Returns:** `message_id`
- (GET) `/chat/<chat_id>/list`
  - **Purpose:** Get all messages from `chat_id`
  - **Returns:** json array with all messages from this `chat_id`
- (GET) `/chat/<chat_id>/sentiment`
  - **Purpose:** Analyze messages from `chat_id`. Use `NLTK` sentiment analysis package for this task
  - **Returns:** json with all sentiments from messages in the chat
​
## Links - API dev in python
​
- [https://bottlepy.org/docs/dev/]
- [https://www.getpostman.com/]
​
## Links - NLP & Text Sentiment Analysis
​
- [https://www.nltk.org/]
- [https://towardsdatascience.com/basic-binary-sentiment-analysis-using-nltk-c94ba17ae386]
- [https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk]
​
# Links - Heroku & Docker & Cloud Databases
​
- [https://docs.docker.com/engine/reference/builder/]
- [https://runnable.com/docker/python/dockerize-your-python-application]
- [https://devcenter.heroku.com/articles/container-registry-and-runtime]
- [https://devcenter.heroku.com/categories/deploying-with-docker]
- Mongodb Atlas [https://www.mongodb.com/cloud/atlas]
- MySQL ClearDB [https://devcenter.heroku.com/articles/cleardb]
​
## Other ideas
​
- [https://www.kaggle.com/rounakbanik/movie-recommender-systems]
Collapse