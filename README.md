<p align="center">
  <img src="https://user-images.githubusercontent.com/12870986/101279908-b901f200-3800-11eb-84fe-badeb1d098d6.png">
</p>

# Short.it - where links get shorter

## Goal

A similar of bit.ly service that accepts a url and returns a short version of it

## Description

Short.it is built as API service also provided a simple frontend interface for direct use.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to run the software

```
python3.8
docker & docker-compose
```

### Installing & running

A step by step guide that tell you how to get a development env running

```
docker-compose -f local.yml up -d --build

# main homepage
http://localhost:8080

```

# REST API

The REST API to the example app is described below.

## Get a short url

### Request

`POST api/shortit/`

    curl -i -H 'Accept: application/json' -d 'url=http://example.com' http://localhost:8000/api/shortit/

### Response

```

HTTP/1.0 201 Created
Content-Type: application/json
Vary: Accept, Accept-Language, Cookie, Origin
Allow: POST, OPTIONS
Server-Timing: TimerPanel_utime;dur=111.32299999999961;desc="User CPU time", TimerPanel_stime;dur=9.498999999999924;desc="System CPU time", TimerPanel_total;dur=120.82199999999953;desc="Total CPU time", TimerPanel_total_time;dur=124.97806549072266;desc="Elapsed time", SQLPanel_sql_time;dur=1.8892288208007812;desc="SQL 4 queries", CachePanel_total_time;dur=0;desc="Cache 0 Calls"
X-Frame-Options: DENY
Content-Length: 74
Content-Language: en
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Server: Werkzeug/1.0.1 Python/3.8.6
Date: Sun, 06 Dec 2020 12:45:07 GMT

{"short_url":"http://localhost:8000/tier.app5fbbpp/","shortcode":"5fbbpp"}

```

## Get count of hits on the short url

### Request

`GET api/analytics/count/?q=shortcode`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/analytics/count/?q=eq99fp

### Response

```

HTTP/1.0 201 Created
Content-Type: application/json
Vary: Accept, Accept-Language, Cookie, Origin
Allow: GET, HEAD, OPTIONS
Server-Timing: TimerPanel_utime;dur=54.10099999999929;desc="User CPU time", TimerPanel_stime;dur=5.441000000001139;desc="System CPU time", TimerPanel_total;dur=59.54200000000043;desc="Total CPU time", TimerPanel_total_time;dur=62.82353401184082;desc="Elapsed time", SQLPanel_sql_time;dur=1.7075538635253906;desc="SQL 2 queries", CachePanel_total_time;dur=0;desc="Cache 0 Calls"
X-Frame-Options: DENY
Content-Length: 11
Content-Language: en
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Server: Werkzeug/1.0.1 Python/3.8.6
Date: Sun, 06 Dec 2020 12:57:18 GMT

{"count":4}

```

## configuration

You can add SHORT_PREFIX to make it appear infront of the shortcode in the generated link in .envs/.local/.django

```
#.envs/.local/.django

example:

SHORT_PREFIX=tier.app


```

## Authors

- **Mo Salam** - [Mo Salam](https://github.com/m7salam)
