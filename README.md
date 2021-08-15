# Django + React Full-Stack Project

Based on the tutorial [How To Build a To-Do application Using Django and React](https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react) at DigitalOcean.

## Prerequisites

This project is built in a an environment with the following specifications:

- Linux Mint 20.1 Ulyssa (base: Ubuntu 20.04 focal)
- Python 3.8.10
- Django 3.2.5
- Node.js 14.17.4
- NPM 6.14.14
- Create React App 4.0.3
- Yarn 1.22.5

## Deployment in Heroku

Read this tutorial: https://devcenter.heroku.com/articles/git

### Create a new Heroku app

```console
heroku create django-react-integration
```

### Add the Heroku remote

```console
heroku git:remote -a django-react-integration
```

### Configure the Heroku buildpacks

```console
heroku buildpacks:add --index 1 heroku/nodejs
heroku buildpacks:add --index 2 heroku/python
```

Note that the buildpacks must be added in that order.
We can see the buildpacks we’ve added by running `heroku buildpacks`.

### Configure PostgreSQL Heroku addon

During production, Heroku will not be using SQLite database. Instead, we need to use PostgreSQL by configuring the addon to our app:

```console
heroku addons:create heroku-postgresql:hobby-dev
```

You can check whether this is successful by running `heroku config`.

### Configure Heroku config variables

heroku config:set ALLOWED_HOSTS=APP_NAME.herokuapp.com
heroku config:set ALLOWED_HOSTS=APP_NAME.herokuapp.com
heroku config:set SECRET_KEY=DJANGO_SECRET_KEY
heroku config:set WEB_CONCURRENCY=1

### Modify Django and React files for Production


### Commit and Push


```console
git push heroku master
```