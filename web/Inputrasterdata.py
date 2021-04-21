## After inputDB.py
import rasterio
## C:\Program Files\PostgreSQL\11\bin>raster2pgsql -C -s 5186
## C:\Users\rlaeh\Desktop\Forestfire\kangwondo\GTIF_GRS80\Gangneung_grid.tif Gangneung_grid
## | psql -U postgres -d webgis
import rasterio.features
import rasterio.warp

data_set = rasterio.open('kangwondo//GTIF_GRS80//gangneung_grid.tif')
Gangneung_grid = data_set.read(1);
print(Gangneung_grid)
with rasterio.open('kangwondo//GTIF_GRS80//gangneung_grid.tif') as dataset:

    # Read the dataset's valid data mask as a ndarray.
    mask = dataset.dataset_mask()

    # Extract feature shapes and values from the array.
    for geom, val in rasterio.features.shapes(
            mask, transform=dataset.transform):

        # Transform shapes from the dataset's own coordinate
        # reference system to CRS84 (EPSG:4326).
        geom = rasterio.warp.transform_geom(
            dataset.crs, 'EPSG:5186', geom, precision=6)

        # Print GeoJSON shapes to stdout.
        print(geom)