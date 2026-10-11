def get_east_midlands_rotations(csv_rows):
    south_stages_leic_first = [
        { "stage": "Feb 27 - Aug 27 (6m)", "hosp": "Leicester Royal Infirmary", "desc": "LRI acute base - Stage 1 initial" },
        { "stage": "Aug 27 - Feb 28 (6m)", "hosp": "Leicester Royal Infirmary", "desc": "LRI - IAC completion" },
        { "stage": "Feb 28 - Aug 28 (6m)", "hosp": "Northampton General Hospital", "desc": "Northampton General acute placement" },
        { "stage": "Aug 28 - Feb 29 (6m)", "hosp": "Northampton General Hospital", "desc": "Northampton General acute placement" },
        { "stage": "Feb 29 - Aug 29 (6m)", "hosp": "Leicester Royal Infirmary", "desc": "LRI specialist anaesthesia modules" },
        { "stage": "Aug 29 - Feb 30 (6m)", "hosp": "Leicester Royal Infirmary", "desc": "LRI Stage 1 completion" }
    ]

    south_stages_northampton_first = [
        { "stage": "Feb 27 - Aug 27 (6m)", "hosp": "Northampton General Hospital", "desc": "Northampton General acute base - Initial" },
        { "stage": "Aug 27 - Feb 28 (6m)", "hosp": "Northampton General Hospital", "desc": "Northampton General - IAC completion" },
        { "stage": "Feb 28 - Aug 28 (6m)", "hosp": "Leicester Royal Infirmary", "desc": "Leicester Royal Infirmary placement" },
        { "stage": "Aug 28 - Feb 29 (6m)", "hosp": "Leicester Royal Infirmary", "desc": "LRI acute & ITU placement" },
        { "stage": "Feb 29 - Aug 29 (6m)", "hosp": "Leicester Royal Infirmary", "desc": "LRI specialist anaesthesia modules" },
        { "stage": "Aug 29 - Feb 30 (6m)", "hosp": "Leicester Royal Infirmary", "desc": "LRI Stage 1 completion" }
    ]

    market_harborough_hubs = {
        "driver": { "name": "Market Harborough (A6)", "coords": [52.4750, -0.9250], "desc": "A6 / A508 corridor midway. 22m north to Leicester Royal Infirmary; 22m south to Northampton General.", "alert": "Market Harborough is the premier equidistant base between Leicester and Northampton." },
        "transit": { "name": "Market Harborough Station", "coords": [52.4810, -0.9160], "desc": "Midland Main Line rail north to Leicester (15m); connecting bus/drive to Northampton.", "alert": "Fast direct trains run north into Leicester in 15 mins." }
    }

    return [
        {
            "id": "ct1-east-midlands-north-1",
            "code": csv_rows[70]["Preference"],
            "region": "East Midlands",
            "title": "Lincolnshire (L14F27): Lincoln, Boston & Nottingham",
            "places": csv_rows[70]["Places Available"],
            "hubs": {
                "driver": { "name": "Newark-on-Trent (A46 / A17 / A1)", "coords": [53.0750, -0.8150], "desc": "Strategic crossroad. 22m northeast to Lincoln, 32m to Boston via A17, 28m southwest to Nottingham via A46.", "alert": "Newark is the best central base bridging Lincolnshire and Nottinghamshire." },
                "transit": { "name": "Newark Northgate / Lincoln", "coords": [53.0820, -0.8030], "desc": "Direct rail on Castle line to Lincoln (25m) and Nottingham (30m).", "alert": "Trains run directly from Newark to both Lincoln and Nottingham." }
            },
            "stages": [
                { "stage": "Feb 27 - Aug 27 (6m)", "hosp": "Lincoln County Hospital", "desc": "Lincoln acute base - Stage 1 initial" },
                { "stage": "Aug 27 - Feb 28 (6m)", "hosp": "Lincoln County Hospital", "desc": "Lincoln acute base - IAC completion" },
                { "stage": "Feb 28 - Aug 28 (6m)", "hosp": "Boston Pilgrim Hospital", "desc": "Pilgrim Hospital acute placement" },
                { "stage": "Aug 28 - Feb 29 (6m)", "hosp": "Nottingham City Hospital", "desc": "Elective & specialist surgery" },
                { "stage": "Feb 29 - Aug 29 (6m)", "hosp": "Nottingham City Hospital", "desc": "Specialist modules & ITU" },
                { "stage": "Aug 29 - Feb 30 (6m)", "hosp": "Queen's Medical Centre (QMC), Nottingham", "desc": "Major Trauma Centre placement" }
            ]
        },
        {
            "id": "ct1-east-midlands-north-1e",
            "code": csv_rows[71]["Preference"],
            "region": "East Midlands",
            "title": "Lincoln County Hospital Starting Post (1E)",
            "places": csv_rows[71]["Places Available"],
            "hubs": {
                "driver": { "name": "Lincoln North / Greetwell", "coords": [53.2350, -0.5150], "desc": "5m drive to Lincoln County Hospital.", "alert": "On-site hospital parking available." },
                "transit": { "name": "Lincoln Central Station", "coords": [53.2260, -0.5420], "desc": "Frequent city buses (4, 17, 18) connect Lincoln station to the hospital.", "alert": "Bus ride is approx 10m up to the hospital site." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Lincoln County Hospital", "desc": "Starting site - Lincoln County Hospital" }
            ]
        },
        {
            "id": "ct1-east-midlands-north-2",
            "code": csv_rows[72]["Preference"],
            "region": "East Midlands",
            "title": "Lincolnshire (L20F27): Boston, Lincoln & Nottingham",
            "places": csv_rows[72]["Places Available"],
            "hubs": {
                "driver": { "name": "Newark-on-Trent (A46 / A17 / A1)", "coords": [53.0750, -0.8150], "desc": "Strategic crossroad. 22m northeast to Lincoln, 32m to Boston via A17, 28m southwest to Nottingham via A46.", "alert": "Newark is the best central base bridging Lincolnshire and Nottinghamshire." },
                "transit": { "name": "Newark Northgate / Lincoln", "coords": [53.0820, -0.8030], "desc": "Direct rail on Castle line to Lincoln (25m) and Nottingham (30m).", "alert": "Trains run directly from Newark to both Lincoln and Nottingham." }
            },
            "stages": [
                { "stage": "Feb 27 - Aug 27 (6m)", "hosp": "Boston Pilgrim Hospital", "desc": "Pilgrim Hospital acute base" },
                { "stage": "Aug 27 - Feb 28 (6m)", "hosp": "Boston Pilgrim Hospital", "desc": "Pilgrim Hospital - IAC completion" },
                { "stage": "Feb 28 - Aug 28 (6m)", "hosp": "Lincoln County Hospital", "desc": "Lincoln acute placement" },
                { "stage": "Aug 28 - Feb 29 (6m)", "hosp": "Queen's Medical Centre (QMC), Nottingham", "desc": "Major Trauma Centre placement" },
                { "stage": "Feb 29 - Aug 29 (6m)", "hosp": "Queen's Medical Centre (QMC), Nottingham", "desc": "MTC & specialist surgery" },
                { "stage": "Aug 29 - Feb 30 (6m)", "hosp": "Nottingham City Hospital", "desc": "Elective & specialist modules" }
            ]
        },
        {
            "id": "ct1-east-midlands-north-2e",
            "code": csv_rows[73]["Preference"],
            "region": "East Midlands",
            "title": "Boston Pilgrim Hospital Starting Post (2E)",
            "places": csv_rows[73]["Places Available"],
            "hubs": {
                "driver": { "name": "Boston / Sibsey", "coords": [52.9950, -0.0150], "desc": "5m drive to Boston Pilgrim Hospital.", "alert": "Direct parking on the Pilgrim Hospital campus." },
                "transit": { "name": "Boston Station (Lincs)", "coords": [52.9780, -0.0280], "desc": "Buses connect Boston rail station to Pilgrim Hospital.", "alert": "Short bus ride or cycle from Boston town centre." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Boston Pilgrim Hospital", "desc": "Starting site - Boston Pilgrim Hospital" }
            ]
        },
        {
            "id": "ct1-east-midlands-north-3",
            "code": csv_rows[74]["Preference"],
            "region": "East Midlands",
            "title": "Notts (N1F27): King's Mill, QMC & Nottingham City",
            "places": csv_rows[74]["Places Available"],
            "hubs": {
                "driver": { "name": "Hucknall / Ravenshead (A60 / A611)", "coords": [53.0350, -1.1850], "desc": "Corridor midway. 15m north to King's Mill; 18m south to Nottingham hospitals.", "alert": "Easy driving links north and south via the A60/A611." },
                "transit": { "name": "Hucknall Tram / Robin Hood Line", "coords": [53.0350, -1.2050], "desc": "Robin Hood Line train to Mansfield/Sutton Parkway; NET Tram direct to QMC.", "alert": "NET Tram connects directly from Hucknall into the QMC campus." }
            },
            "stages": [
                { "stage": "Feb 27 - Aug 27 (6m)", "hosp": "Kings Mill Hospital, Mansfield", "desc": "King's Mill acute base" },
                { "stage": "Aug 27 - Feb 28 (6m)", "hosp": "Kings Mill Hospital, Mansfield", "desc": "King's Mill - IAC completion" },
                { "stage": "Feb 28 - Aug 28 (6m)", "hosp": "Queen's Medical Centre (QMC), Nottingham", "desc": "Major Trauma Centre placement" },
                { "stage": "Aug 28 - Feb 29 (6m)", "hosp": "Queen's Medical Centre (QMC), Nottingham", "desc": "MTC & specialist anaesthesia" },
                { "stage": "Feb 29 - Aug 29 (6m)", "hosp": "Nottingham City Hospital", "desc": "Elective & specialist modules" },
                { "stage": "Aug 29 - Feb 30 (6m)", "hosp": "Kings Mill Hospital, Mansfield", "desc": "King's Mill Stage 1 completion" }
            ]
        },
        {
            "id": "ct1-east-midlands-north-3e",
            "code": csv_rows[75]["Preference"],
            "region": "East Midlands",
            "title": "Nottingham University Hospitals Starting Post (3E)",
            "places": csv_rows[75]["Places Available"],
            "hubs": {
                "driver": { "name": "Wollaton / Beeston", "coords": [52.9350, -1.2150], "desc": "5-10m drive to QMC; 15m to City Hospital via ring road.", "alert": "QMC has a dedicated NET tram stop on campus." },
                "transit": { "name": "Nottingham Station / NET Tram", "coords": [52.9470, -1.1460], "desc": "NET Tram connects Nottingham station directly to QMC in 12m.", "alert": "Tram stops right inside Queen's Medical Centre." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Queen's Medical Centre (QMC), Nottingham", "desc": "Starting trust - Nottingham University Hospitals (QMC & City)" },
                { "stage": "CT1 (12m)", "hosp": "Nottingham City Hospital", "desc": "NUH Trust campus alternative" }
            ]
        },
        {
            "id": "ct1-east-midlands-north-8",
            "code": csv_rows[76]["Preference"],
            "region": "East Midlands",
            "title": "Derbyshire (D3 F27): Derby, Burton & Chesterfield",
            "places": csv_rows[76]["Places Available"],
            "hubs": {
                "driver": { "name": "Derby North / Ripley (A38)", "coords": [52.9750, -1.4550], "desc": "A38 corridor. 12m south to Royal Derby, 22m to Burton; 22m north to Chesterfield via A38/A61.", "alert": "A38 dual carriageway provides direct links across Derbyshire." },
                "transit": { "name": "Derby Midland Station", "coords": [52.9160, -1.4630], "desc": "Direct rail south to Burton (10m) and north to Chesterfield (18m).", "alert": "Frequent fast trains connect Derby, Burton and Chesterfield." }
            },
            "stages": [
                { "stage": "Feb 27 - Aug 27 (6m)", "hosp": "Royal Derby Hospital", "desc": "Royal Derby acute base" },
                { "stage": "Aug 27 - Feb 28 (6m)", "hosp": "Royal Derby Hospital", "desc": "Royal Derby - IAC completion" },
                { "stage": "Feb 28 - Aug 28 (6m)", "hosp": "Queen's Hospital, Burton", "desc": "Queen's Hospital Burton placement" },
                { "stage": "Aug 28 - Feb 29 (6m)", "hosp": "Queen's Hospital, Burton", "desc": "Burton acute & general placement" },
                { "stage": "Feb 29 - Aug 29 (6m)", "hosp": "Chesterfield Royal Hospital", "desc": "Chesterfield acute placement" },
                { "stage": "Aug 29 - Feb 30 (6m)", "hosp": "Chesterfield Royal Hospital", "desc": "Chesterfield Stage 1 completion" }
            ]
        },
        {
            "id": "ct1-east-midlands-north-9",
            "code": csv_rows[77]["Preference"],
            "region": "East Midlands",
            "title": "Derbyshire (D19 F27): Chesterfield, Derby & Burton",
            "places": csv_rows[77]["Places Available"],
            "hubs": {
                "driver": { "name": "Derby North / Ripley (A38)", "coords": [52.9750, -1.4550], "desc": "A38 corridor. 12m south to Royal Derby, 22m to Burton; 22m north to Chesterfield via A38/A61.", "alert": "A38 dual carriageway provides direct links across Derbyshire." },
                "transit": { "name": "Derby Midland Station", "coords": [52.9160, -1.4630], "desc": "Direct rail south to Burton (10m) and north to Chesterfield (18m).", "alert": "Frequent fast trains connect Derby, Burton and Chesterfield." }
            },
            "stages": [
                { "stage": "Feb 27 - Aug 27 (6m)", "hosp": "Chesterfield Royal Hospital", "desc": "Chesterfield acute base" },
                { "stage": "Aug 27 - Feb 28 (6m)", "hosp": "Chesterfield Royal Hospital", "desc": "Chesterfield - IAC completion" },
                { "stage": "Feb 28 - Aug 28 (6m)", "hosp": "Royal Derby Hospital", "desc": "Royal Derby acute placement" },
                { "stage": "Aug 28 - Feb 29 (6m)", "hosp": "Royal Derby Hospital", "desc": "Royal Derby general anaesthesia" },
                { "stage": "Feb 29 - Aug 29 (6m)", "hosp": "Queen's Hospital, Burton", "desc": "Queen's Hospital Burton placement" },
                { "stage": "Aug 29 - Feb 30 (6m)", "hosp": "Queen's Hospital, Burton", "desc": "Burton Stage 1 completion" }
            ]
        },
        {
            "id": "ct1-east-midlands-south-4",
            "code": csv_rows[78]["Preference"],
            "region": "East Midlands",
            "title": "East Midlands South (27R): Leicester & Northampton",
            "places": csv_rows[78]["Places Available"],
            "hubs": market_harborough_hubs,
            "stages": south_stages_leic_first
        },
        {
            "id": "ct1-east-midlands-south-5",
            "code": csv_rows[79]["Preference"],
            "region": "East Midlands",
            "title": "East Midlands South (27S): Leicester & Northampton",
            "places": csv_rows[79]["Places Available"],
            "hubs": market_harborough_hubs,
            "stages": south_stages_leic_first
        },
        {
            "id": "ct1-east-midlands-south-6",
            "code": csv_rows[80]["Preference"],
            "region": "East Midlands",
            "title": "East Midlands South (27T): Leicester & Northampton",
            "places": csv_rows[80]["Places Available"],
            "hubs": market_harborough_hubs,
            "stages": south_stages_leic_first
        },
        {
            "id": "ct1-east-midlands-south-7",
            "code": csv_rows[81]["Preference"],
            "region": "East Midlands",
            "title": "East Midlands South (27U): Northampton & Leicester",
            "places": csv_rows[81]["Places Available"],
            "hubs": market_harborough_hubs,
            "stages": south_stages_northampton_first
        }
    ]
