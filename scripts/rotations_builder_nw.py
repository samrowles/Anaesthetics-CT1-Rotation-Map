def get_north_west_rotations(csv_rows):
    mcr_stages = [
        { "stage": "CT1 - CT3", "hosp": "Manchester Royal Infirmary", "desc": "Central Manchester Teaching Hospitals" },
        { "stage": "CT1 - CT3", "hosp": "Salford Royal Hospital", "desc": "Regional Major Trauma & Neuro Centre" },
        { "stage": "CT1 - CT3", "hosp": "Wythenshawe Hospital, Manchester", "desc": "Regional Cardiothoracics & Burns" },
        { "stage": "CT1 - CT3", "hosp": "Royal Bolton Hospital", "desc": "Acute DGH Base" },
        { "stage": "CT1 - CT3", "hosp": "Stepping Hill Hospital, Stockport", "desc": "Stockport Acute Base" }
    ]

    return [
        {
            "id": "ct1-north-west-greater-manchester-9",
            "code": csv_rows[29]["Preference"],
            "region": "North West",
            "title": "Greater Manchester Anaesthesia Scheme (13 Places)",
            "places": csv_rows[29]["Places Available"],
            "hubs": {
                "driver": { "name": "Sale / Altrincham / M60 J6-8", "coords": [53.4250, -2.3150], "desc": "M60 orbital motorway access: 15m to Wythenshawe, 18m to Salford Royal, 20m to MRI.", "alert": "M60 ring road provides rapid connections across Greater Manchester." },
                "transit": { "name": "Manchester Piccadilly / Metrolink", "coords": [53.4770, -2.2310], "desc": "Extensive Metrolink tram network and local rail connecting all Manchester hospitals.", "alert": "Metrolink connects directly to Salford Royal and Wythenshawe." }
            },
            "stages": mcr_stages
        },
        {
            "id": "ct1-north-west-greater-manchester-2e",
            "code": csv_rows[30]["Preference"],
            "region": "North West",
            "title": "Greater Manchester Anaesthesia Scheme (2E)",
            "places": csv_rows[30]["Places Available"],
            "hubs": {
                "driver": { "name": "Sale / Altrincham / M60 J6-8", "coords": [53.4250, -2.3150], "desc": "M60 orbital motorway access: 15m to Wythenshawe, 18m to Salford Royal, 20m to MRI.", "alert": "M60 ring road provides rapid connections across Greater Manchester." },
                "transit": { "name": "Manchester Piccadilly / Metrolink", "coords": [53.4770, -2.2310], "desc": "Extensive Metrolink tram network and local rail connecting all Manchester hospitals.", "alert": "Metrolink connects directly to Salford Royal and Wythenshawe." }
            },
            "stages": mcr_stages
        },
        {
            "id": "ct1-north-west-cheshire-merseyside-11",
            "code": csv_rows[58]["Preference"],
            "region": "North West",
            "title": "Warrington (12m), Royal Liverpool (9m) & LWH (3m)",
            "places": csv_rows[58]["Places Available"],
            "hubs": {
                "driver": { "name": "Widnes / Rainhill (M62 J7)", "coords": [53.4350, -2.7650], "desc": "M62 corridor midway. 15m east to Warrington; 20m west to Liverpool hospitals.", "alert": "M62 motorway provides fast dual-direction commutes." },
                "transit": { "name": "Liverpool Lime Street / Warrington Central", "coords": [53.4070, -2.9770], "desc": "Direct fast rail between Liverpool Lime St and Warrington (25m).", "alert": "Trains run frequently between Liverpool and Warrington." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Warrington Hospital", "desc": "Warrington general acute base" },
                { "stage": "CT2 (9m)", "hosp": "Royal Liverpool University Hospital", "desc": "Tertiary adult acute anaesthesia" },
                { "stage": "CT3 (3m)", "hosp": "Liverpool Women's Hospital (LWH)", "desc": "Obstetric anaesthesia module" }
            ]
        },
        {
            "id": "ct1-north-west-cheshire-merseyside-10",
            "code": csv_rows[59]["Preference"],
            "region": "North West",
            "title": "Whiston (12m) & Warrington (12m)",
            "places": csv_rows[59]["Places Available"],
            "hubs": {
                "driver": { "name": "Rainhill / St Helens South (M62 J7)", "coords": [53.4150, -2.7550], "desc": "8m west to Whiston Hospital; 12m east to Warrington Hospital.", "alert": "Short, easy commutes between adjacent trusts." },
                "transit": { "name": "Rainhill Station", "coords": [53.4180, -2.7550], "desc": "Direct rail on the historic Liverpool-Manchester line to Whiston and Warrington.", "alert": "Local rail links are very convenient along this corridor." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Whiston Hospital, Prescot", "desc": "Whiston acute general base" },
                { "stage": "CT2 (6m)", "hosp": "Warrington Hospital", "desc": "Intensive Care Medicine placement" },
                { "stage": "CT2 (6m)", "hosp": "Warrington Hospital", "desc": "Theatres anaesthesia placement" }
            ]
        },
        {
            "id": "ct1-north-west-cheshire-merseyside-4",
            "code": csv_rows[60]["Preference"],
            "region": "North West",
            "title": "Southport (12m) & Royal Liverpool (12m)",
            "places": csv_rows[60]["Places Available"],
            "hubs": {
                "driver": { "name": "Formby / Crosby (A565)", "coords": [53.5350, -3.0650], "desc": "Coastal corridor midway. 15m north to Southport; 22m south to central Liverpool.", "alert": "A565 connects Southport straight into Liverpool city centre." },
                "transit": { "name": "Merseyrail Northern Line (Formby)", "coords": [53.5550, -3.0720], "desc": "Direct Merseyrail trains running every 15m north to Southport and south to Liverpool Central.", "alert": "Merseyrail provides frequent 15-minute train services." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Southport and Formby District General Hospital", "desc": "Southport general acute base" },
                { "stage": "CT2 (6m)", "hosp": "Royal Liverpool University Hospital", "desc": "Intensive Care Medicine module" },
                { "stage": "CT2 (6m)", "hosp": "Royal Liverpool University Hospital", "desc": "General theatres anaesthesia" }
            ]
        },
        {
            "id": "ct1-north-west-cheshire-merseyside-1",
            "code": csv_rows[61]["Preference"],
            "region": "North West",
            "title": "Chester (18m) & Aintree (6m)",
            "places": csv_rows[61]["Places Available"],
            "hubs": {
                "driver": { "name": "Ellesmere Port / Chester North (M53)", "coords": [53.2850, -2.8950], "desc": "M53/M57 corridor. 10m south to Countess of Chester; 25m north to Aintree via Kingsway Tunnel/M57.", "alert": "M53 motorway links Chester directly to Merseyside." },
                "transit": { "name": "Chester Station / Merseyrail", "coords": [53.1970, -2.8790], "desc": "Merseyrail Wirral line to Liverpool Central; connecting Northern line to Aintree.", "alert": "Direct Merseyrail network links Chester into Liverpool." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Countess of Chester Hospital", "desc": "General anaesthesia base" },
                { "stage": "CT2 (6m)", "hosp": "Countess of Chester Hospital", "desc": "Intensive Care Medicine module" },
                { "stage": "CT2 (6m)", "hosp": "Aintree University Hospital, Liverpool", "desc": "Specialist surgery & MTC module" }
            ]
        },
        {
            "id": "ct1-north-west-cheshire-merseyside-8",
            "code": csv_rows[62]["Preference"],
            "region": "North West",
            "title": "Whiston (12m), LWH (3m) & Aintree (9m)",
            "places": csv_rows[62]["Places Available"],
            "hubs": {
                "driver": { "name": "Broadgreen / West Derby (M62/Queens Drive)", "coords": [53.4250, -2.8950], "desc": "Central Merseyside location. 12m east to Whiston, 15m north to Aintree, 10m to LWH.", "alert": "Queens Drive ring road makes reaching all three sites fast." },
                "transit": { "name": "Broadgreen Station / Liverpool", "coords": [53.4080, -2.9050], "desc": "Local city buses and City Line rail services.", "alert": "City buses connect central Liverpool, Whiston and Aintree." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Whiston Hospital, Prescot", "desc": "Whiston general acute base" },
                { "stage": "CT2 (3m)", "hosp": "Liverpool Women's Hospital (LWH)", "desc": "Obstetric anaesthesia placement" },
                { "stage": "CT2 (9m)", "hosp": "Aintree University Hospital, Liverpool", "desc": "Major Trauma & general theatres" }
            ]
        },
        {
            "id": "ct1-north-west-cheshire-merseyside-2",
            "code": csv_rows[63]["Preference"],
            "region": "North West",
            "title": "Crewe (Leighton 18m) & Aintree (6m)",
            "places": csv_rows[63]["Places Available"],
            "hubs": {
                "driver": { "name": "Northwich / Knutsford (M6 J19)", "coords": [53.2650, -2.5150], "desc": "Mid Cheshire. 18m south to Leighton Hospital; 38m north-west to Aintree via M56/M57.", "alert": "Aintree placement in Year 2 involves an M56/M57 motorway commute." },
                "transit": { "name": "Crewe Station", "coords": [53.0890, -2.4330], "desc": "Major rail hub with direct trains to Liverpool Lime Street (38m).", "alert": "Local buses connect from Crewe station to Leighton Hospital." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Leighton Hospital, Crewe", "desc": "General anaesthesia base" },
                { "stage": "CT2 (6m)", "hosp": "Leighton Hospital, Crewe", "desc": "Intensive Care Medicine module" },
                { "stage": "CT2 (6m)", "hosp": "Aintree University Hospital, Liverpool", "desc": "Major Trauma & specialist theatres" }
            ]
        },
        {
            "id": "ct1-north-west-cheshire-merseyside-5",
            "code": csv_rows[64]["Preference"],
            "region": "North West",
            "title": "Southport (12m) & Royal Liverpool (12m) (Post 5)",
            "places": csv_rows[64]["Places Available"],
            "hubs": {
                "driver": { "name": "Formby / Crosby (A565)", "coords": [53.5350, -3.0650], "desc": "Coastal corridor midway. 15m north to Southport; 22m south to central Liverpool.", "alert": "A565 connects Southport straight into Liverpool city centre." },
                "transit": { "name": "Merseyrail Northern Line (Formby)", "coords": [53.5550, -3.0720], "desc": "Direct Merseyrail trains running every 15m north to Southport and south to Liverpool Central.", "alert": "Merseyrail provides frequent 15-minute train services." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Southport and Formby District General Hospital", "desc": "Southport general acute base" },
                { "stage": "CT2 (6m)", "hosp": "Royal Liverpool University Hospital", "desc": "General theatres anaesthesia" },
                { "stage": "CT2 (6m)", "hosp": "Royal Liverpool University Hospital", "desc": "Intensive Care Medicine module" }
            ]
        },
        {
            "id": "ct1-north-west-cheshire-merseyside-6",
            "code": csv_rows[65]["Preference"],
            "region": "North West",
            "title": "Southport (12m) & Aintree (12m)",
            "places": csv_rows[65]["Places Available"],
            "hubs": {
                "driver": { "name": "Maghull / Ormskirk (A59)", "coords": [53.5350, -2.9350], "desc": "A59 corridor midway. 15m north-west to Southport; 12m south to Aintree.", "alert": "Excellent midway position along the A59/A570 corridor." },
                "transit": { "name": "Merseyrail Northern Line (Maghull)", "coords": [53.5150, -2.9350], "desc": "Direct Merseyrail trains south to Aintree station (8m) and connecting bus to Southport.", "alert": "Aintree Hospital is easily reached from Merseyrail station." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Southport and Formby District General Hospital", "desc": "Southport general acute base" },
                { "stage": "CT2 (6m)", "hosp": "Aintree University Hospital, Liverpool", "desc": "General theatres anaesthesia" },
                { "stage": "CT2 (6m)", "hosp": "Aintree University Hospital, Liverpool", "desc": "Intensive Care Medicine module" }
            ]
        },
        {
            "id": "ct1-north-west-cheshire-merseyside-7",
            "code": csv_rows[66]["Preference"],
            "region": "North West",
            "title": "Wirral (12m), LWH (3m) & Crewe (Leighton 9m)",
            "places": csv_rows[66]["Places Available"],
            "hubs": {
                "driver": { "name": "Chester / Ellesmere Port (M53)", "coords": [53.2550, -2.9150], "desc": "Central pivot: 18m north to Arrowe Park Wirral, 20m north to LWH, 28m south-east to Leighton.", "alert": "Central Cheshire/Wirral nexus off M53 J10/12." },
                "transit": { "name": "Chester / Hooton", "coords": [53.3050, -2.9650], "desc": "Merseyrail Wirral Line links into Liverpool and Birkenhead.", "alert": "Leighton placement is easier by car from Cheshire." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Arrowe Park Hospital (Wirral)", "desc": "Wirral University Teaching Hospital base" },
                { "stage": "CT2 (3m)", "hosp": "Liverpool Women's Hospital (LWH)", "desc": "Obstetric anaesthesia placement" },
                { "stage": "CT2 (9m)", "hosp": "Leighton Hospital, Crewe", "desc": "Cheshire acute placement" }
            ]
        },
        {
            "id": "ct1-north-west-cheshire-merseyside-3",
            "code": csv_rows[67]["Preference"],
            "region": "North West",
            "title": "Crewe (Leighton 12m) & Wirral (Arrowe Park 12m)",
            "places": csv_rows[67]["Places Available"],
            "hubs": {
                "driver": { "name": "Chester / Tarporley (A51 / A55)", "coords": [53.1850, -2.7150], "desc": "A51/A55 corridor. 16m east to Leighton Hospital; 25m north-west to Arrowe Park.", "alert": "Scenic Cheshire base connecting both hospital sites." },
                "transit": { "name": "Chester Station", "coords": [53.1970, -2.8790], "desc": "Merseyrail line to Wirral; direct trains east towards Crewe.", "alert": "Direct rail links between Chester and both catchment areas." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Leighton Hospital, Crewe", "desc": "General anaesthesia base" },
                { "stage": "CT2 (6m)", "hosp": "Arrowe Park Hospital (Wirral)", "desc": "General theatres anaesthesia" },
                { "stage": "CT2 (6m)", "hosp": "Arrowe Park Hospital (Wirral)", "desc": "Intensive Care Medicine module" }
            ]
        },
        {
            "id": "ct1-north-west-cheshire-merseyside-1e",
            "code": csv_rows[68]["Preference"],
            "region": "North West",
            "title": "Whiston (18m) & Chester (6m)",
            "places": csv_rows[68]["Places Available"],
            "hubs": {
                "driver": { "name": "Runcorn / Widnes (Mersey Gateway)", "coords": [53.3350, -2.7250], "desc": "Mersey Gateway bridge corridor. 16m north to Whiston; 18m south to Chester via M56/A56.", "alert": "Mersey Gateway bridge makes commuting between Halton, Prescot and Chester very fast." },
                "transit": { "name": "Runcorn Station", "coords": [53.3410, -2.7410], "desc": "Mainline rail to Liverpool and connecting services to Chester.", "alert": "Car is very efficient across the Mersey Gateway." }
            },
            "stages": [
                { "stage": "CT1 - CT2 (18m)", "hosp": "Whiston Hospital, Prescot", "desc": "Whiston acute general base" },
                { "stage": "CT2 (6m)", "hosp": "Countess of Chester Hospital", "desc": "Countess of Chester acute placement" }
            ]
        }
    ]
