# Training-Tracker

Upload images and get links to thumbnails  based on plan you have. 
3 standard plan's:
 1. Basic: <br>
    - 200px thumbnail link
 2. Premium <br>
    Basic +:
    - 400px thmubnail link
    - link to original size image
 3. Enterprise <br>
    Premium +:
    - ability to create temporary link to original image

## Setup
1. Inside main folder run following command (required docker installed)

> docker compose up

2. (optional) populate db with initial data. 
###### Warning: You this command only once when you start fresh project. It can overwrite existing objects with the same ID. 

> docker exec -it images-app python manage.py loaddata plan.json

3. (optional) create superuser

> docker exec -it images-app python manage.py createsuperuser

4. (optional) run tests

> docker exec -it images-app python manage.py test

## Stack
- Django
- DRF
- Pillow
- sorl-thumbnail
- cryptography

## Approach

### General informations

Authentication - Session authentication 

Project is written with buisness logic putted in service/selector layer, with using as simple views and serializers as it possible. Most of views use APIView class.
ImageUploadAPi uses GenericApiView just to easily upload images via browsable API.

Some validation code is putted in clean methods in models, because objects are also created via django-admin.

Some code releted to aboslute urls are also written in views.

### How images are handled

Images are public, retreving image endpoint will not raise error if user2 will use user1 image url. It will return user1 image. 
Images paths are construced with uuid library, so genrally users should not be able to guess images urls. Just keep urls secret if you do not want to share it :).
Images privacy is not a scope of the project.

Image thumbnails are handle by sorl.thumbnail libary 
After image upload it creates thmubnails with sizing defined in current user plan. Thumbnails are save in media/cache folder.
Library takes care of mapping images with thumbnails.

User can retrieve image via links listed in images lists. Endpoint get image path and size from url, and check if user has permission for retriving image with given size.
It returns 404 if any problem occures (invalid url format, invalid query params, no permission etc)

When user upgrade plan and retrieve images lists, library will create additional thumbnails if needed. It will not recreate exiting thumbnails. This action can take some time
thats why I have used pagination.

When user downgrade plan library will not delete exiting thumbnails. But user will not be able to retrieve them.

Temporary links can be created via specific endpoint by providing time in seconds for how long the link should be active. API will encrypt expiration time in url with path 
to original image and return it. View will create absolute link with encrypted part to ImagesRetrieveTempLink endpoint. It will return image if link does not expired, 
otherwise it will return 404.

If original image will be delete (via django admin) it will also delete all related thumbnails.










