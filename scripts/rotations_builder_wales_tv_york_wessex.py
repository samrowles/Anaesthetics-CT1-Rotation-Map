def get_wales_rotations(csv_rows):
    return [
        {
            "id": "ct1-wales-south-7",
            "code": csv_rows[5]["Preference"],
            "region": "Wales",
            "title": "Cardiff (UHW 24m) & Bridgend (12m)",
            "places": csv_rows[5]["Places Available"],
            "hubs": {
                "driver": { "name": "Cardiff West / Cowbridge", "coords": [51.4850, -3.3550], "desc": "M4 J33/J34 corridor. 18m to UHW Cardiff; 16m to Princess of Wales Bridgend.", "alert": "M4 corridor makes commuting easy between Cardiff and Bridgend." },
                "transit": { "name": "Cardiff Central / Bridgend Station", "coords": [51.4750, -3.1780], "desc": "Direct fast trains between Cardiff Central and Bridgend (20m).", "alert": "UHW requires bus from Cardiff Central; Bridgend station has local buses to hospital." }
            },
            "stages": [
                { "stage": "CT1 - CT2 (24m)", "hosp": "University Hospital of Wales, Cardiff", "desc": "Tertiary Major Trauma Centre & teaching base" },
                { "stage": "CT3 (12m)", "hosp": "Princess of Wales Hospital, Bridgend", "desc": "District general acute base" }
            ]
        },
        {
            "id": "ct1-wales-south-4",
            "code": csv_rows[26]["Preference"],
            "region": "Wales",
            "title": "Bridgend (24m) & Cwmbran (Grange 12m)",
            "places": csv_rows[26]["Places Available"],
            "hubs": {
                "driver": { "name": "Cardiff North / M4 J30-32", "coords": [51.5280, -3.2150], "desc": "Equidistant on M4 corridor. 25m west to Bridgend; 22m northeast to Grange Cwmbran.", "alert": "Cardiff North provides central positioning along the M4." },
                "transit": { "name": "Newport / Cardiff Central", "coords": [51.5880, -2.9980], "desc": "Rail connections along South Wales mainline.", "alert": "Grange Hospital is rural off Cwmbran; car recommended for early shifts." }
            },
            "stages": [
                { "stage": "CT1 - CT2 (24m)", "hosp": "Princess of Wales Hospital, Bridgend", "desc": "District general acute base" },
                { "stage": "CT3 (12m)", "hosp": "Grange University Hospital, Cwmbran", "desc": "Specialist Critical Care Centre" }
            ]
        },
        {
            "id": "ct1-wales-south-2",
            "code": csv_rows[37]["Preference"],
            "region": "Wales",
            "title": "Cwmbran (Grange 24m) & Merthyr Tydfil (12m)",
            "places": csv_rows[37]["Places Available"],
            "hubs": {
                "driver": { "name": "Pontypool / Abergavenny / A465", "coords": [51.7250, -3.0550], "desc": "A465 Heads of the Valleys corridor. 20m south to Grange; 25m west to Merthyr.", "alert": "New A465 dual carriageway provides fast links between valleys." },
                "transit": { "name": "Cwmbran / Abergavenny", "coords": [51.6550, -3.0180], "desc": "Welsh Marches line rail links.", "alert": "Valley terrain makes public transit between these two sites slow; car strongly recommended." }
            },
            "stages": [
                { "stage": "CT1 - CT2 (24m)", "hosp": "Grange University Hospital, Cwmbran", "desc": "Specialist Critical Care Centre" },
                { "stage": "CT3 (12m)", "hosp": "Prince Charles Hospital, Merthyr Tydfil", "desc": "Acute general placement" }
            ]
        },
        {
            "id": "ct1-wales-south-3",
            "code": csv_rows[38]["Preference"],
            "region": "Wales",
            "title": "Cwmbran (Grange 12m) & Merthyr Tydfil (24m)",
            "places": csv_rows[38]["Places Available"],
            "hubs": {
                "driver": { "name": "Pontypool / Abergavenny / A465", "coords": [51.7250, -3.0550], "desc": "A465 Heads of the Valleys corridor. 20m south to Grange; 25m west to Merthyr.", "alert": "New A465 dual carriageway provides fast links between valleys." },
                "transit": { "name": "Cwmbran / Abergavenny", "coords": [51.6550, -3.0180], "desc": "Welsh Marches line rail links.", "alert": "Valley terrain makes public transit between these two sites slow; car strongly recommended." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Grange University Hospital, Cwmbran", "desc": "Specialist Critical Care Centre" },
                { "stage": "CT2 - CT3 (24m)", "hosp": "Prince Charles Hospital, Merthyr Tydfil", "desc": "Acute general placement" }
            ]
        },
        {
            "id": "ct1-wales-south-5",
            "code": csv_rows[41]["Preference"],
            "region": "Wales",
            "title": "Carmarthen (Glangwili 24m) & Swansea (Morriston 12m)",
            "places": csv_rows[41]["Places Available"],
            "hubs": {
                "driver": { "name": "Cross Hands / Llanelli (M4 J49)", "coords": [51.7850, -4.0850], "desc": "M4 terminus / A48 corridor. 18m west to Glangwili; 16m east to Morriston.", "alert": "Cross Hands is the strategic midway base between Carmarthen and Swansea." },
                "transit": { "name": "Carmarthen / Swansea Station", "coords": [51.6210, -3.9420], "desc": "Direct rail between Swansea and Carmarthen (45m).", "alert": "Local buses link stations to hospitals; Morriston is close to M4 J46." }
            },
            "stages": [
                { "stage": "CT1 - CT2 (24m)", "hosp": "Glangwili Hospital, Carmarthen", "desc": "West Wales general acute base" },
                { "stage": "CT3 (12m)", "hosp": "Morriston Hospital, Swansea", "desc": "Major Trauma & Regional Burns/Plastics" }
            ]
        },
        {
            "id": "ct1-wales-south-6",
            "code": csv_rows[42]["Preference"],
            "region": "Wales",
            "title": "Carmarthen (Glangwili 24m) & Swansea (Morriston 12m) (Post 6)",
            "places": csv_rows[42]["Places Available"],
            "hubs": {
                "driver": { "name": "Cross Hands / Llanelli (M4 J49)", "coords": [51.7850, -4.0850], "desc": "M4 terminus / A48 corridor. 18m west to Glangwili; 16m east to Morriston.", "alert": "Cross Hands is the strategic midway base between Carmarthen and Swansea." },
                "transit": { "name": "Carmarthen / Swansea Station", "coords": [51.6210, -3.9420], "desc": "Direct rail between Swansea and Carmarthen (45m).", "alert": "Local buses link stations to hospitals; Morriston is close to M4 J46." }
            },
            "stages": [
                { "stage": "CT1 - CT2 (24m)", "hosp": "Glangwili Hospital, Carmarthen", "desc": "West Wales general acute base" },
                { "stage": "CT3 (12m)", "hosp": "Morriston Hospital, Swansea", "desc": "Major Trauma & Regional Burns/Plastics" }
            ]
        },
        {
            "id": "ct1-wales-north-1",
            "code": csv_rows[69]["Preference"],
            "region": "Wales",
            "title": "North Wales: Bangor (12m) & Rhyl (Glan Clwyd 24m)",
            "places": csv_rows[69]["Places Available"],
            "hubs": {
                "driver": { "name": "Conwy / Llandudno Junction (A55)", "coords": [53.2820, -3.8150], "desc": "A55 North Wales Expressway midway. 20m west to Bangor; 20m east to Glan Clwyd.", "alert": "A55 expressway gives straightforward direct drives to both North Wales sites." },
                "transit": { "name": "Llandudno Junction", "coords": [53.2840, -3.8110], "desc": "Major North Wales railway junction on North Wales Coast Line.", "alert": "Direct trains to Bangor (18m) and Rhyl (15m)." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Ysbyty Gwynedd, Bangor", "desc": "North West Wales acute base" },
                { "stage": "CT2 - CT3 (24m)", "hosp": "Glan Clwyd Hospital, Rhyl", "desc": "Sub-regional trauma & specialist acute base" }
            ]
        }
    ]

def get_thames_valley_rotations(csv_rows):
    return [
        {
            "id": "ct1-thames-valley-oxford-ouh-1",
            "code": csv_rows[15]["Preference"],
            "region": "Thames Valley",
            "title": "Oxford University Hospitals (JR / Horton) CT1 Post",
            "places": csv_rows[15]["Places Available"],
            "hubs": {
                "driver": { "name": "North Oxford / Kidlington (A34 / A4260)", "coords": [51.8250, -1.2850], "desc": "15m south to John Radcliffe; 22m north to Horton Banbury.", "alert": "Strategic location linking both potential Oxford trust hospital sites." },
                "transit": { "name": "Oxford Parkway", "coords": [51.8020, -1.2750], "desc": "Chiltern Railways line to Banbury (18m); bus 700 direct to JR Hospital.", "alert": "Bus 700 connects Oxford Parkway directly to the John Radcliffe." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "John Radcliffe Hospital, Oxford", "desc": "Tertiary teaching & trauma base (or Horton General)" },
                { "stage": "CT1 (12m)", "hosp": "Horton General Hospital, Banbury", "desc": "District general placement alternative" }
            ]
        },
        {
            "id": "ct1-thames-valley-oxford-ouh-1e",
            "code": csv_rows[16]["Preference"],
            "region": "Thames Valley",
            "title": "Oxford (John Radcliffe) 4-Place Track",
            "places": csv_rows[16]["Places Available"],
            "hubs": {
                "driver": { "name": "Headington / Marston", "coords": [51.7650, -1.2150], "desc": "Immediate proximity to John Radcliffe campus.", "alert": "Hospital parking is restricted; cycling or Park & Ride widely used." },
                "transit": { "name": "Oxford City Centre / Thornhill P&R", "coords": [51.7550, -1.1850], "desc": "Frequent hospital buses (700, 8, 9, 280) serve the Headington hospitals.", "alert": "Thornhill Park & Ride provides fast dedicated buses to JR." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "John Radcliffe Hospital, Oxford", "desc": "Oxford University Hospitals NHS Trust base (Years 2 & 3 TBC)" }
            ]
        },
        {
            "id": "ct1-thames-valley-royal-berkshire-3",
            "code": csv_rows[27]["Preference"],
            "region": "Thames Valley",
            "title": "Reading (Royal Berkshire) CT1 Post",
            "places": csv_rows[27]["Places Available"],
            "hubs": {
                "driver": { "name": "Reading Central / Earley", "coords": [51.4450, -0.9550], "desc": "5-10m drive to Royal Berkshire Hospital; easy access from M4 J10/J11.", "alert": "Town centre hospital with staff permit parking." },
                "transit": { "name": "Reading Station", "coords": [51.4580, -0.9720], "desc": "Major Great Western / Elizabeth Line interchange; 15m walk or bus to RBH.", "alert": "Frequent buses (3, 9, 17) run between station and hospital." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Royal Berkshire Hospital, Reading", "desc": "Royal Berkshire NHS Foundation Trust base (Years 2 & 3 TBC)" }
            ]
        },
        {
            "id": "ct1-thames-valley-buckinghamshire-2",
            "code": csv_rows[28]["Preference"],
            "region": "Thames Valley",
            "title": "Bucks: Stoke Mandeville & Wycombe (4 Places)",
            "places": csv_rows[28]["Places Available"],
            "hubs": {
                "driver": { "name": "Princes Risborough / Great Missenden", "coords": [51.7250, -0.8250], "desc": "A4010 corridor. 15m north to Stoke Mandeville; 18m south to Wycombe.", "alert": "A4010 links Aylesbury and High Wycombe directly across the Chilterns." },
                "transit": { "name": "Aylesbury / High Wycombe", "coords": [51.8150, -0.8150], "desc": "Chiltern Railways and Arriva 300 bus connects Aylesbury and High Wycombe.", "alert": "Arriva 300 bus connects Stoke Mandeville and Wycombe hospital sites." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Stoke Mandeville Hospital, Aylesbury", "desc": "Bucks Healthcare NHS Trust base (National Spinal & Acute)" },
                { "stage": "CT1 (12m)", "hosp": "Wycombe Hospital, High Wycombe", "desc": "Elective surgical & outpatient base" }
            ]
        }
    ]

def get_yorkshire_rotations(csv_rows):
    return [
        {
            "id": "ct1-yorkshire-south-2e",
            "code": csv_rows[17]["Preference"],
            "region": "Yorkshire and the Humber",
            "title": "South Yorkshire 6-Monthly Rotations (2E)",
            "places": csv_rows[17]["Places Available"],
            "hubs": {
                "driver": { "name": "Sheffield North / Meadowhall (M1 J34)", "coords": [53.4150, -1.4150], "desc": "M1 corridor. 12m to Northern General, 15m to Rotherham, 25m to Barnsley.", "alert": "Strategic location linking Sheffield and Rotherham hospitals." },
                "transit": { "name": "Meadowhall Interchange", "coords": [53.4170, -1.4120], "desc": "Supertram into central Sheffield; direct trains to Rotherham, Barnsley, Doncaster.", "alert": "Excellent multi-modal transport hub for South Yorkshire." }
            },
            "stages": [
                { "stage": "CT1 - CT3", "hosp": "Northern General Hospital, Sheffield", "desc": "Major Trauma Centre & Sheffield Teaching Hospitals" },
                { "stage": "CT1 - CT3", "hosp": "Rotherham Hospital", "desc": "District general acute placement" },
                { "stage": "CT1 - CT3", "hosp": "Doncaster Royal Infirmary", "desc": "Acute Doncaster base" },
                { "stage": "CT1 - CT3", "hosp": "Barnsley Hospital", "desc": "Acute Barnsley base" }
            ]
        },
        {
            "id": "ct1-yorkshire-south-3",
            "code": csv_rows[18]["Preference"],
            "region": "Yorkshire and the Humber",
            "title": "South Yorkshire Network (Barnsley, Doncaster, Sheffield, Rotherham)",
            "places": csv_rows[18]["Places Available"],
            "hubs": {
                "driver": { "name": "Rotherham / M1 J33/J34", "coords": [53.4320, -1.3550], "desc": "Equidistant across South Yorkshire footprint via M1 and M18.", "alert": "M18 provides rapid transit east to Doncaster." },
                "transit": { "name": "Sheffield / Meadowhall", "coords": [53.3780, -1.4620], "desc": "Central rail connections across the South Yorkshire region.", "alert": "Rail lines run directly from Sheffield to Barnsley and Doncaster." }
            },
            "stages": [
                { "stage": "CT1 - CT3", "hosp": "Northern General Hospital, Sheffield", "desc": "Sheffield base" },
                { "stage": "CT1 - CT3", "hosp": "Doncaster Royal Infirmary", "desc": "Doncaster base" },
                { "stage": "CT1 - CT3", "hosp": "Barnsley Hospital", "desc": "Barnsley base" },
                { "stage": "CT1 - CT3", "hosp": "Rotherham Hospital", "desc": "Rotherham base" },
                { "stage": "CT1 - CT3", "hosp": "Bassetlaw Hospital, Worksop", "desc": "Worksop placement" }
            ]
        },
        {
            "id": "ct1-yorkshire-west-4",
            "code": csv_rows[19]["Preference"],
            "region": "Yorkshire and the Humber",
            "title": "West Yorkshire Core Network (Leeds, Bradford, Airedale, Calderdale)",
            "places": csv_rows[19]["Places Available"],
            "hubs": {
                "driver": { "name": "Leeds West / Pudsey (Ring Road / M621)", "coords": [53.7950, -1.6650], "desc": "Strategic nexus between Leeds (15m), Bradford (15m), and M62 towards Calderdale/Wakefield.", "alert": "Pudsey/Bramley gives balanced access east and west." },
                "transit": { "name": "Leeds Central", "coords": [53.7950, -1.5470], "desc": "Dense commuter rail network: 18m to Bradford, 15m to Wakefield, 25m to Halifax.", "alert": "Fast local trains connect West Yorkshire towns efficiently." }
            },
            "stages": [
                { "stage": "CT1 - CT3", "hosp": "Leeds General Infirmary", "desc": "Leeds Teaching Hospitals base" },
                { "stage": "CT1 - CT3", "hosp": "Bradford Royal Infirmary", "desc": "Bradford acute base" },
                { "stage": "CT1 - CT3", "hosp": "Pinderfields Hospital, Wakefield", "desc": "Mid Yorkshire Trust base" },
                { "stage": "CT1 - CT3", "hosp": "Calderdale Royal Hospital, Halifax", "desc": "Calderdale & Huddersfield Trust" },
                { "stage": "CT1 - CT3", "hosp": "Airedale General Hospital, Steeton", "desc": "Airedale acute base" },
                { "stage": "CT1 - CT3", "hosp": "Harrogate District Hospital", "desc": "Harrogate general base" }
            ]
        },
        {
            "id": "ct1-yorkshire-west-1e",
            "code": csv_rows[20]["Preference"],
            "region": "Yorkshire and the Humber",
            "title": "West Yorkshire 6-Monthly Rotations (1E)",
            "places": csv_rows[20]["Places Available"],
            "hubs": {
                "driver": { "name": "Leeds West / Pudsey (Ring Road / M621)", "coords": [53.7950, -1.6650], "desc": "Strategic nexus between Leeds (15m), Bradford (15m), and M62 towards Calderdale/Wakefield.", "alert": "Pudsey/Bramley gives balanced access east and west." },
                "transit": { "name": "Leeds Central", "coords": [53.7950, -1.5470], "desc": "Dense commuter rail network: 18m to Bradford, 15m to Wakefield, 25m to Halifax.", "alert": "Fast local trains connect West Yorkshire towns efficiently." }
            },
            "stages": [
                { "stage": "CT1 - CT3", "hosp": "Leeds General Infirmary", "desc": "Leeds Teaching Hospitals base" },
                { "stage": "CT1 - CT3", "hosp": "Bradford Royal Infirmary", "desc": "Bradford acute base" },
                { "stage": "CT1 - CT3", "hosp": "Pinderfields Hospital, Wakefield", "desc": "Mid Yorkshire Trust base" },
                { "stage": "CT1 - CT3", "hosp": "Calderdale Royal Hospital, Halifax", "desc": "Calderdale & Huddersfield Trust" },
                { "stage": "CT1 - CT3", "hosp": "Airedale General Hospital, Steeton", "desc": "Airedale acute base" },
                { "stage": "CT1 - CT3", "hosp": "Harrogate District Hospital", "desc": "Harrogate general base" }
            ]
        },
        {
            "id": "ct1-yorkshire-north-1",
            "code": csv_rows[21]["Preference"],
            "region": "Yorkshire and the Humber",
            "title": "North Yorkshire: York, Scarborough & Harrogate",
            "places": csv_rows[21]["Places Available"],
            "hubs": {
                "driver": { "name": "York Ring Road / Malton (A64)", "coords": [53.9950, -1.0550], "desc": "A64 corridor. 10m into York Hospital; 45m to Scarborough; 35m west to Harrogate via A59.", "alert": "Scarborough is on the East Coast (~40 mi from York via A64)." },
                "transit": { "name": "York Station", "coords": [53.9580, -1.0930], "desc": "Direct trains to Harrogate (30m) and Scarborough (48m).", "alert": "York station is a major hub with direct lines to both Harrogate and Scarborough." }
            },
            "stages": [
                { "stage": "CT1 - CT3", "hosp": "York Hospital", "desc": "York Teaching Hospital base" },
                { "stage": "CT1 - CT3", "hosp": "Harrogate District Hospital", "desc": "Harrogate District acute base" },
                { "stage": "CT1 - CT3", "hosp": "Scarborough Hospital", "desc": "East Coast general base" }
            ]
        },
        {
            "id": "ct1-yorkshire-east-2",
            "code": csv_rows[55]["Preference"],
            "region": "Yorkshire and the Humber",
            "title": "East Yorkshire & Humber: Hull, Scunthorpe & Grimsby",
            "places": csv_rows[55]["Places Available"],
            "hubs": {
                "driver": { "name": "Hessle / Humber Bridge (A15)", "coords": [53.7150, -0.4450], "desc": "Immediate access to Humber Bridge. 12m to Hull Royal; 25m south to Scunthorpe; 35m to Grimsby.", "alert": "Humber Bridge connects north and south banks seamlessly (£1.50 toll)." },
                "transit": { "name": "Hull Paragon Interchange", "coords": [53.7440, -0.3440], "desc": "Rail connections across Humberside.", "alert": "Cross-Humber public transit is limited; car strongly recommended." }
            },
            "stages": [
                { "stage": "CT1 - CT3", "hosp": "Hull Royal Infirmary", "desc": "Tertiary Major Trauma Centre" },
                { "stage": "CT1 - CT3", "hosp": "Scunthorpe General Hospital", "desc": "Northern Lincolnshire acute base" },
                { "stage": "CT1 - CT3", "hosp": "Diana, Princess of Wales Hospital, Grimsby", "desc": "Grimsby acute general base" },
                { "stage": "CT1 - CT3", "hosp": "Goole and District Hospital", "desc": "Goole elective base" }
            ]
        },
        {
            "id": "ct1-yorkshire-east-5e",
            "code": csv_rows[56]["Preference"],
            "region": "Yorkshire and the Humber",
            "title": "East Yorkshire 6-Monthly Rotations (5E)",
            "places": csv_rows[56]["Places Available"],
            "hubs": {
                "driver": { "name": "Hessle / Humber Bridge (A15)", "coords": [53.7150, -0.4450], "desc": "Immediate access to Humber Bridge. 12m to Hull Royal; 25m south to Scunthorpe; 35m to Grimsby.", "alert": "Humber Bridge connects north and south banks seamlessly (£1.50 toll)." },
                "transit": { "name": "Hull Paragon Interchange", "coords": [53.7440, -0.3440], "desc": "Rail connections across Humberside.", "alert": "Cross-Humber public transit is limited; car strongly recommended." }
            },
            "stages": [
                { "stage": "CT1 - CT3", "hosp": "Hull Royal Infirmary", "desc": "Tertiary Major Trauma Centre" },
                { "stage": "CT1 - CT3", "hosp": "Scunthorpe General Hospital", "desc": "Northern Lincolnshire acute base" },
                { "stage": "CT1 - CT3", "hosp": "Diana, Princess of Wales Hospital, Grimsby", "desc": "Grimsby acute general base" },
                { "stage": "CT1 - CT3", "hosp": "Goole and District Hospital", "desc": "Goole elective base" }
            ]
        }
    ]

def get_wessex_rotations(csv_rows):
    stages = [
        { "stage": "CT1 - CT3", "hosp": "Southampton General Hospital", "desc": "Regional MTC & Specialist Cardiac/Neuro Centre" },
        { "stage": "CT1 - CT3", "hosp": "Queen Alexandra Hospital, Portsmouth", "desc": "Major Acute & Vascular Centre" },
        { "stage": "CT1 - CT3", "hosp": "Royal Hampshire County Hospital, Winchester", "desc": "Elective Orthopaedics & General" },
        { "stage": "CT1 - CT3", "hosp": "Basingstoke & North Hampshire Hospital", "desc": "DGH Anaesthesia & Critical Care" },
        { "stage": "CT1 - CT3", "hosp": "Poole Hospital", "desc": "Acute District General Placement" },
        { "stage": "CT1 - CT3", "hosp": "Royal Bournemouth Hospital", "desc": "Major Elective Centre" },
        { "stage": "CT1 - CT3", "hosp": "Salisbury District Hospital", "desc": "Regional Burns & Plastics" },
        { "stage": "CT1 - CT3", "hosp": "Dorset County Hospital, Dorchester", "desc": "DGH Anaesthesia" }
    ]
    return [
        {
            "id": "ct1-wessex-1",
            "code": csv_rows[22]["Preference"],
            "region": "Wessex",
            "title": "Wessex Core Anaesthetics Scheme (8 Places)",
            "places": csv_rows[22]["Places Available"],
            "hubs": {
                "driver": { "name": "Winchester / Eastleigh (M3/M27)", "coords": [51.0250, -1.3350], "desc": "Central Wessex hub. 18m to Southampton, 28m to Portsmouth, 22m to Basingstoke.", "alert": "Premier driving base for the Wessex training network." },
                "transit": { "name": "Eastleigh / Southampton Central", "coords": [50.9680, -1.3530], "desc": "Direct rail to Winchester (12m), Basingstoke (22m), and Portsmouth (40m).", "alert": "Frequent train services along the South Coast rail line." }
            },
            "stages": stages
        },
        {
            "id": "ct1-wessex-1e",
            "code": csv_rows[23]["Preference"],
            "region": "Wessex",
            "title": "Wessex Core Anaesthetics Scheme (1E)",
            "places": csv_rows[23]["Places Available"],
            "hubs": {
                "driver": { "name": "Winchester / Eastleigh (M3/M27)", "coords": [51.0250, -1.3350], "desc": "Central Wessex hub. 18m to Southampton, 28m to Portsmouth, 22m to Basingstoke.", "alert": "Premier driving base for the Wessex training network." },
                "transit": { "name": "Eastleigh / Southampton Central", "coords": [50.9680, -1.3530], "desc": "Direct rail to Winchester (12m), Basingstoke (22m), and Portsmouth (40m).", "alert": "Frequent train services along the South Coast rail line." }
            },
            "stages": stages
        }
    ]
