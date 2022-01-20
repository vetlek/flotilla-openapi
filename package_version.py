import requests
import yaml

URL = "https://test.pypi.org/pypi/flotilla-openapi/json"

def is_newer(version1, version2):
    if version1.split(".")[0] > version2.split(".")[0]:
        return True
    if version1.split(".")[0] == version2.split(".")[0] and version1.split(".")[1] > version2.split(".")[1]:
        return True
    return False

if __name__ == "__main__":
    with open("openapi.yaml","r") as stream:
        api_spec = yaml.safe_load(stream)
    openapi_version = api_spec["info"]["version"]
    try:
        pypi_version = requests.get(URL).json()["info"]["version"]
    except Exception:
        pypi_version = "0.0.0"
    if is_newer(openapi_version, pypi_version):
        print(openapi_version)
        exit()
    updated_version = f"{pypi_version.split('.')[0]}.{int(pypi_version.split('.')[1])}.{int(pypi_version.split('.')[2])+1}"
    api_spec["info"]["version"] = updated_version
    with open("openapi.yaml","w") as file:
        yaml.dump(api_spec, file, sort_keys=False)
    print(updated_version)
