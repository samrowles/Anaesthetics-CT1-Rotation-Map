import json
from build_ct1_data import HOSPITALS, REGION_COLORS, csv_rows
from rotations_builder import build_rotations
from rotations_builder_wales_tv_york_wessex import (
    get_wales_rotations,
    get_thames_valley_rotations,
    get_yorkshire_rotations,
    get_wessex_rotations
)
from rotations_builder_london_kss_wm_ne import (
    get_london_rotations,
    get_kss_rotations,
    get_west_midlands_rotations,
    get_north_east_rotations
)
from rotations_builder_eoe import get_eoe_rotations
from rotations_builder_nw import get_north_west_rotations
from rotations_builder_em import get_east_midlands_rotations

all_rotations = []
all_rotations.extend(build_rotations()) # Severn (8) + Peninsula (7) = 15
all_rotations.extend(get_wales_rotations(csv_rows)) # 7
all_rotations.extend(get_thames_valley_rotations(csv_rows)) # 4
all_rotations.extend(get_yorkshire_rotations(csv_rows)) # 7
all_rotations.extend(get_wessex_rotations(csv_rows)) # 2
all_rotations.extend(get_london_rotations(csv_rows)) # 4
all_rotations.extend(get_kss_rotations(csv_rows)) # 2
all_rotations.extend(get_west_midlands_rotations(csv_rows)) # 2
all_rotations.extend(get_north_east_rotations(csv_rows)) # 1
all_rotations.extend(get_eoe_rotations(csv_rows)) # 12
all_rotations.extend(get_north_west_rotations(csv_rows)) # 13
all_rotations.extend(get_east_midlands_rotations(csv_rows)) # 12

print(f"Total rotations gathered: {len(all_rotations)}")

# Validate hospital references
missing_hosps = set()
for r in all_rotations:
    for s in r["stages"]:
        h = s["hosp"]
        if h not in HOSPITALS:
            missing_hosps.add(h)

if missing_hosps:
    print(f"ERROR: Missing hospitals: {missing_hosps}")
else:
    print("SUCCESS: All hospital names found in HOSPITALS!")

# Validate region references
missing_regions = set()
for r in all_rotations:
    if r["region"] not in REGION_COLORS:
        missing_regions.add(r["region"])

if missing_regions:
    print(f"ERROR: Missing regions in REGION_COLORS: {missing_regions}")
else:
    print("SUCCESS: All regions match REGION_COLORS!")

# Validate unique IDs
ids = [r["id"] for r in all_rotations]
if len(ids) != len(set(ids)):
    print("ERROR: Duplicate IDs found!")
else:
    print("SUCCESS: All IDs are unique!")

# Validate all CSV codes are mapped
csv_prefs = set(r["Preference"] for r in csv_rows.values())
rot_codes = set(r["code"] for r in all_rotations)
missing_prefs = csv_prefs - rot_codes
extra_codes = rot_codes - csv_prefs
print(f"Missing CSV preferences: {len(missing_prefs)}")
print(f"Extra codes: {len(extra_codes)}")
