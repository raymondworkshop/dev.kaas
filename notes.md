
#### notes 
* TODO

* staging   -> production  
    - > git commit -m "update" .
      > git push staging master  

      > heroku config:set --remote staging \
        SECRET_KEY=the-staging-key \
        APP_SETTINGS=config.StagingConfig  

    - promote the new to production with different configuration  
      > heroku config:set --remote prod \
        SECRET_KEY=the-production-key \
        APP_SETTINGS=config.ProductionConfig 

      > heroku pipelines:promote --remote staging

#### reference 
* [Deploying a Python Flask Example Application Using Heroku](https://realpython.com/flask-by-example-part-1-project-setup/#deploying-the-application-to-heroku)