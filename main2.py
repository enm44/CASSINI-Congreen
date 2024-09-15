import openeo
import matplotlib
import xarray as xr
import numpy as np

aoi = {
    'type': 'Square',
    "coordinates": [
            19.331941,
            40.909329,
            20.256917,
            41.613357
            ]
}

connection = openeo.connect(url='openeo.dataspace.copernicus.eu')
connection.authenticate_oidc()

udf = openeo.UDF(
"""
//VERSION=3
function setup() {
  return {
    input: ["B12","B11","B09","B06","B05","B04","B03","dataMask"],
    output: { bands: 7 }
  };
}

function evaluatePixel(sample) {
  // B12, B11, B10 > 0.3, B05 B04 B03 < 0.3 
  let co2high = 0;
  let co2mid = 0;

  if ((sample.B12 + sample.B11) / 2 > 0.27 && (sample.B05 + sample.B04 + sample.B03) / 3 < 0.4 && sample.B09 < 0.09 && 0.25 < sample.B06) {
    co2high = 1;
  }
  if ((sample.B12 + sample.B11) / 2 > 0.2 && (sample.B05 + sample.B04 + sample.B03) / 3 < 0.5 && sample.B09 < 0.09 && 0.3 < sample.B06) {
    co2mid = 1;
  }

  // avco = (2.5 * (1.5 * (sample.B12 + sample.B11) / 2) - (0.1 / ((sample.B04 + sample.B05) / 2)));
  // return [sample.B12 * (0.1 / sample.B04), sample.B11 - 0.5, 3 * sample.B04, sample.dataMask];
  // return [5 * ((sample.B12 + sample.B11 + sample.B10) / 3) - (0.1 / ((sample.B04 + sample.B05) / 1.5)), sample.B10, (sample.B05 - sample.B04) / (sample.B05 + sample.B04) * 0.75, sample.dataMask];
  // (0.5 * ((sample.B12 + sample.B11) / 2) - (1 / ((sample.B04 + sample.B05) / 2)) - (1 / sample.B09))
  return [(1.5 * co2high) + (0.3 * co2mid), (0.1 * co2mid), (sample.B05 - sample.B04) / (sample.B05 + sample.B04), sample.dataMask];
}

""")

co2sat = connection.load_collection(
    'SENTINEL_2_L1C',
    temporal_extent=["2024-09-14","2024-09-14"],
    spatial_extent={"west":19.331941, "south":40.909329,
                    "east":20.256917, "north":41.613357}
)
co2sat = co2sat.aggregate_temporal_period(reducer="mean", period="day")

resmap = co2sat.apply_dimension(process=udf)

job_options = {
    "executor-memory": "2G",
    "executor-memoryOverhead": "3G",
    "executor-cores": "2",
}

job = resmap.execute_batch(title="C02 albania", outputfile="mapco2.nc", job_options=job_options)

mapdata = xr.load_dataset("mapco2.nc")




