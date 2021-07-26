# Password Manager


The most secure online password manager (theoretically).

I have always struggled with my passwords. I use capital letters, numbers, special symbols in my passwords and keep them unrelated to myself for maximum security and peace of mind, but that also makes them hard to remember, especially when there are so many of them.

Sure, I could use any of the password managers available out there, but cyber attacks on those are not a rare sight.

So, I built this project.

The best way to store passwords of multiple users, I thought, was to hash them using their master password.

But, this approach has a few disadvantages too.

If a user forgets his/her master password, he/she loses all the passwords, i.e., there can be no "Forgot Password" feature.

To help with that, I am using [Shamir's Secret Sharing](https://en.wikipedia.org/wiki/Secret_sharing#Shamir's_scheme) algorithm.

Whenever a new user logs in, he/she is presented with some keys that can be stored somewhere safe and can be used to retrieve the master password.


This is the backend of the project.

The web frontend repository : [password-manager-web-frontend](github.com/AyushRawal/password-manager-web-frontend).


It is a REST API written using Flask in Python.


## Installation

Clone this repository and and cd into it and run :

```bash
pip install -r requirements.txt
```

For deployment purposes, please make sure that debug is set to false.
