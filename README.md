# Password Manager

<a href="https://github.com/AyushRawal/password-manager-backend/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/AyushRawal/password-manager-backend?style=flat-square"></a> <a href="https://github.com/AyushRawal/password-manager-backend/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/AyushRawal/password-manager-backend?style=flat-square"></a> <a href="https://github.com/AyushRawal/password-manager-backend/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/AyushRawal/password-manager-backend?style=flat-square"></a> <a href="http://makeapullrequest.com"><img src="https://img.shields.io/badge/PRs-Welcome-orange?style=flat-square"></a>

<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"> <img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"> <img src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white">

The most secure way to manage passwords online (theoretically).

This is the backend of the project, a REST API written using Flask in Python.

You can use the API using this url : https://secure-passwd-manager.herokuapp.com/

### Check out the [web frontend repository](https://github.com/AyushRawal/password-manager) for the motivation behind this project.

### Also check out the CLI client [passman](https://github.com/AyushRawal/password-manager-cli), I made for this project.

## Usage 📑

The allowed methods are GET, POST, PATCH and DELETE.

A record object looks like this:

```json
{
	"id": "record-id",
	"title": "record-title",
	"password": "record-password",
	"url": "record-url",
	"notes": "record-notes"
}
```

### GET

To get the records of a user, perform a get request on https://secure-passwd-manager.herokuapp.com/user/your-user-name

This returns a json object which is an array of record objects.

```
{
    "records": [
        {
            "id": "record-id",
            "title": "record-title",
            "password": "record-password",
            "url": "record-url",
            "notes": "record-notes",
        },
        ...
    ]
}
```

### POST

Similarly, you can do a post request that takes a json object with the following fields:

- title
- password
- url (optional)
- notes (optional)

The response is a record object with the above provided values.

### PATCH

Similarly, you can do a patch request that takes a json object with the following fields:

- id
- title (optional)
- password (optional)
- url (optional)
- notes (optional)

The response is a record object with the modified value.

### DELETE

You can also do a delete request that takes a json object with `id` as its only field.
No json object is returned on delete request.

## To run this on your own machine

Clone this repository and cd into it and run :

```bash
pip install -r requirements.txt

python main.py
```

For deployment purposes check this out: https://flask.palletsprojects.com/en/2.0.x/deploying/index.html.

Also, you might want to use a database well suited for scaling. I have deployed this on heroku with Postgresql.
<img src="https://img.shields.io/badge/postgres-%23316192.svg?style=flat-square&logo=postgresql&logoColor=white">

## Support 🙏

Please drop a star ⭐ if you like this project.

_**Note :** Please feel free to ask for a feature or report any bug by opening an issue._

<br/><p align=center>Made with ❤️ for 🌏 Everyone</p>
