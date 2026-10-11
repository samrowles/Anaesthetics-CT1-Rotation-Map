import csv

with open('ct1_rotations.csv', encoding='utf-8') as f:
    csv_rows = {int(r['Current Assigned Rank']): r for r in csv.DictReader(f)}

def build_rotations():
    rotations = []

    # 1. SOUTH WEST - SEVERN
    rotations.extend([
        {
            "id": "ct1-severn-north-bristol-1e",
            "code": csv_rows[1]["Preference"],
            "region": "South West - Severn",
            "title": "North Bristol (2 yrs) & Swindon (1 yr)",
            "places": csv_rows[1]["Places Available"],
            "hubs": {
                "driver": { "name": "North Bristol / Almondsbury (M4/M5)", "coords": [51.5450, -2.5750], "desc": "M4 junction 16/19. 15m to Southmead; 42m to Swindon via M4.", "alert": "Convenient M4 access for the final Swindon year." },
                "transit": { "name": "Bristol Parkway", "coords": [51.5130, -2.5420], "desc": "Fast direct trains to Swindon (23m); frequent local buses to Southmead.", "alert": "Bristol Parkway provides direct high-speed rail to Swindon." }
            },
            "stages": [
                { "stage": "CT1 - CT2 (24m)", "hosp": "Southmead Hospital (NBT)", "desc": "North Bristol Trust acute anaesthesia base" },
                { "stage": "CT3 (12m)", "hosp": "Great Western Hospital, Swindon", "desc": "Swindon acute placement" }
            ]
        },
        {
            "id": "ct1-severn-bristol-2",
            "code": csv_rows[2]["Preference"],
            "region": "South West - Severn",
            "title": "Bristol BRI (CT1), Swindon (CT2) & Bristol (CT3)",
            "places": csv_rows[2]["Places Available"],
            "hubs": {
                "driver": { "name": "Bristol / Keynsham", "coords": [51.4130, -2.4970], "desc": "Central Bristol access via A4; M4 corridor access to Swindon.", "alert": "Swindon year requires 45m drive via M4." },
                "transit": { "name": "Bristol Temple Meads", "coords": [51.4490, -2.5810], "desc": "Walk/bus to BRI; direct fast trains to Swindon (35m).", "alert": "Trains run frequently between Bristol and Swindon." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Bristol Royal Infirmary (UHBW)", "desc": "Central Bristol teaching base" },
                { "stage": "CT2 (12m)", "hosp": "Great Western Hospital, Swindon", "desc": "Swindon acute placement" },
                { "stage": "CT3 (12m)", "hosp": "Bristol Royal Infirmary (UHBW)", "desc": "Central Bristol teaching base" }
            ]
        },
        {
            "id": "ct1-severn-cheltenham-gloucester-3",
            "code": csv_rows[3]["Preference"],
            "region": "South West - Severn",
            "title": "Gloucester (2 yrs) & Bristol BRI (1 yr)",
            "places": csv_rows[3]["Places Available"],
            "hubs": {
                "driver": { "name": "Stonehouse / Stroud (M5 J13)", "coords": [51.7480, -2.2820], "desc": "M5 corridor midway between Gloucester (18m) and Bristol (32m).", "alert": "Ideal equidistant location on the M5 corridor." },
                "transit": { "name": "Gloucester / Cheltenham Spa", "coords": [51.8650, -2.2380], "desc": "Direct rail to Bristol Temple Meads (40m) and central Gloucester.", "alert": "Direct trains on CrossCountry/GWR line." }
            },
            "stages": [
                { "stage": "CT1 - CT2 (24m)", "hosp": "Gloucestershire Royal Hospital", "desc": "Gloucestershire acute base" },
                { "stage": "CT3 (12m)", "hosp": "Bristol Royal Infirmary (UHBW)", "desc": "Central Bristol UHBW placement" }
            ]
        },
        {
            "id": "ct1-severn-swindon-2e",
            "code": csv_rows[4]["Preference"],
            "region": "South West - Severn",
            "title": "Swindon (2 yrs) & North Bristol (1 yr)",
            "places": csv_rows[4]["Places Available"],
            "hubs": {
                "driver": { "name": "Swindon / Chippenham (M4 J16/17)", "coords": [51.5150, -1.9120], "desc": "M4 corridor. 15m to Great Western Hospital; 35m to Southmead.", "alert": "Chippenham/Swindon gives easy access to both sites." },
                "transit": { "name": "Swindon Station", "coords": [51.5640, -1.7850], "desc": "High-speed rail to Bristol Parkway (23m); local buses to GWH.", "alert": "Local buses connect Swindon station to Great Western Hospital." }
            },
            "stages": [
                { "stage": "CT1 - CT2 (24m)", "hosp": "Great Western Hospital, Swindon", "desc": "Swindon acute base" },
                { "stage": "CT3 (12m)", "hosp": "Southmead Hospital (NBT)", "desc": "North Bristol Trust base" }
            ]
        },
        {
            "id": "ct1-severn-yeovil-6",
            "code": csv_rows[6]["Preference"],
            "region": "South West - Severn",
            "title": "Taunton (Musgrove Park) & Yeovil Rotation",
            "places": csv_rows[6]["Places Available"],
            "hubs": {
                "driver": { "name": "Somerton / Ilminster", "coords": [51.0530, -2.7350], "desc": "A303 / A358 corridor midway between Taunton (25m) and Yeovil (22m).", "alert": "Rural commute along A358 and A372." },
                "transit": { "name": "Taunton Station", "coords": [51.0230, -3.1030], "desc": "Mainline rail to Taunton; bus services connect to Yeovil.", "alert": "Public transport between Taunton and Yeovil can be limited for early shifts; car recommended." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Musgrove Park Hospital, Taunton", "desc": "Musgrove Park Hospital Taunton (first 12 months)" },
                { "stage": "CT2 - CT3 (24m)", "hosp": "Yeovil District Hospital", "desc": "Working between Yeovil District Hospital & Musgrove Park" },
                { "stage": "CT2 - CT3 (24m)", "hosp": "Musgrove Park Hospital, Taunton", "desc": "Musgrove Park shared placement" }
            ]
        },
        {
            "id": "ct1-severn-north-bristol-4",
            "code": csv_rows[7]["Preference"],
            "region": "South West - Severn",
            "title": "North Bristol (Southmead) Severn Track",
            "places": csv_rows[7]["Places Available"],
            "hubs": {
                "driver": { "name": "North Bristol / Westbury-on-Trym", "coords": [51.4980, -2.6160], "desc": "5-10m drive to Southmead Hospital.", "alert": "Bristol CAZ in city centre, but Southmead is outside CAZ." },
                "transit": { "name": "Bristol Parkway / Horfield", "coords": [51.5130, -2.5420], "desc": "Frequent buses (76, 77) direct to Southmead Hospital.", "alert": "Direct bus routes from North Bristol." }
            },
            "stages": [
                { "stage": "CT1 - CT3", "hosp": "Southmead Hospital (NBT)", "desc": "North Bristol Severn footprint placement" }
            ]
        },
        {
            "id": "ct1-severn-bath-1",
            "code": csv_rows[8]["Preference"],
            "region": "South West - Severn",
            "title": "Bath (Royal United Hospital) Severn Track",
            "places": csv_rows[8]["Places Available"],
            "hubs": {
                "driver": { "name": "Bath / Saltford", "coords": [51.4010, -2.4570], "desc": "A4 corridor. 15m to Royal United Hospital Bath; 25m to Bristol.", "alert": "Bath clean air zone applies in central city; RUH has staff parking." },
                "transit": { "name": "Bath Spa", "coords": [51.3770, -2.3570], "desc": "Frequent buses from Bath Spa station to RUH (approx 15-20m).", "alert": "Bus connections required from Bath Spa railway station." }
            },
            "stages": [
                { "stage": "CT1 - CT3", "hosp": "Royal United Hospital, Bath", "desc": "Bath RUH Severn footprint placement" }
            ]
        },
        {
            "id": "ct1-severn-swindon-5",
            "code": csv_rows[9]["Preference"],
            "region": "South West - Severn",
            "title": "Swindon (Great Western) Severn Track",
            "places": csv_rows[9]["Places Available"],
            "hubs": {
                "driver": { "name": "Swindon South / Coate Water", "coords": [51.5360, -1.7450], "desc": "Directly adjacent to M4 J15 and A419. 3-5m to GWH.", "alert": "Immediate access to hospital off M4 J15." },
                "transit": { "name": "Swindon Central", "coords": [51.5640, -1.7850], "desc": "Frequent bus routes (1, 1A, 2) from Swindon station directly to GWH.", "alert": "Direct buses run every 10 mins to hospital." }
            },
            "stages": [
                { "stage": "CT1 - CT3", "hosp": "Great Western Hospital, Swindon", "desc": "Great Western Hospital Swindon Severn placement" }
            ]
        }
    ])

    # 2. SOUTH WEST - PENINSULA
    rotations.extend([
        {
            "id": "ct1-peninsula-north-devon-2",
            "code": csv_rows[10]["Preference"],
            "region": "South West - Peninsula",
            "title": "North Devon (Barnstaple) CT1-CT2 Post",
            "places": csv_rows[10]["Places Available"],
            "hubs": {
                "driver": { "name": "Barnstaple / Bideford", "coords": [51.0820, -4.0620], "desc": "5-10m drive to North Devon District Hospital.", "alert": "Picturesque coastal location; driving recommended due to rural transit links." },
                "transit": { "name": "Barnstaple Station", "coords": [51.0740, -4.0630], "desc": "Tarka Line trains to Exeter; local buses connect to hospital.", "alert": "Bus connection needed from Barnstaple rail station." }
            },
            "stages": [
                { "stage": "CT1 - CT2 (24m)", "hosp": "North Devon District Hospital, Barnstaple", "desc": "North Devon acute placement (CT3 year agreed with TPD)" }
            ]
        },
        {
            "id": "ct1-peninsula-taunton-6",
            "code": csv_rows[11]["Preference"],
            "region": "South West - Peninsula",
            "title": "Taunton (Musgrove Park) 3-Year Post",
            "places": csv_rows[11]["Places Available"],
            "hubs": {
                "driver": { "name": "Taunton / Wellington", "coords": [51.0150, -3.1250], "desc": "5-10m drive to Musgrove Park Hospital.", "alert": "Easy access from M5 J25/J26." },
                "transit": { "name": "Taunton Central", "coords": [51.0230, -3.1030], "desc": "Direct buses and short cycle from Taunton rail station.", "alert": "Good bus services linking station and town centre to Musgrove Park." }
            },
            "stages": [
                { "stage": "CT1 - CT3 (36m)", "hosp": "Musgrove Park Hospital, Taunton", "desc": "Musgrove Park Hospital for full 3-year programme" }
            ]
        },
        {
            "id": "ct1-peninsula-torbay-5",
            "code": csv_rows[12]["Preference"],
            "region": "South West - Peninsula",
            "title": "Torbay Hospital 3-Year Post",
            "places": csv_rows[12]["Places Available"],
            "hubs": {
                "driver": { "name": "Torquay / Newton Abbot", "coords": [50.5050, -3.5850], "desc": "A380 corridor. 8m from Newton Abbot, 10m from Torquay centre.", "alert": "Newton Abbot offers dual access towards Exeter and Torbay." },
                "transit": { "name": "Torre / Torquay", "coords": [50.4780, -3.5380], "desc": "Torre station is within walking/bus distance of Torbay Hospital.", "alert": "Torre railway station is ~15m walk or short bus ride to hospital." }
            },
            "stages": [
                { "stage": "CT1 - CT3 (36m)", "hosp": "Torbay Hospital", "desc": "Torbay Hospital for full 3-year programme" }
            ]
        },
        {
            "id": "ct1-peninsula-cornwall-4",
            "code": csv_rows[13]["Preference"],
            "region": "South West - Peninsula",
            "title": "Cornwall (Royal Cornwall, Truro) 3-Year Post",
            "places": csv_rows[13]["Places Available"],
            "hubs": {
                "driver": { "name": "Truro / Falmouth", "coords": [50.2350, -5.0750], "desc": "A39 corridor. 8m from Truro centre; 20m from Falmouth.", "alert": "Main hospital located at Treliske, west of Truro." },
                "transit": { "name": "Truro Station", "coords": [50.2640, -5.0640], "desc": "Direct buses and Park & Ride services from Truro station to Treliske.", "alert": "Frequent bus services run between station and hospital." }
            },
            "stages": [
                { "stage": "CT1 - CT3 (36m)", "hosp": "Royal Cornwall Hospital, Truro", "desc": "Treliske site for full 3-year programme" }
            ]
        },
        {
            "id": "ct1-peninsula-exeter-1",
            "code": csv_rows[14]["Preference"],
            "region": "South West - Peninsula",
            "title": "Exeter (Royal Devon & Exeter) 3-Year Post",
            "places": csv_rows[14]["Places Available"],
            "hubs": {
                "driver": { "name": "Exeter / Topsham", "coords": [50.7050, -3.5050], "desc": "5-10m drive to RD&E Wonford. Easy access from M5 J30.", "alert": "Staff parking permit system at Wonford." },
                "transit": { "name": "Exeter Central / St Davids", "coords": [50.7280, -3.5350], "desc": "Direct bus routes (H bus) from central Exeter to RD&E Wonford.", "alert": "H bus runs directly every 15 mins to hospital entrance." }
            },
            "stages": [
                { "stage": "CT1 - CT3 (36m)", "hosp": "Royal Devon & Exeter Hospital", "desc": "Wonford site for full 3-year programme" }
            ]
        },
        {
            "id": "ct1-peninsula-plymouth-3",
            "code": csv_rows[24]["Preference"],
            "region": "South West - Peninsula",
            "title": "Plymouth (Derriford) 3-Year Post (Post 3)",
            "places": csv_rows[24]["Places Available"],
            "hubs": {
                "driver": { "name": "Plymouth North / Crownhill", "coords": [50.4100, -4.1350], "desc": "5m drive to Derriford Hospital.", "alert": "Tavistock Road / A386 corridor can have morning congestion." },
                "transit": { "name": "Plymouth Station / City Centre", "coords": [50.3780, -4.1430], "desc": "Frequent bus routes (42, 50, 51) run direct to Derriford Hospital.", "alert": "Dedicated hospital bus interchange at main entrance." }
            },
            "stages": [
                { "stage": "CT1 - CT3 (36m)", "hosp": "Derriford Hospital, Plymouth", "desc": "Derriford Major Trauma Centre for full 3-year programme" }
            ]
        },
        {
            "id": "ct1-peninsula-plymouth-1e",
            "code": csv_rows[25]["Preference"],
            "region": "South West - Peninsula",
            "title": "Plymouth (Derriford) 3-Year Post (Post 1E)",
            "places": csv_rows[25]["Places Available"],
            "hubs": {
                "driver": { "name": "Plymouth North / Crownhill", "coords": [50.4100, -4.1350], "desc": "5m drive to Derriford Hospital.", "alert": "Tavistock Road / A386 corridor can have morning congestion." },
                "transit": { "name": "Plymouth Station / City Centre", "coords": [50.3780, -4.1430], "desc": "Frequent bus routes (42, 50, 51) run direct to Derriford Hospital.", "alert": "Dedicated hospital bus interchange at main entrance." }
            },
            "stages": [
                { "stage": "CT1 - CT3 (36m)", "hosp": "Derriford Hospital, Plymouth", "desc": "Derriford Major Trauma Centre for full 3-year programme" }
            ]
        }
    ])

    return rotations
