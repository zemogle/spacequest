# Space Quest website

A Django project to generate a static website, hosted as a GitHub page via [www.zemogle.net](https://www.zemogle.net).

## Deployment

Copy static files from Google Drive to Static S3 server:

```
s3cmd sync /Users/egomez/Library/CloudStorage/GoogleDrive-egomez@lco.global/Shared\ drives/Education/Space\ Quest/*.png s3://static.darkmattersheep.net/spacequest/
```

Generate static build

```
./manage.py build
```

Copy into zemogle.net project and deploy git push to Github
