# Dev Containers

* `chmod +x test.py`
* If copying a desired `devcontainer.json` to the root of `.devcontainer`, remember to update the relative path
```json
"build": {
    "dockerfile": "../Dockerfile"
},
```
to 
```json
"build": {
    "dockerfile": "Dockerfile"
},
```