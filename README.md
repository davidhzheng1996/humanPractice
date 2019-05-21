# humanPractice
In order to launch the site, please do the following in your terminal.
1. git clone git@github.com:davidhzheng1996/humanPractice.git
2. pip3 install -r requirements.txt
3. python3 manage.py runserver
4. Then go to your browser Type localhost:8000 in your browser

The website contains 2 main pages, one that contains an interface for uploading .txt files in order to start the word frequency analysis. The other page contains the 10 most recent frequency analysis, where the user can see the stop-word settings, original text, time stamp as well as the word frequencies. The stopword libraries used is from nltk.corpus.

Viewsets.py were where most of the backend apis were implemented while views.py were used to create urls for different page views. Furthermore, models.py were where the database was initialized while serializers.py were used to validate the incoming data that would be saved to the psql database.

