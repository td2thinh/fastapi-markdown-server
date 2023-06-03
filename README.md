<br/>
<p align="center">
  <a href="https://github.com/td2thinh/fastapi-markdown-server">
    <img src="https://d3uyj2gj5wa63n.cloudfront.net/wp-content/uploads/2021/02/fastapi-logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Simple RestAPI CRUD Server</h3>

  <p align="center">
    Simple REST server created with FastAPI for my front end app
    <br/>
    <br/>
  </p>
</p>



## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)


## About The Project

REST server that provides CRUD APIs for my front end note taking app that supports markdown at: [Link to repo](https://github.com/td2thinh/react-markdown-note)

This was done to get a hands-on experience with building a back end using FastAPI and work with MongoDB

## Built With

FastAPI + Motor + Beanie

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* pipenv

```sh
pip install pipenv
```

### Installation

1. Get the URI to your cloud MongoDB

2. Clone the repo

```sh
git clone https://github.com/td2thinh/fastapi-markdown-server.git
```

3. Install python packages

```sh
pipenv install
```

4. Enter your DB URI and PORT in `.env`

```JS
PORT = 5889
MONGODB_URL = mongodb+srv://<username>:<password>@<Cluster>.mongodb.net/?retryWrites=true&w=majority
```

## Usage

Simple docs for the APIs available at http://localhost:PORT/docs
