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
all_rotations.extend(build_rotations())
all_rotations.extend(get_wales_rotations(csv_rows))
all_rotations.extend(get_thames_valley_rotations(csv_rows))
all_rotations.extend(get_yorkshire_rotations(csv_rows))
all_rotations.extend(get_wessex_rotations(csv_rows))
all_rotations.extend(get_london_rotations(csv_rows))
all_rotations.extend(get_kss_rotations(csv_rows))
all_rotations.extend(get_west_midlands_rotations(csv_rows))
all_rotations.extend(get_north_east_rotations(csv_rows))
all_rotations.extend(get_eoe_rotations(csv_rows))
all_rotations.extend(get_north_west_rotations(csv_rows))
all_rotations.extend(get_east_midlands_rotations(csv_rows))

# 1. Filter out rotations with no places
active_rotations = [r for r in all_rotations if int(r.get("places", 0) or 0) > 0]

# 2. Identify hospitals used in the remaining active rotations
used_hospitals = set()
for r in active_rotations:
    for s in r.get("stages", []):
        used_hospitals.add(s["hosp"])

# 3. Filter hospitals to only those used in active rotations
active_hospitals = {name: data for name, data in HOSPITALS.items() if name in used_hospitals}

lines = []
lines.append("// ============================================================================")
lines.append("// CT1 Anaesthetics National Placement Data")
lines.append("// ============================================================================")
lines.append("")
lines.append("const HOSPITALS = {")

# Group hospitals by region for clean reading
hosps_by_reg = {}
for name, data in active_hospitals.items():
    reg = data["region"]
    if reg not in hosps_by_reg:
        hosps_by_reg[reg] = []
    hosps_by_reg[reg].append((name, data))

first_reg = True
for reg, items in sorted(hosps_by_reg.items()):
    if not first_reg:
        lines.append("")
    first_reg = False
    lines.append(f"  // {reg}")
    for name, data in sorted(items):
        coords_str = f"[{data['coords'][0]}, {data['coords'][1]}]"
        lines.append(f'  "{name}": {{ coords: {coords_str}, region: "{data["region"]}" }},')

lines.append("};")
lines.append("")
lines.append("const REGION_COLORS = {")
for reg, col in sorted(REGION_COLORS.items()):
    lines.append(f'  "{reg}": "{col}",')
lines.append("};")
lines.append("")
lines.append("const ROTATIONS_DATA = [")

# Group rotations by region for clean code blocks
rot_by_reg = {}
for r in active_rotations:
    reg = r["region"]
    if reg not in rot_by_reg:
        rot_by_reg[reg] = []
    rot_by_reg[reg].append(r)

for reg, rots in rot_by_reg.items():
    lines.append(f"  // ==================== {reg.upper()} ====================")
    for rot in rots:
        lines.append("  {")
        lines.append(f'    id: "{rot["id"]}",')
        lines.append(f'    code: {json.dumps(rot["code"])},')
        lines.append(f'    region: "{rot["region"]}",')
        lines.append(f'    title: {json.dumps(rot["title"])},')
        lines.append(f'    places: {json.dumps(str(rot["places"]))},')
        lines.append("    hubs: {")
        d = rot["hubs"]["driver"]
        t = rot["hubs"]["transit"]
        lines.append(f'      driver: {{ name: {json.dumps(d["name"])}, coords: [{d["coords"][0]}, {d["coords"][1]}], desc: {json.dumps(d["desc"])}, alert: {json.dumps(d["alert"])} }},')
        lines.append(f'      transit: {{ name: {json.dumps(t["name"])}, coords: [{t["coords"][0]}, {t["coords"][1]}], desc: {json.dumps(t["desc"])}, alert: {json.dumps(t["alert"])} }}')
        lines.append("    },")
        lines.append("    stages: [")
        for s in rot["stages"]:
            lines.append(f'      {{ stage: {json.dumps(s["stage"])}, hosp: {json.dumps(s["hosp"])}, desc: {json.dumps(s["desc"])} }},')
        lines.append("    ]")
        lines.append("  },")

lines.append("];")
lines.append("")

with open("data.js", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("data.js successfully written!")
