import csv
import json

# Read CSV data
with open('ct1_rotations.csv', encoding='utf-8') as f:
    csv_rows = {int(r['Current Assigned Rank']): r for r in csv.DictReader(f)}

HOSPITALS = {
  # Cambridge Biomedical Campus
  "Addenbrooke's Hospital, Cambridge": { "coords": [52.1751, 0.1408], "region": "East of England" },
  "Royal Papworth Hospital, Cambridge": { "coords": [52.1738, 0.1388], "region": "East of England" },

  # East of England
  "Watford General Hospital": { "coords": [51.6471, -0.4035], "region": "East of England" },
  "Lister Hospital, Stevenage": { "coords": [51.9162, -0.2154], "region": "East of England" },
  "Broomfield Hospital, Chelmsford": { "coords": [51.7762, 0.4682], "region": "East of England" },
  "Basildon Cardiothoracic Centre": { "coords": [51.5562, 0.4491], "region": "East of England" },
  "Southend Hospital": { "coords": [51.5544, 0.6861], "region": "East of England" },
  "Colchester Hospital": { "coords": [51.9142, 0.9011], "region": "East of England" },
  "Princess Alexandra Hospital, Harlow": { "coords": [51.7725, 0.0894], "region": "East of England" },
  "Bedford Hospital": { "coords": [52.1292, -0.4683], "region": "East of England" },
  "Luton & Dunstable Hospital": { "coords": [51.8972, -0.4721], "region": "East of England" },
  "Norfolk & Norwich University Hospital": { "coords": [52.6181, 1.2212], "region": "East of England" },
  "Ipswich Hospital": { "coords": [52.0543, 1.2001], "region": "East of England" },
  "West Suffolk Hospital, Bury St Edmunds": { "coords": [52.2321, 0.7042], "region": "East of England" },
  "James Paget Hospital, Great Yarmouth": { "coords": [52.5492, 1.7161], "region": "East of England" },
  "Queen Elizabeth Hospital, Kings Lynn": { "coords": [52.7531, 0.4431], "region": "East of England" },
  "Peterborough City Hospital": { "coords": [52.5844, -0.2786], "region": "East of England" },

  # London
  "Royal Free Hospital": { "coords": [51.5532, -0.1652], "region": "London" },
  "St Bartholomew's Hospital (Barts Cardiac)": { "coords": [51.5173, -0.1002], "region": "London" },
  "Queen Square (NHNN)": { "coords": [51.5221, -0.1224], "region": "London" },
  "University College Hospital (UCH)": { "coords": [51.5252, -0.1362], "region": "London" },
  "Moorfields Eye Hospital": { "coords": [51.5273, -0.0881], "region": "London" },
  "Royal London Hospital": { "coords": [51.5192, -0.0593], "region": "London" },
  "Barnet Hospital (BCF)": { "coords": [51.6521, -0.2223], "region": "London" },
  "RNOH Stanmore": { "coords": [51.6262, -0.3204], "region": "London" },
  "Queen's Hospital, Romford": { "coords": [51.5691, 0.1792], "region": "London" },
  "Whittington Hospital (London General)": { "coords": [51.5661, -0.1402], "region": "London" },
  "Homerton University Hospital": { "coords": [51.5504, -0.0483], "region": "London" },
  "Chelsea & Westminster Hospital": { "coords": [51.4842, -0.1824], "region": "London" },
  "Charing Cross Hospital": { "coords": [51.4883, -0.2192], "region": "London" },
  "Northwick Park Hospital": { "coords": [51.5772, -0.3202], "region": "London" },
  "Hammersmith Hospital": { "coords": [51.5171, -0.2372], "region": "London" },
  "St Mary's Hospital, Paddington": { "coords": [51.5172, -0.1742], "region": "London" },
  "Royal Brompton Hospital": { "coords": [51.4902, -0.1693], "region": "London" },
  "West Middlesex University Hospital": { "coords": [51.4782, -0.3271], "region": "London" },
  "Hillingdon Hospital": { "coords": [51.5232, -0.4601], "region": "London" },
  "St George's Hospital, Tooting": { "coords": [51.4272, -0.1752], "region": "London" },
  "King's College Hospital": { "coords": [51.4682, -0.0931], "region": "London" },
  "Guy's & St Thomas' Hospital": { "coords": [51.4982, -0.1192], "region": "London" },

  # Kent, Surrey and Sussex
  "Maidstone Hospital": { "coords": [51.2747, 0.4857], "region": "Kent, Surrey and Sussex" },
  "Tunbridge Wells Hospital (Pembury)": { "coords": [51.1488, 0.3081], "region": "Kent, Surrey and Sussex" },
  "Medway Maritime Hospital, Gillingham": { "coords": [51.3795, 0.5416], "region": "Kent, Surrey and Sussex" },

  # Thames Valley
  "John Radcliffe Hospital, Oxford": { "coords": [51.7652, -1.2191], "region": "Thames Valley" },
  "Horton General Hospital, Banbury": { "coords": [52.0537, -1.3363], "region": "Thames Valley" },
  "Royal Berkshire Hospital, Reading": { "coords": [51.4472, -0.9602], "region": "Thames Valley" },
  "Stoke Mandeville Hospital, Aylesbury": { "coords": [51.7997, -0.8024], "region": "Thames Valley" },
  "Wycombe Hospital, High Wycombe": { "coords": [51.6262, -0.7536], "region": "Thames Valley" },

  # Wessex
  "Southampton General Hospital": { "coords": [50.9341, -1.4322], "region": "Wessex" },
  "Queen Alexandra Hospital, Portsmouth": { "coords": [50.8492, -1.0712], "region": "Wessex" },
  "Basingstoke & North Hampshire Hospital": { "coords": [51.2721, -1.1092], "region": "Wessex" },
  "Royal Hampshire County Hospital, Winchester": { "coords": [51.0641, -1.3321], "region": "Wessex" },
  "Poole Hospital": { "coords": [50.7252, -1.9772], "region": "Wessex" },
  "Royal Bournemouth Hospital": { "coords": [50.7422, -1.8261], "region": "Wessex" },
  "Dorset County Hospital, Dorchester": { "coords": [50.7132, -2.4462], "region": "Wessex" },
  "Salisbury District Hospital": { "coords": [51.0471, -1.7962], "region": "Wessex" },

  # South West - Severn
  "Bristol Royal Infirmary (UHBW)": { "coords": [51.4582, -2.5971], "region": "South West - Severn" },
  "Southmead Hospital (NBT)": { "coords": [51.4972, -2.5931], "region": "South West - Severn" },
  "Gloucestershire Royal Hospital": { "coords": [51.8682, -2.2341], "region": "South West - Severn" },
  "Great Western Hospital, Swindon": { "coords": [51.5332, -1.7331], "region": "South West - Severn" },
  "Royal United Hospital, Bath": { "coords": [51.3917, -2.3910], "region": "South West - Severn" },
  "Yeovil District Hospital": { "coords": [50.9452, -2.6339], "region": "South West - Severn" },

  # South West - Peninsula
  "Royal Cornwall Hospital, Truro": { "coords": [50.2712, -5.0931], "region": "South West - Peninsula" },
  "Derriford Hospital, Plymouth": { "coords": [50.4162, -4.1162], "region": "South West - Peninsula" },
  "Royal Devon & Exeter Hospital": { "coords": [50.7152, -3.5131], "region": "South West - Peninsula" },
  "Torbay Hospital": { "coords": [50.4852, -3.5571], "region": "South West - Peninsula" },
  "Musgrove Park Hospital, Taunton": { "coords": [51.0142, -3.1202], "region": "South West - Peninsula" },
  "North Devon District Hospital, Barnstaple": { "coords": [51.0922, -4.0504], "region": "South West - Peninsula" },

  # East Midlands
  "Queen's Medical Centre (QMC), Nottingham": { "coords": [52.9431, -1.1862], "region": "East Midlands" },
  "Nottingham City Hospital": { "coords": [52.9862, -1.1612], "region": "East Midlands" },
  "Royal Derby Hospital": { "coords": [52.9102, -1.5121], "region": "East Midlands" },
  "Chesterfield Royal Hospital": { "coords": [53.2272, -1.3912], "region": "East Midlands" },
  "Lincoln County Hospital": { "coords": [53.2321, -0.5182], "region": "East Midlands" },
  "Boston Pilgrim Hospital": { "coords": [52.9892, -0.0071], "region": "East Midlands" },
  "Kings Mill Hospital, Mansfield": { "coords": [53.1362, -1.2181], "region": "East Midlands" },
  "Leicester Royal Infirmary": { "coords": [52.6282, -1.1342], "region": "East Midlands" },
  "Glenfield Hospital, Leicester": { "coords": [52.6542, -1.1802], "region": "East Midlands" },
  "Northampton General Hospital": { "coords": [52.2352, -0.8871], "region": "East Midlands" },
  "Kettering General Hospital": { "coords": [52.3992, -0.7381], "region": "East Midlands" },
  "Queen's Hospital, Burton": { "coords": [52.8177, -1.6560], "region": "East Midlands" },

  # Wales
  "Glan Clwyd Hospital, Rhyl": { "coords": [53.2682, -3.5161], "region": "Wales" },
  "Ysbyty Gwynedd, Bangor": { "coords": [53.2090, -4.1620], "region": "Wales" },
  "The Walton Centre, Liverpool": { "coords": [53.4752, -2.9421], "region": "Wales" },
  "Glangwili Hospital, Carmarthen": { "coords": [51.8642, -4.2882], "region": "Wales" },
  "Royal Glamorgan Hospital, Llantrisant": { "coords": [51.5452, -3.3981], "region": "Wales" },
  "Morriston Hospital, Swansea": { "coords": [51.6702, -3.9262], "region": "Wales" },
  "University Hospital of Wales, Cardiff": { "coords": [51.5072, -3.1902], "region": "Wales" },
  "Princess of Wales Hospital, Bridgend": { "coords": [51.5174, -3.5717], "region": "Wales" },
  "Grange University Hospital, Cwmbran": { "coords": [51.6470, -2.9960], "region": "Wales" },
  "Prince Charles Hospital, Merthyr Tydfil": { "coords": [51.7641, -3.3849], "region": "Wales" },

  # West Midlands
  "Royal Stoke University Hospital": { "coords": [53.0052, -2.2152], "region": "West Midlands" },
  "New Cross Hospital, Wolverhampton": { "coords": [52.5972, -2.0972], "region": "West Midlands" },
  "Walsall Manor Hospital": { "coords": [52.5852, -1.9962], "region": "West Midlands" },
  "Midlands Met University Hospital": { "coords": [52.4972, -1.9672], "region": "West Midlands" },
  "Royal Shrewsbury Hospital": { "coords": [52.7062, -2.7842], "region": "West Midlands" },
  "Queen Elizabeth Hospital Birmingham": { "coords": [52.4512, -1.9402], "region": "West Midlands" },
  "UHCW Coventry": { "coords": [52.4172, -1.4362], "region": "West Midlands" },
  "Warwick Hospital": { "coords": [52.2852, -1.5972], "region": "West Midlands" },
  "Russells Hall Hospital, Dudley": { "coords": [52.5024, -2.1191], "region": "West Midlands" },

  # Yorkshire and the Humber
  "Hull Royal Infirmary": { "coords": [53.7442, -0.3582], "region": "Yorkshire and the Humber" },
  "York Hospital": { "coords": [53.9702, -1.0832], "region": "Yorkshire and the Humber" },
  "Scarborough Hospital": { "coords": [54.2792, -0.4282], "region": "Yorkshire and the Humber" },
  "Scunthorpe General Hospital": { "coords": [53.5902, -0.6692], "region": "Yorkshire and the Humber" },
  "Diana, Princess of Wales Hospital, Grimsby": { "coords": [53.5448, -0.0962], "region": "Yorkshire and the Humber" },
  "Goole and District Hospital": { "coords": [53.7166, -0.8745], "region": "Yorkshire and the Humber" },
  "Northern General Hospital, Sheffield": { "coords": [53.4152, -1.4582], "region": "Yorkshire and the Humber" },
  "Royal Hallamshire Hospital, Sheffield": { "coords": [53.3785, -1.4932], "region": "Yorkshire and the Humber" },
  "Doncaster Royal Infirmary": { "coords": [53.5282, -1.1062], "region": "Yorkshire and the Humber" },
  "Rotherham Hospital": { "coords": [53.4182, -1.3482], "region": "Yorkshire and the Humber" },
  "Barnsley Hospital": { "coords": [53.5582, -1.5042], "region": "Yorkshire and the Humber" },
  "Bassetlaw Hospital, Worksop": { "coords": [53.3170, -1.1104], "region": "Yorkshire and the Humber" },
  "Leeds General Infirmary": { "coords": [53.8012, -1.5532], "region": "Yorkshire and the Humber" },
  "Bradford Royal Infirmary": { "coords": [53.8042, -1.7962], "region": "Yorkshire and the Humber" },
  "Pinderfields Hospital, Wakefield": { "coords": [53.6932, -1.4842], "region": "Yorkshire and the Humber" },
  "Calderdale Royal Hospital, Halifax": { "coords": [53.7050, -1.8574], "region": "Yorkshire and the Humber" },
  "Huddersfield Royal Infirmary": { "coords": [53.6553, -1.8151], "region": "Yorkshire and the Humber" },
  "Airedale General Hospital, Steeton": { "coords": [53.8980, -1.9627], "region": "Yorkshire and the Humber" },
  "Harrogate District Hospital": { "coords": [53.9937, -1.5176], "region": "Yorkshire and the Humber" },

  # North West
  "Royal Liverpool University Hospital": { "coords": [53.4092, -2.9642], "region": "North West" },
  "Liverpool Women's Hospital (LWH)": { "coords": [53.3985, -2.9610], "region": "North West" },
  "Aintree University Hospital, Liverpool": { "coords": [53.4616, -2.9434], "region": "North West" },
  "Whiston Hospital, Prescot": { "coords": [53.4208, -2.7877], "region": "North West" },
  "Warrington Hospital": { "coords": [53.3938, -2.6097], "region": "North West" },
  "Southport and Formby District General Hospital": { "coords": [53.6338, -2.9787], "region": "North West" },
  "Countess of Chester Hospital": { "coords": [53.2086, -2.8986], "region": "North West" },
  "Leighton Hospital, Crewe": { "coords": [53.1199, -2.4778], "region": "North West" },
  "Arrowe Park Hospital (Wirral)": { "coords": [53.3699, -3.0960], "region": "North West" },
  "Manchester Royal Infirmary": { "coords": [53.4622, -2.2272], "region": "North West" },
  "Salford Royal Hospital": { "coords": [53.4881, -2.3214], "region": "North West" },
  "Wythenshawe Hospital, Manchester": { "coords": [53.3897, -2.2950], "region": "North West" },
  "Royal Bolton Hospital": { "coords": [53.5539, -2.4299], "region": "North West" },
  "Stepping Hill Hospital, Stockport": { "coords": [53.3839, -2.1318], "region": "North West" },

  # North East
  "Royal Victoria Infirmary, Newcastle": { "coords": [54.9782, -1.6232], "region": "North East" },
  "Freeman Hospital, Newcastle": { "coords": [55.0020, -1.5940], "region": "North East" },
  "Sunderland Royal Hospital": { "coords": [54.9031, -1.4097], "region": "North East" },
  "James Cook University Hospital, Middlesbrough": { "coords": [54.5520, -1.2140], "region": "North East" },
  "Cumberland Infirmary, Carlisle": { "coords": [54.8965, -2.9577], "region": "North East" }
}

REGION_COLORS = {
  "East of England": "#ea580c",
  "East Midlands": "#16a34a",
  "Kent, Surrey and Sussex": "#059669",
  "London": "#dc2626",
  "North East": "#6366f1",
  "North West": "#0284c7",
  "South West - Peninsula": "#0d9488",
  "South West - Severn": "#0891b2",
  "Thames Valley": "#8b5cf6",
  "Wales": "#c026d3",
  "Wessex": "#2563eb",
  "West Midlands": "#d97706",
  "Yorkshire and the Humber": "#4f46e5"
}
