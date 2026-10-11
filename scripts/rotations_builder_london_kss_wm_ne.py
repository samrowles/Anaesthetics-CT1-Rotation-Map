def get_london_rotations(csv_rows):
    return [
        {
            "id": "ct1-london-north-west-lr4",
            "code": csv_rows[31]["Preference"],
            "region": "London",
            "title": "NW London: West Middlesex, Hammersmith & Chelsea",
            "places": csv_rows[31]["Places Available"],
            "hubs": {
                "driver": { "name": "Chiswick / Acton", "coords": [51.4920, -0.2720], "desc": "A4 / M4 / A40 corridor. 15m to West Mid, 12m to Hammersmith, 20m to Chelsea.", "alert": "Public transport strongly recommended across West London." },
                "transit": { "name": "Hammersmith / Turnham Green", "coords": [51.4930, -0.2250], "desc": "District & Piccadilly lines. Direct buses to West Mid (H91), easy tube to Hammersmith & Chelsea.", "alert": "Excellent 24-hr Tube and bus connectivity." }
            },
            "stages": [
                { "stage": "CT1 (Feb 27)", "hosp": "West Middlesex University Hospital", "desc": "Initial Assessment of Competence (IAC) & 3m ICM" },
                { "stage": "CT2 (Feb 28)", "hosp": "Hammersmith Hospital", "desc": "Imperial College Healthcare (QCCH) - IACOA" },
                { "stage": "CT3 (Feb 29)", "hosp": "Chelsea & Westminster Hospital", "desc": "3m ICM, Stage 1 Obs & Paediatric Anaesthesia" }
            ]
        },
        {
            "id": "ct1-london-north-central-lr2",
            "code": csv_rows[32]["Preference"],
            "region": "London",
            "title": "NC London: Romford (BHRUT 2 yrs) & Royal Free (1 yr)",
            "places": csv_rows[32]["Places Available"],
            "hubs": {
                "driver": { "name": "Stratford / Wanstead (A12 / North Circular)", "coords": [51.5750, 0.0250], "desc": "A12 corridor. 20m east to Romford; 30m west to Hampstead (Royal Free).", "alert": "A12 gives good car access east to Queen's Hospital Romford." },
                "transit": { "name": "Stratford Interchange", "coords": [51.5420, -0.0030], "desc": "Elizabeth line direct to Romford (18m); Overground / Jubilee + Northern line to Royal Free.", "alert": "Elizabeth Line provides ultrafast transit to Romford." }
            },
            "stages": [
                { "stage": "CT1 (Feb 27 - Feb 28)", "hosp": "Queen's Hospital, Romford", "desc": "Barking, Havering & Redbridge (BHRUT) - Complete IAC" },
                { "stage": "CT2 (Feb 28 - Feb 29)", "hosp": "Queen's Hospital, Romford", "desc": "BHRUT - 6m ITU & 3m Obs for IACOA" },
                { "stage": "CT3 (Feb 29 - Feb 30)", "hosp": "Royal Free Hospital", "desc": "Royal Free London - Stage 1 Anaesthesia completion" }
            ]
        },
        {
            "id": "ct1-london-north-central-lr3",
            "code": csv_rows[33]["Preference"],
            "region": "London",
            "title": "NC London: Royal Free (2 yrs) & Barnet Hospital (1 yr)",
            "places": csv_rows[33]["Places Available"],
            "hubs": {
                "driver": { "name": "Finchley / Golders Green (A1 / A598)", "coords": [51.5950, -0.1950], "desc": "A1 corridor. 15m south to Royal Free (Hampstead); 18m north to Barnet Hospital.", "alert": "Convenient car access up the A1 corridor to Barnet." },
                "transit": { "name": "Northern Line Corridor (Camden / Highgate / Finchley)", "coords": [51.5720, -0.1450], "desc": "Northern line (High Barnet branch) connects directly to High Barnet, and south to Belsize Park.", "alert": "Belsize Park (Northern line) is 5m walk from Royal Free; bus 107/263 to Barnet." }
            },
            "stages": [
                { "stage": "CT1 (Feb 27 - Feb 28)", "hosp": "Royal Free Hospital", "desc": "Royal Free Hampstead - Complete IAC" },
                { "stage": "CT2 (Feb 28 - Feb 29)", "hosp": "Royal Free Hospital", "desc": "Royal Free - 3m ITU & 3m Obs for IACOA" },
                { "stage": "CT3 (Feb 29 - Feb 30)", "hosp": "Barnet Hospital (BCF)", "desc": "Barnet Hospital - 3m ITU & Stage 1 Anaesthesia" }
            ]
        },
        {
            "id": "ct1-london-north-east-lr1",
            "code": csv_rows[34]["Preference"],
            "region": "London",
            "title": "NE London: Homerton (1 yr) & Romford (BHRUT 2 yrs)",
            "places": csv_rows[34]["Places Available"],
            "hubs": {
                "driver": { "name": "Stratford / Leyton (A12)", "coords": [51.5550, -0.0150], "desc": "10m to Homerton; 22m via A12 to Queen's Hospital Romford.", "alert": "A12 provides direct connection out to Romford." },
                "transit": { "name": "Stratford / Hackney Central", "coords": [51.5450, -0.0150], "desc": "Overground direct to Homerton (5m); Elizabeth Line direct to Romford (18m).", "alert": "Overground and Elizabeth Line make this rotation commute very fast." }
            },
            "stages": [
                { "stage": "CT1 (Feb 27 - Feb 28)", "hosp": "Homerton University Hospital", "desc": "Homerton Hospital CT1 initial placement" },
                { "stage": "CT2 (Feb 28 - Feb 29)", "hosp": "Queen's Hospital, Romford", "desc": "BHRUT acute anaesthesia & ITU" },
                { "stage": "CT3 (Feb 29 - Feb 30)", "hosp": "Queen's Hospital, Romford", "desc": "BHRUT Stage 1 completion" }
            ]
        }
    ]

def get_kss_rotations(csv_rows):
    return [
        {
            "id": "ct1-kss-kent-1",
            "code": csv_rows[35]["Preference"],
            "region": "Kent, Surrey and Sussex",
            "title": "KSS Kent: Maidstone & Tunbridge Wells NHS Trust",
            "places": csv_rows[35]["Places Available"],
            "hubs": {
                "driver": { "name": "Tonbridge / Paddock Wood (A21 / A228)", "coords": [51.1950, 0.3250], "desc": "A21/A228 corridor midway. 12m south to Tunbridge Wells Hospital; 15m north to Maidstone Hospital.", "alert": "Easy driving links between Tonbridge, Pembury and Maidstone." },
                "transit": { "name": "Tonbridge Station", "coords": [51.1910, 0.2740], "desc": "Major Kent railway hub with direct buses/shuttles to Pembury and Maidstone.", "alert": "Dedicated hospital shuttle bus connects Maidstone and Tunbridge Wells hospitals." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Tunbridge Wells Hospital (Pembury)", "desc": "Maidstone & Tunbridge Wells NHS Trust base" },
                { "stage": "CT1 (12m)", "hosp": "Maidstone Hospital", "desc": "Maidstone Hospital acute base alternative" }
            ]
        },
        {
            "id": "ct1-kss-kent-medway-k1e",
            "code": csv_rows[50]["Preference"],
            "region": "Kent, Surrey and Sussex",
            "title": "KSS Kent: Medway Maritime Hospital",
            "places": csv_rows[50]["Places Available"],
            "hubs": {
                "driver": { "name": "Rochester / Chatham / Gillingham (M2 J3/J4)", "coords": [51.3750, 0.5250], "desc": "5-10m drive to Medway Maritime Hospital; quick access from M2 / A2.", "alert": "Medway town centre hospital with staff permit parking." },
                "transit": { "name": "Gillingham Station (Kent)", "coords": [51.3870, 0.5510], "desc": "Southeastern high-speed line to St Pancras (45m); 15m walk or bus to Medway Maritime.", "alert": "High-speed rail connects Gillingham into central London." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Medway Maritime Hospital, Gillingham", "desc": "Medway NHS Foundation Trust base (CT2 & CT3 TBC)" }
            ]
        }
    ]

def get_west_midlands_rotations(csv_rows):
    return [
        {
            "id": "ct1-west-midlands-2",
            "code": csv_rows[39]["Preference"],
            "region": "West Midlands",
            "title": "Coventry (UHCW) Starting Scheme (6 Places)",
            "places": csv_rows[39]["Places Available"],
            "hubs": {
                "driver": { "name": "Coventry East / Kenilworth", "coords": [52.3850, -1.5150], "desc": "A46 / A45 corridor. 12m to UHCW Walsgrave; 15m to Warwick Hospital.", "alert": "A46 bypass gives quick access to hospitals across Coventry & Warwickshire." },
                "transit": { "name": "Coventry Station", "coords": [52.4010, -1.5130], "desc": "Direct hospital buses (9, 9A) link Coventry railway station to UHCW.", "alert": "Frequent bus services run between station and hospital." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "UHCW Coventry", "desc": "Major Trauma Centre & Tertiary Teaching Base" },
                { "stage": "CT2 - CT3", "hosp": "Warwick Hospital", "desc": "South Warwickshire acute placement" }
            ]
        },
        {
            "id": "ct1-west-midlands-1",
            "code": csv_rows[40]["Preference"],
            "region": "West Midlands",
            "title": "Dudley (Russells Hall) Starting Scheme",
            "places": csv_rows[40]["Places Available"],
            "hubs": {
                "driver": { "name": "Stourbridge / Dudley West (A491 / A4123)", "coords": [52.4850, -2.1350], "desc": "5-10m drive to Russells Hall Hospital; convenient access towards Wolverhampton and Birmingham.", "alert": "Central Black Country base." },
                "transit": { "name": "Stourbridge Junction / Dudley Bus Station", "coords": [52.4550, -2.1350], "desc": "Direct buses to Russells Hall Hospital; train links into Birmingham Snow Hill.", "alert": "Frequent bus services link Dudley town and Stourbridge to Russells Hall." }
            },
            "stages": [
                { "stage": "CT1 (12m)", "hosp": "Russells Hall Hospital, Dudley", "desc": "Dudley Group NHS Foundation Trust base" },
                { "stage": "CT2 - CT3", "hosp": "New Cross Hospital, Wolverhampton", "desc": "Black Country acute placement" },
                { "stage": "CT2 - CT3", "hosp": "Queen Elizabeth Hospital Birmingham", "desc": "Regional tertiary MTC placement" }
            ]
        }
    ]

def get_north_east_rotations(csv_rows):
    return [
        {
            "id": "ct1-north-east-1",
            "code": csv_rows[57]["Preference"],
            "region": "North East",
            "title": "North East & Cumbria 6-Monthly Scheme (4 Places)",
            "places": csv_rows[57]["Places Available"],
            "hubs": {
                "driver": { "name": "Newcastle / Gateshead (A1 corridor)", "coords": [54.9650, -1.6150], "desc": "Central North East hub. 10m to RVI/Freeman, 20m to Sunderland Royal via A184/A19.", "alert": "Carlisle is ~58 mi west via the A69 across northern Pennines." },
                "transit": { "name": "Newcastle Central Station / Metro", "coords": [54.9680, -1.6170], "desc": "Tyne & Wear Metro connects directly to RVI (Haymarket) and Sunderland.", "alert": "Metro network provides seamless links across Newcastle, Gateshead and Sunderland." }
            },
            "stages": [
                { "stage": "CT1 - CT3", "hosp": "Royal Victoria Infirmary, Newcastle", "desc": "Major Trauma Centre & tertiary acute" },
                { "stage": "CT1 - CT3", "hosp": "Freeman Hospital, Newcastle", "desc": "Regional Cardiothoracic & Transplant Centre" },
                { "stage": "CT1 - CT3", "hosp": "Sunderland Royal Hospital", "desc": "South Tyneside and Sunderland acute base" },
                { "stage": "CT1 - CT3", "hosp": "James Cook University Hospital, Middlesbrough", "desc": "Teesside Major Trauma Centre" },
                { "stage": "CT1 - CT3", "hosp": "Cumberland Infirmary, Carlisle", "desc": "North Cumbria acute base" }
            ]
        }
    ]
