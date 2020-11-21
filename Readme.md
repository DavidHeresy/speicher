# Speicher

- Speicher is a webserver.
- Speicher delivers an index.html at /.
- Speicher stores data in the JSON format.
- GET /data returns the stored data.
- POST /data updatess the stored data.

## Config

This is what your `config.json` should look like:

```json
{
    "index": "path/to/index.html",
    "data": "path/to/data.json"
}
```

