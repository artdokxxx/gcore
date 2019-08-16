# GCORE TASK

## Description

Just rest api with one point

## Requirements

Python - `3.6.4`  
Python packages - `See requirements.txt`

## How use

You need install all requirements, use for this:  
```bash
pip install -r requirements.txt
```

If you want just run in cli for test:    

```bash
python manage.py runserver
```

## Structure

`app` - Django application  
`app/utils` - Some utils for services  
`app/views` - Directory with views  
`app/services` - Services  
`requirements` - Python packages requirements for project   

##Points

### [GET] /

Return information about last commit in GIT repository and start time APP

Example:

```json
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "commit": "12290ea81c41df46c1a3b91e7d6fe9849792afaf",
    "commit_date": "2019-08-16T12:35:58Z",
    "branch": "master",
    "version": "",
    "started": "2019-08-16T09:42:40Z",
    "uptime_seconds": 1
}
```
