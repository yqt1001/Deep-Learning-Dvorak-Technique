import time
import html_loader
import os

save_images = True
valid_satellites = ["goes11", "goes12", "goes13", "goes15", "himawari8", "msg3", "msg2", "msg1", "mtsat2", "mtsat1r", "meteo7", "gms6"]
basins = ["ATL/", "CPAC/", "EPAC/", "IO/", "WPAC/"]
data_out_file_name = "training"
year_url = ""
basin_url = ""
storm_url = ""
base_url = "https://www.nrlmry.navy.mil/tcdat/tc"

if __name__ == '__main__':
    start = time.time()

    if save_images:
        if not os.path.exists("./images/"):
            os.makedirs("./images/")

    if year_url != "":
        html_loader.load_year(year_url)
    elif basin_url != "":
        html_loader.load_basin(basin_url)
    elif storm_url != "":
        html_loader.load_storm(storm_url)
    elif base_url != "":
        for year in range(17, 3, -1):
            if year < 10:
                year = "0" + str(year)
            html_loader.load_year(base_url + str(year) + "/")

    print("Took " + str(time.time() - start) + "s to complete.")
