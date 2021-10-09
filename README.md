# HTTP Dump

> Dump HTTP requests for debugging purpose

Requires Python >= 3.6

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/c7f663d457a04be3a72dbf69252ad387)](https://www.codacy.com/gh/jaswdr/http-dump/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jaswdr/http-dump&amp;utm_campaign=Badge_Grade)
[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/jaswdr/http-dump)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fjaswdr%2Fhttp-dump&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

## Getting Started

```
$ docker run -p 8080:80 ghcr.io/jaswdr/http-dump:master
 * Serving Flask app 'dump' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://10.0.0.1:80/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 995-808-312
```

Then open **http://localhost:8080/?foo=bar&bar=foo**

Example of response:
```
{
    "uuid": "9b513c673ee840b581b964b0aca3f62c",
    "endpoint": "dump",
    "method": "GET",
    "cookies": {
        "grafana_session": "88deff3280a7bcaab18922192d282442",
        "cookie-name": "cookie-value"
    },
    "data": "b''",
    "headers": {
        "Host": "10.0.0.1:8080",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:92.0) Gecko/20100101 Firefox/92.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Dnt": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    },
    "args": {
        "foo": "bar",
        "bar": "foo"
    },
    "form": {},
    "remote_addr": "10.0.0.2",
    "files": []
}
```

## Get involved

Have a question? Use the [Discussions](https://github.com/jaswdr/http-dump/discussions) page.

## License

http-dump is released under the MIT Licence. See the bundled LICENSE file for details.
