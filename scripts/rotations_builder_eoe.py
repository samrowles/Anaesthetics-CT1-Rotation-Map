def get_eoe_rotations(csv_rows):
    return [
        {
            "id": "ct1-eoe-norfolk-norwich-1",
            "code": csv_rows[36]["Preference"],
            "region": "East of England",
            "title": "Norfolk: Norwich (24m) & Great Yarmouth (James Paget 12m)",
            "places": csv_rows[36]["Places Available"],
            "hubs": {
                "driver": { "name": "Acle / Brundall (A47)", "coords": [52.6350, 1.4850], "desc": "A47 corridor midway. 16m west to NNUH Norwich; 15m east to James Paget Gorleston.", "alert": "A47 dual carriageway provides quick links between Norwich and Great Yarmouth." },
                "transit": { "name": "Norwich Station", "coords": [52.6270, 1.3060], "desc": "Direct rail to Great Yarmouth (30m); frequent hospital buses from Norwich station to NNUH.", "alert": "Connecting bus needed from Great Yarmouth station to James Paget." }
            },
            "stages": [
                { "stage": "CT1 - CT2 (24m)", "hosp": "Norfolk & Norwich University Hospital", "desc": "Tertiary teaching and acute base" },
                { "stage": "CT3 (12m)", "hosp": "James Paget Hospital, Great Yarmouth", "desc": "Coastal general acute base" }
            ]
        },
        {
            "id": "ct1-eoe-essex-chelmsford-8",
            "code": csv_rows[43]["Preference"],
            "region": "East of England",
            "title": "Essex: Chelmsford (Broomfield 24m) & Harlow (12m)",
            "places": csv_rows[43]["Places Available"],
            "hubs": {
                "driver": { "name": "Great Dunmow / Stansted / A120", "coords": [51.8750, 0.3650], "desc": "A120 / A414 corridor. 22m south-east to Broomfield; 20m south-west to Harlow.", "alert": "A120 and A414 give rural cross-county connections between Chelmsford and Harlow." },
                "transit": { "name": "Chelmsford / Harlow Town", "coords": [51.7370, 0.4680], "desc": "Direct Greater Anglia rail lines to London; local bus connections.", "alert": "East-west public transport between Chelmsford and Harlow is bus-based; car recommended." }
            },
            "stages": [
                { "stage": "CT1 - CT2 (24m)", "hosp": "Broomfield Hospital, Chelmsford", "desc": "Mid Essex acute & plastic surgery base" },
                { "stage": "CT3 (12m)", "hosp": "Princess Alexandra Hospital, Harlow", "desc": "West Essex acute general base" }
            ]
        },
        {
            "id": "ct1-eoe-essex-colchester-1e",
            "code": csv_rows[44]["Preference"],
            "region": "East of England",
            "title": "Essex: Colchester Hospital CT1 Post",
            "places": csv_rows[44]["Places Available"],
            "hubs": {
                "driver": { "name": "Colchester North / Mile End (A12)", "coords": [51.9150, 0.8950], "desc": "Immediate access to Colchester Hospital off A12 J28.", "alert": "Direct access off the A12; staff parking on site." },
                "transit": { "name": "Colchester North Station", "coords": [51.9020, 0.8940], "desc": "15m walk or 5m bus ride from Colchester mainline station to hospital.", "alert": "Frequent buses run between station and hospital." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Colchester Hospital", "desc": "East Suffolk & North Essex NHS Foundation Trust base" }
            ]
        },
        {
            "id": "ct1-eoe-bedfordshire-bedford-3e",
            "code": csv_rows[45]["Preference"],
            "region": "East of England",
            "title": "Bedfordshire: Bedford Hospital CT1 Post",
            "places": csv_rows[45]["Places Available"],
            "hubs": {
                "driver": { "name": "Bedford South / Ampthill", "coords": [52.0850, -0.4650], "desc": "5-10m drive to Bedford Hospital; convenient access to A6 and A421.", "alert": "Town centre hospital with staff parking." },
                "transit": { "name": "Bedford Station (Midland)", "coords": [52.1360, -0.4780], "desc": "Thameslink / EMR mainline station; 15m walk to Bedford Hospital South wing.", "alert": "Bedford St Johns station is also nearby." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Bedford Hospital", "desc": "Bedfordshire Hospitals NHS Foundation Trust base" }
            ]
        },
        {
            "id": "ct1-eoe-bedfordshire-bedford-4",
            "code": csv_rows[46]["Preference"],
            "region": "East of England",
            "title": "Bedfordshire: Bedford (24m) & Luton & Dunstable (12m)",
            "places": csv_rows[46]["Places Available"],
            "hubs": {
                "driver": { "name": "Flitwick / Ampthill / Harlington (M1 J12/A6)", "coords": [52.0050, -0.4950], "desc": "Midway on the Bedfordshire corridor. 15m north to Bedford; 16m south to Luton & Dunstable.", "alert": "Flitwick / Ampthill offers a perfect equidistant midpoint on the A6." },
                "transit": { "name": "Flitwick Station (Thameslink)", "coords": [52.0040, -0.4960], "desc": "Direct Thameslink trains north to Bedford (12m) and south to Leagrave/Luton (12m).", "alert": "Thameslink connects directly to both towns." }
            },
            "stages": [
                { "stage": "CT1 - CT2 (24m)", "hosp": "Bedford Hospital", "desc": "Bedford South wing acute base" },
                { "stage": "CT3 (12m)", "hosp": "Luton & Dunstable Hospital", "desc": "Luton & Dunstable acute base" }
            ]
        },
        {
            "id": "ct1-eoe-hertfordshire-watford-6",
            "code": csv_rows[47]["Preference"],
            "region": "East of England",
            "title": "Herts: Watford (24m) & Stevenage (Lister 12m)",
            "places": csv_rows[47]["Places Available"],
            "hubs": {
                "driver": { "name": "St Albans / Hatfield (A414 / M25 J21A)", "coords": [51.7550, -0.3350], "desc": "Central Herts hub. 18m south-west to Watford; 18m north to Lister Stevenage via A1(M).", "alert": "St Albans provides balanced access to both hospital sites." },
                "transit": { "name": "St Albans City / Hatfield", "coords": [51.7500, -0.3250], "desc": "Thameslink rail to St Albans; local buses and rail connections across Herts.", "alert": "Car is generally much faster between Watford and Stevenage." }
            },
            "stages": [
                { "stage": "CT1 - CT2 (24m)", "hosp": "Watford General Hospital", "desc": "West Herts Teaching Hospitals base" },
                { "stage": "CT3 (12m)", "hosp": "Lister Hospital, Stevenage", "desc": "East & North Herts NHS Trust base" }
            ]
        },
        {
            "id": "ct1-eoe-hertfordshire-watford-7",
            "code": csv_rows[48]["Preference"],
            "region": "East of England",
            "title": "Herts: Watford (12m) & Stevenage (Lister 24m)",
            "places": csv_rows[48]["Places Available"],
            "hubs": {
                "driver": { "name": "St Albans / Hatfield (A414 / M25 J21A)", "coords": [51.7550, -0.3350], "desc": "Central Herts hub. 18m south-west to Watford; 18m north to Lister Stevenage via A1(M).", "alert": "St Albans provides balanced access to both hospital sites." },
                "transit": { "name": "St Albans City / Hatfield", "coords": [51.7500, -0.3250], "desc": "Thameslink rail to St Albans; local buses and rail connections across Herts.", "alert": "Car is generally much faster between Watford and Stevenage." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Watford General Hospital", "desc": "West Herts Teaching Hospitals base" },
                { "stage": "CT2 - CT3 (24m)", "hosp": "Lister Hospital, Stevenage", "desc": "East & North Herts NHS Trust base" }
            ]
        },
        {
            "id": "ct1-eoe-essex-harlow-5",
            "code": csv_rows[49]["Preference"],
            "region": "East of England",
            "title": "Essex: Harlow (24m) & Chelmsford (Broomfield 12m)",
            "places": csv_rows[49]["Places Available"],
            "hubs": {
                "driver": { "name": "Great Dunmow / Stansted / A120", "coords": [51.8750, 0.3650], "desc": "A120 / A414 corridor. 22m south-east to Broomfield; 20m south-west to Harlow.", "alert": "A120 and A414 give rural cross-county connections between Chelmsford and Harlow." },
                "transit": { "name": "Chelmsford / Harlow Town", "coords": [51.7370, 0.4680], "desc": "Direct Greater Anglia rail lines to London; local bus connections.", "alert": "East-west public transport between Chelmsford and Harlow is bus-based; car recommended." }
            },
            "stages": [
                { "stage": "CT1 - CT2 (24m)", "hosp": "Princess Alexandra Hospital, Harlow", "desc": "West Essex acute general base" },
                { "stage": "CT3 (12m)", "hosp": "Broomfield Hospital, Chelmsford", "desc": "Mid Essex acute & plastic surgery base" }
            ]
        },
        {
            "id": "ct1-eoe-bedfordshire-luton-3",
            "code": csv_rows[51]["Preference"],
            "region": "East of England",
            "title": "Bedfordshire: Luton & Dunstable (24m) & Bedford (12m)",
            "places": csv_rows[51]["Places Available"],
            "hubs": {
                "driver": { "name": "Flitwick / Ampthill / Harlington (M1 J12/A6)", "coords": [52.0050, -0.4950], "desc": "Midway on the Bedfordshire corridor. 15m north to Bedford; 16m south to Luton & Dunstable.", "alert": "Flitwick / Ampthill offers a perfect equidistant midpoint on the A6." },
                "transit": { "name": "Flitwick Station (Thameslink)", "coords": [52.0040, -0.4960], "desc": "Direct Thameslink trains north to Bedford (12m) and south to Leagrave/Luton (12m).", "alert": "Thameslink connects directly to both towns." }
            },
            "stages": [
                { "stage": "CT1 - CT2 (24m)", "hosp": "Luton & Dunstable Hospital", "desc": "Luton & Dunstable acute base" },
                { "stage": "CT3 (12m)", "hosp": "Bedford Hospital", "desc": "Bedford South wing acute base" }
            ]
        },
        {
            "id": "ct1-eoe-norfolk-kings-lynn-2",
            "code": csv_rows[52]["Preference"],
            "region": "East of England",
            "title": "Norfolk & Cambs: Kings Lynn (24m) & Peterborough (12m)",
            "places": csv_rows[52]["Places Available"],
            "hubs": {
                "driver": { "name": "Wisbech / Guyhirn (A47)", "coords": [52.6550, 0.0550], "desc": "A47 corridor midway. 18m east to Queen Elizabeth Kings Lynn; 22m west to Peterborough City Hospital.", "alert": "A47 provides the direct arterial route between Kings Lynn and Peterborough." },
                "transit": { "name": "Peterborough Station", "coords": [52.5740, -0.2500], "desc": "Major ECML railway interchange; Excel bus connects Peterborough to Kings Lynn.", "alert": "First Excel bus runs between Peterborough rail station and Kings Lynn." }
            },
            "stages": [
                { "stage": "CT1 - CT2 (24m)", "hosp": "Queen Elizabeth Hospital, Kings Lynn", "desc": "Queen Elizabeth Hospital acute base" },
                { "stage": "CT3 (12m)", "hosp": "Peterborough City Hospital", "desc": "Peterborough City acute base" }
            ]
        },
        {
            "id": "ct1-eoe-suffolk-ipswich-2e",
            "code": csv_rows[53]["Preference"],
            "region": "East of England",
            "title": "Suffolk: Ipswich Hospital CT1 Post",
            "places": csv_rows[53]["Places Available"],
            "hubs": {
                "driver": { "name": "Ipswich East / Kesgrave (A12 / A14)", "coords": [52.0650, 1.2250], "desc": "5-10m drive to Ipswich Hospital; easy access to A12 and A14.", "alert": "East Ipswich location with on-site staff parking." },
                "transit": { "name": "Ipswich Station", "coords": [52.0510, 1.1440], "desc": "Frequent buses (66, 66A) link Ipswich railway station directly to Ipswich Hospital.", "alert": "Direct Superroute 66 bus connects station to hospital every 15 mins." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Ipswich Hospital", "desc": "East Suffolk & North Essex NHS Foundation Trust base" }
            ]
        },
        {
            "id": "ct1-eoe-suffolk-ipswich-9",
            "code": csv_rows[54]["Preference"],
            "region": "East of England",
            "title": "Suffolk & Essex: Ipswich (24m) & Colchester (12m)",
            "places": csv_rows[54]["Places Available"],
            "hubs": {
                "driver": { "name": "Manningtree / Stratford St Mary (A12)", "coords": [51.9650, 1.0150], "desc": "A12 corridor midway. 16m north-east to Ipswich Hospital; 14m south-west to Colchester Hospital.", "alert": "A12 dual carriageway provides very fast 15-20m drives to both hospitals." },
                "transit": { "name": "Manningtree Station", "coords": [51.9450, 1.0550], "desc": "Mainline rail station with 10m direct trains to both Colchester and Ipswich.", "alert": "Direct trains link Manningtree to both towns in 10 mins." }
            },
            "stages": [
                { "stage": "CT1 - CT2 (24m)", "hosp": "Ipswich Hospital", "desc": "Ipswich Hospital acute base" },
                { "stage": "CT3 (12m)", "hosp": "Colchester Hospital", "desc": "Colchester Hospital acute base" }
            ]
        }
    ]
