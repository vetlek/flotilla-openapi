version=`python package_version.py`
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate -i local/openapi.yaml -g python-fastapi -o /local/openapi --additional-properties=packageName=flotilla_openapi,packageVersion=${version}
