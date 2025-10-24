<!-- Banner -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=timeAuto&height=200&section=header&text=Moco+Bot&fontSize=60&fontAlign=50&fontAlignY=35&animation=fadeIn" />
</div>


<h1 align="center">
   Moco Bot
</h1>

<p align="center">
  <b>A Public, Downgraded Version of  <img src="https://img.shields.io/badge/Telegram_Bot-MOCO-blue?style=flat-square&logo=telegram/http://t.me/DearMocoBot?start=true?style=flat-square" /> </b>
  <br>
  <i>Built with Pyrofork • Docker Ready • Multi-Platform Deployment</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-2.0.0-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Pyrofork-Latest-important?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python" />
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=bisug&style=flat-square&color=blue" />
  <img src="https://img.shields.io/github/stars/bisug/Moco-Bot?style=flat-square&color=yellow" />
  <img src="https://img.shields.io/github/forks/bisug/Moco-Bot?style=flat-square&color=green" />
  <img src="https://img.shields.io/github/issues/bisug/Moco-Bot?style=flat-square&color=red" />
  <img src="https://img.shields.io/github/last-commit/bisug/Moco-Bot?style=flat-square&color=purple" />
  <img src="https://img.shields.io/github/license/bisug/Moco-Bot?style=flat-square&color=orange" />
  <img src="https://img.shields.io/github/repo-size/bisug/Moco-Bot?style=flat-square&color=lightgrey" />
  <img src="https://img.shields.io/badge/Python-3.12+-blue?style=flat-square&logo=python" />
  <img src="https://img.shields.io/badge/Docker-Ready-cyan?style=flat-square&logo=docker" />
  <img src="https://img.shields.io/badge/Telegram-Bot-blue?style=flat-square&logo=telegram" />
</p>


## 🎯 Overview

Moco-Bot is a sophisticated Telegram bot built with **pyrofork**, designed for seamless deployment across modern cloud platforms. Featuring a robust Docker setup and multi-deployment options, it brings unique Free Fire utilities and essential Telegram functionalities to your fingertips.

## ✨ Core Features

### 🎮 Free Fire Utilities
| Command | Parameters | Description | Restrictions |
|---------|------------|-------------|--------------|
| `/like` | `<region> <uid>` | Send 100 likes to Free Fire player profile 🎁 | ⚠️ Group-only for API limit management |

> **ℹ️ How Free Fire Likes Work?**
> This feature utilizes Garena's backend API through a network of automated Guest accounts to deliver likes directly to specified player profiles.


## **Deployment**

This bot is configured to be easily deployed on cloud platforms such as Heroku, Render, and Koyeb.

**Web Application Mode**

For platforms like Render and Koyeb free tiers, where exposing a public port for a web application is often required, the bot can switch modes:

· Set WEB_APP to true in your configuration (config.py or .env file). This enables the built-in Flask server to expose the necessary port.

**Heroku Deployment**

· As a Standard Worker: For a typical Heroku bot deployment, set WEB_APP to false
· As a Web Dyno: If you choose to deploy it as a web application exposing a port on Heroku, set WEB_APP to true

## Deploy Button 

[![Deploy on Render](https://img.shields.io/badge/Deploy-Render-0078D7?style=for-the-badge&logo=render&logoWidth=80)](https://render.com/deploy?repo=https://github.com/bisug/Moco-Bot) 
[![Deploy on Heroku](https://img.shields.io/badge/Deploy-Heroku-430098?style=for-the-badge&logo=heroku&logoWidth=80)](https://heroku.com/deploy?template=https://github.com/bisug/Moco-Bot) 
[![Deploy on Koyeb](https://img.shields.io/badge/Deploy-Koyeb-FF6600?style=for-the-badge&logo=koyeb&logoWidth=80)](https://app.koyeb.com/deploy?repo=https://github.com/bisug/Moco-Bot)

## 🔑 Environment Variables

Below are the required and optional environment variables for deployment.

```env
API_ID=              # Required - Get from https://my.telegram.org
API_HASH=            # Required - From https://my.telegram.org
BOT_TOKEN=           # Required - Get t.me/BotFather
OWNER_ID=            # Required - Your Telegram user ID
LOGGER_GROUP_ID=     # Required - Log group/channel ID
MONGO_URL=					# Required - MongoDB connection string
WEB_APP=
BOT_NAME=
BOT_USERNAME=
LIKE_API_URL=
LIKE_API_KEY=

```


## 🐳 **Docker Setup**

The recommended way to deploy Moco is using the provided Dockerfile for a consistent, containerized environment.

**Dockerfile**

```
# Python version
FROM python:3.12

# Update OS packages
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Set working directory
WORKDIR /app

# Copy requirements first (cache layer)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Start the bot
CMD ["python", "-m", "Moco"]
```

## **Build and Run**

1. **Clone the repository:**

```
git clone git@github.com:bisug/Moco-Bot.git
```

1. **Build the Docker image:**

```
docker build -t moco-bot .
```

1. **Run the container:**

```
docker run -d --name moco-instance moco-bot
```

* <b> *MADE BY <a href="https://github.com/bisug">BISU G</a>* </b>
