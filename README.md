Nespresso Coffee Machine Store
---

### Introduction

Nespresso Coffee Machine Store API is a simple project that listing coffee machines and pods with the following functionality:

  - User can list all coffee machines with custom filters 
  - User can list all coffee pods with custom filters

### Technologies

Nespresso Coffee Machine uses a number of open source projects to work properly:

* [Python](https://www.python.org) - is a class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible.
* [Pip](https://pypi.org/project/pip/) - is a package-management system written in Python used to install and manage software packages.
* [Django](https://www.djangoproject.com/) - Django is a Python-based free and open-source web framework that follows the model-template-views architectural pattern.
* [Restful APIs](https://restfulapi.net/) - is architectural style for distributed hypermedia systems.
* [Postgresql](https://www.postgresql.org/) -  is a powerful, open source object-relational database system.
* [Docker](https://www.docker.com/) - is a set of platform as a service (PaaS) products that use OS-level virtualization.
* [Docker Compose](https://docs.docker.com/compose/) - is a tool for running multi-container applications on Docker.

And of course Nespresso Coffee Machine Store itself is open source with a [public repository](https://github.com/FadyAlfred/ncoffemachine)
 on GitHub.

### Install and run

```sh
$ Clone the repository
$ Go into the project folder and exec docker-compose up --build
$ The app should be up and running on localhost:8000
```

### Admin dashboard

```sh
$ Open http://127.0.0.1:8000/admin on yor browser
$ Login using the following credentials {username: admin, password: admin}
$ All CURD operation on coffee machines or pods can be done throw this dashboard
```

### Demo Data

Once you run the project the data below would be inserted to the database
```
· CM001 – small machine, base model
· CM002 – small machine, premium model
· CM003 – small machine, deluxe model, water line compatible
· CM101 – large machine, base model
· CM102 – large machine, premium model, water line compatible
· CM103 – large machine, deluxe model, water line compatible
· EM001 – espresso machine, base model
· EM002 – espresso machine, premium model
· EM003 – espresso machine, deluxe model, water line compatible
· CP001 – small coffee pod, 1 dozen, vanilla
· CP003 – small coffee pod, 3 dozen, vanilla
· CP011 – small coffee pod, 1 dozen, caramel
· CP013 – small coffee pod, 3 dozen, caramel
· CP021 – small coffee pod, 1 dozen, psl
· CP023 – small coffee pod, 3 dozen, psl
· CP031 – small coffee pod, 1 dozen, mocha
· CP033 – small coffee pod, 3 dozen, mocha
· CP041 – small coffee pod, 1 dozen, hazelnut
· CP043 – small coffee pod, 3 dozen, hazelnut
· CP101 – large coffee pod, 1 dozen, vanilla
· CP103 – large coffee pod, 3 dozen, vanilla
· CP111 – large coffee pod, 1 dozen, caramel
· CP113 – large coffee pod, 3 dozen, caramel
· CP121 – large coffee pod, 1 dozen, psl
· CP123 – large coffee pod, 3 dozen, psl
· CP131 – large coffee pod, 1 dozen, mocha
· CP133 – large coffee pod, 3 dozen, mocha
· CP141 – large coffee pod, 1 dozen, hazelnut
· CP143 – large coffee pod, 3 dozen, hazelnut
· EP003 – espresso pod, 3 dozen, vanilla
· EP005 – espresso pod, 5 dozen, vanilla
· EP007 – espresso pod, 7 dozen, vanilla
· EP013 – espresso pod, 3 dozen, caramel
· EP015 – espresso pod, 5 dozen, caramel
· EP017 – espresso pod, 7 dozen, caramel
```


### Sample request flow
- Get list of the coffee machines with filters and pagination
```sh
Request
GET 
'http://127.0.0.1:8000/store/machines/?type=E&water_line_compatible=true&edation='
```
```
Allowed Query Params:
    type -> {L: Large Machine, S: Small Machine, E: Espresso Machine}
    water_line_compatible -> [true, false]
    edition -> {B: Base Model, P: Permium Model, D: Deluxe Model}
    page -> page number
    page_size -> page size
```
```
Response: success
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 9,
            "sku": "EM003",
            "water_line_compatible": true,
            "type": "E",
            "edition": "D"
        }
    ]
}
```

- Get list of the coffee pods with filters and pagination
```sh
Request
GET 
'http://127.0.0.1:8000/store/pods/?type=&flavor=V&size=7'
```
```
Allowed Query Params:
    type -> {L: Large Machine, S: Small Machine, E: Espresso Machine}
    flavor -> {V: Vanilla, C: Carmel, P: Psl, M: Mocha, H: Hazelnut}
    size -> [1, 3, 5, 7]
    page -> page number
    page_size -> page size
```
```
Response: success
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 23,
            "sku": "EP007",
            "size": 7,
            "type": "E",
            "flavor": "V"
        }
    ]
```