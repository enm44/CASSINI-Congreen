import requests
import os
from sentinelhub import SHConfig
import numpy as np
import matplotlib.pyplot as plt
import codecs

os.chdir('C:/Users/Perdorues/Documents/git/cassini/TIRANA')

# Only run this cell if you have not created a configuration.

config = SHConfig()

config.sh_client_id = "sh-a4cc91d4-f201-47ff-b14b-f540f88cb8e4"
config.sh_client_secret = "dJEvwUiQNGzpJxwt3BDb283eTI9a8TMp"
config.sh_token_url = "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token"
config.sh_base_url = "https://sh.dataspace.copernicus.eu"
config.save("cdse")

url = "https://sh.dataspace.copernicus.eu/api/v1/process"
headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJYVUh3VWZKaHVDVWo0X3k4ZF8xM0hxWXBYMFdwdDd2anhob2FPLUxzREZFIn0.eyJleHAiOjE3MjY0MDE2MzYsImlhdCI6MTcyNjQwMTAzNiwiYXV0aF90aW1lIjoxNzI2Mzg4NTY0LCJqdGkiOiIwMmNlYmZiYy0yNTYxLTRlZmMtYjM1MC00OTBjZWQ2MTExZGMiLCJpc3MiOiJodHRwczovL2lkZW50aXR5LmRhdGFzcGFjZS5jb3Blcm5pY3VzLmV1L2F1dGgvcmVhbG1zL0NEU0UiLCJzdWIiOiIxYjIzNzVkNS01OGRlLTQyNTQtODBjNS0xZmVhMzliMzQxOGQiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJzaC0yZDA3NzkxNy1lZTZlLTQyOGUtODZiZC1lZjNmOWVlNGUyZTEiLCJub25jZSI6Ijg1NTY5MDk4LWNiN2UtNDZhZi04NjA0LWE5ZWVjYzM3YzQwOSIsInNlc3Npb25fc3RhdGUiOiIyNzNhNzgxMi1iMTM1LTQyOTktYjVjZi1jMDdmNmYxZDZkMWUiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cHM6Ly9zaGFwcHMuZGF0YXNwYWNlLmNvcGVybmljdXMuZXUiXSwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSB1c2VyLWNvbnRleHQiLCJzaWQiOiIyNzNhNzgxMi1iMTM1LTQyOTktYjVjZi1jMDdmNmYxZDZkMWUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwib3JnYW5pemF0aW9ucyI6WyJkZWZhdWx0LTFiMjM3NWQ1LTU4ZGUtNDI1NC04MGM1LTFmZWEzOWIzNDE4ZCJdLCJuYW1lIjoiRW5lYSBNdXNsaXUiLCJ1c2VyX2NvbnRleHRfaWQiOiJlNTA1ZDk4Zi00ZWZmLTRmNjgtYjY3Ni1jYjk4MTM4MDk4MWYiLCJjb250ZXh0X3JvbGVzIjp7fSwiY29udGV4dF9ncm91cHMiOlsiL2FjY2Vzc19ncm91cHMvdXNlcl90eXBvbG9neS9jb3Blcm5pY3VzX2dlbmVyYWwvIiwiL29yZ2FuaXphdGlvbnMvZGVmYXVsdC0xYjIzNzVkNS01OGRlLTQyNTQtODBjNS0xZmVhMzliMzQxOGQvcmVndWxhcl91c2VyLyJdLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJlbmVhbXVzbGl1QGdtYWlsLmNvbSIsImdpdmVuX25hbWUiOiJFbmVhIiwidXNlcl9jb250ZXh0IjoiZGVmYXVsdC0xYjIzNzVkNS01OGRlLTQyNTQtODBjNS0xZmVhMzliMzQxOGQiLCJmYW1pbHlfbmFtZSI6Ik11c2xpdSIsImVtYWlsIjoiZW5lYW11c2xpdUBnbWFpbC5jb20ifQ.E1mazhrj7qE76N6NkNJoXY-KMwDDKcPXOwdttdGRpAuB8jIb_EAkvM7XymoeS8gsUYGKFaY87HdMuOvCAtXMGKw4fkGZBx7FY8LA6B35vgMYOI_uzPvRBgZm8OQeG7UHOr5dAcNUOHvT_8-J3-dLNPO9f727i12vgsDTyE_EnOqxNb2_nRLTM_VuW9WjxV1j-CWiWmObMYsfCVzbJga4ZOgnBxxpVD0-PDeXZDrKODXzoZvYehTvqemIyZNRwV1cNdIEVKGiby8oxeAFuVGjTZRr7ikEiDefN4alWeQy5GkKkYQ1KCmiCsvaMyfx6KFyWkuC2vLhGspDU1X8XZjeNw"
}
data = {
  "input": {
    "bounds": {
      "bbox": [
        18.093477,
        39.384998,
        21.783405,
        43.100732
      ]
    },
    "data": [
      {
        "dataFilter": {
          "timeRange": {
            "from": "2024-08-14T00:00:00Z",
            "to": "2024-09-14T23:59:00Z"
          }
        },
        "type": "sentinel-2-l1c"
      }
    ]
  },
  "output": {
    "width": 2000,
    "height": 2500,
    "responses": [
      {
        "identifier": "default",
        "format": {
          "type": "image/jpeg"
        }
      }
    ]
  },
"evalscript": "//VERSION=3\nfunction setup() {\n  return {\n    input: [\"B12\",\"B11\",\"B09\",\"B06\",\"B05\",\"B04\",\"B03\",\"dataMask\"],\n    output: { bands: 7 }\n  };\n}\n\nfunction evaluatePixel(sample) {\n  // B12, B11, B10 > 0.3, B05 B04 B03 < 0.3 \n  let co2high = 0;\n  let co2mid = 0;\n\n  if ((sample.B12 + sample.B11) / 2 > 0.27 && (sample.B05 + sample.B04 + sample.B03) / 3 < 0.4 && sample.B09 < 0.09 && 0.25 < sample.B06) {\n    co2high = 1;\n  }\n  if ((sample.B12 + sample.B11) / 2 > 0.2 && (sample.B05 + sample.B04 + sample.B03) / 3 < 0.5 && sample.B09 < 0.09 && 0.3 < sample.B06) {\n    co2mid = 1;\n  }\n\n  // avco = (2.5 * (1.5 * (sample.B12 + sample.B11) / 2) - (0.1 / ((sample.B04 + sample.B05) / 2)));\n  // return [sample.B12 * (0.1 / sample.B04), sample.B11 - 0.5, 3 * sample.B04, sample.dataMask];\n  // return [5 * ((sample.B12 + sample.B11 + sample.B10) / 3) - (0.1 / ((sample.B04 + sample.B05) / 1.5)), sample.B10, (sample.B05 - sample.B04) / (sample.B05 + sample.B04) * 0.75, sample.dataMask];\n  // (0.5 * ((sample.B12 + sample.B11) / 2) - (1 / ((sample.B04 + sample.B05) / 2)) - (1 / sample.B09))\n  return [(1.5 * co2high) + (1 * co2mid) + (0.5 * sample.B05) + (0.7 * sample.B04), (0.1 * co2mid) + (1 * sample.B04), (sample.B05 - sample.B04) / (sample.B05 + sample.B04) + (1 * sample.B03), sample.dataMask];\n}\n"
}
# "evalscript": "//VERSION=3\nfunction setup() {\n  return {\n    input: [\"B12\",\"B11\",\"B09\",\"B06\",\"B05\",\"B04\",\"B03\",\"dataMask\"],\n    output: { bands: 7 }\n  };\n}\n\nfunction evaluatePixel(sample) {\n  // B12, B11, B10 > 0.3, B05 B04 B03 < 0.3 \n  let co2high = 0;\n  let co2mid = 0;\n\n  if ((sample.B12 + sample.B11) / 2 > 0.27 && (sample.B05 + sample.B04 + sample.B03) / 3 < 0.4 && sample.B09 < 0.09 && 0.25 < sample.B06) {\n    co2high = 1;\n  }\n  if ((sample.B12 + sample.B11) / 2 > 0.2 && (sample.B05 + sample.B04 + sample.B03) / 3 < 0.5 && sample.B09 < 0.09 && 0.3 < sample.B06) {\n    co2mid = 1;\n  }\n\n  // avco = (2.5 * (1.5 * (sample.B12 + sample.B11) / 2) - (0.1 / ((sample.B04 + sample.B05) / 2)));\n  // return [sample.B12 * (0.1 / sample.B04), sample.B11 - 0.5, 3 * sample.B04, sample.dataMask];\n  // return [5 * ((sample.B12 + sample.B11 + sample.B10) / 3) - (0.1 / ((sample.B04 + sample.B05) / 1.5)), sample.B10, (sample.B05 - sample.B04) / (sample.B05 + sample.B04) * 0.75, sample.dataMask];\n  // (0.5 * ((sample.B12 + sample.B11) / 2) - (1 / ((sample.B04 + sample.B05) / 2)) - (1 / sample.B09))\n  return [(1.5 * co2high) + (1 * co2mid) + (0.2 * sample.B05), (0.1 * co2mid) + (1 * sample.B04), (sample.B05 - sample.B04) / (sample.B05 + sample.B04) + (1 * sample.B03), sample.dataMask];\n}\n"

response = requests.post(url, headers=headers, json=data)
print(response.content)
with open('tirana2021.jpg', 'wb') as resmap:
  resmap.write(response.content)