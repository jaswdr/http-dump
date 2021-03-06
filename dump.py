#!/usr/bin/env python

import socket
import os
import sys
import json
from uuid import uuid4
import tempfile
from flask import Flask, request, Response

app = Flask(__name__)


def save_request(uuid, request):
    req_data = {}
    req_data["uuid"] = uuid
    req_data["endpoint"] = request.endpoint
    req_data["hostname"] = socket.gethostname()
    req_data["method"] = request.method
    req_data["cookies"] = request.cookies
    req_data["data"] = request.data
    req_data["headers"] = dict(request.headers)
    req_data["headers"].pop("Cookie", None)
    req_data["args"] = request.args
    req_data["form"] = request.form
    req_data["remote_addr"] = request.remote_addr
    files = []
    for name, fs in request.files.items():
        dst = tempfile.NamedTemporaryFile()
        fs.save(dst)
        dst.flush()
        filesize = os.stat(dst.name).st_size
        dst.close()
        files.append(
            {
                "name": name,
                "filename": fs.filename,
                "filesize": filesize,
                "mimetype": fs.mimetype,
                "mimetype_params": fs.mimetype_params,
            }
        )
    req_data["files"] = files
    return req_data


@app.before_request
def before_request():
    print(request.method, request.endpoint)


@app.after_request
def after_request(resp):
    resp.headers.add("Access-Control-Allow-Origin", "*")
    resp.headers.add("Access-Control-Allow-Headers", "Content-Type, X-Token")
    resp.headers.add("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE")
    return resp


@app.route("/", defaults={"path": ""}, methods=["GET", "POST", "PUT", "DELETE"])
@app.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def dump(path):
    uuid = uuid4().hex
    req_data = save_request(uuid, request)
    req_data["path"] = path
    resp = Response(
        json.dumps(req_data, indent=4, default=str), mimetype="application/json"
    )
    resp.set_cookie("test-cookie", value="test-cookie-value")
    return resp


if __name__ == "__main__":
    app.run("0.0.0.0", port=int(sys.argv[1]), debug=False)
