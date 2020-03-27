
HOST = "coronavirus-monitor.p.rapidapi.com"
API_KEY = "rvy6OR8SFOjlCcMXB7uGNKXGaPC5OW06"


indian_states_abbr = {
    "ap": "Andhra Pradesh",
    "ar": "Arunachal Pradesh",
    "as": "Assam",
    "br": "Bihar",
    "ct": "Chhattisgarh",
    "dl": "Delhi",
    "ga": "Goa",
    "gj": "Gujarat",
    "hr": "Haryana",
    "hp": "Himachal Pradesh",
    "jk": "Jammu & Kashmir",
    "jh": "Jharkhand",
    "ka": "Karnataka",
    "kl": "Kerala",
    "mp": "Madhya Pradesh",
    "mh": "Maharashtra",
    "mn": "Manipur",
    "ml": "Meghalaya",
    "mz": "Mizoram",
    "nl": "Nagaland",
    "or": "Orissa",
    "pb": "Punjab",
    "rj": "Rajasthan",
    "sk": "Sikkim",
    "tn": "Tamil Nadu",
    "tr": "Tripura",
    "ut": "Uttarakhand",
    "up": "Uttar Pradesh",
    "wb": "West Bengal",
    "an": "Andaman & Nicobar",
    "ch": "Chandigarh",
    "dn": "Dadra and Nagar Haveli",
    "dd": "Daman & Diu",
    "ld": "Lakshadweep",
    "la": "Ladakh",
    "tg": "Telengana",
    "py": "Pondicherry"
}


country_code_map = {
    "Afghanistan": "AF",
        "Aland Islands": "AX",
        "Albania": "AL",
        "Algeria": "DZ",
        "American Samoa": "AS",
        "Andorra": "AD",
        "Angola": "AO",
        "Anguilla": "AI",
        "Antarctica": "AQ",
        "Antigua and Barbuda": "AG",
        "Argentina": "AR",
        "Armenia": "AM",
        "Aruba": "AW",
        "Australia": "AU",
        "Austria": "AT",
        "Azerbaijan": "AZ",
        "Bahamas": "BS",
        "Bahrain": "BH",
        "Bangladesh": "BD",
        "Barbados": "BB",
        "Belarus": "BY",
        "Belgium": "BE",
        "Belize": "BZ",
        "Benin": "BJ",
        "Bermuda": "BM",
        "Bhutan": "BT",
        "Bolivia": "BO",
        "Bonaire, Sint Eustatius and Saba": "BQ",
        "Bosnia and Herzegovina": "BA",
        "Botswana": "BW",
        "Bouvet Island": "BV",
        "Brazil": "BR",
        "British Indian Ocean Territory": "IO",
        "Brunei": "BN",
        "Bulgaria": "BG",
        "Burkina Faso": "BF",
        "Burundi": "BI",
        "Cambodia": "KH",
        "Cameroon": "CM",
        "Canada": "CA",
        "Cabo Verde": "CV",
        "Cayman Islands": "KY",
        "CAR": "CF",
        "Chad": "TD",
        "Chile": "CL",
        "China": "CN",
        "Christmas Island": "CX",
        "Cocos (Keeling) Islands": "CC",
        "Colombia": "CO",
        "Comoros": "KM",
        "Congo": "CG",
        "DRC": "CD",
        "Cook Islands": "CK",
        "Costa Rica": "CR",
        "Ivory Coast": "CI",
        "Croatia": "HR",
        "Cuba": "CU",
        "Cura\u00e7ao": "CW",
        "Cyprus": "CY",
        "Czechia": "CZ",
        "Denmark": "DK",
        "Djibouti": "DJ",
        "Dominica": "DM",
        "Dominican Republic": "DO",
        "Ecuador": "EC",
        "Egypt": "EG",
        "El Salvador": "SV",
        "Equatorial Guinea": "GQ",
        "Eritrea": "ER",
        "Estonia": "EE",
        "Ethiopia": "ET",
        "Falkland Islands (Malvinas)": "FK",
        "Faeroe Islands": "FO",
        "Fiji": "FJ",
        "Finland": "FI",
        "France": "FR",
        "French Guiana": "GF",
        "French Polynesia": "PF",
        "French Southern Territories": "TF",
        "Gabon": "GA",
        "Gambia": "GM",
        "Georgia": "GE",
        "Germany": "DE",
        "Ghana": "GH",
        "Gibraltar": "GI",
        "Greece": "GR",
        "Greenland": "GL",
        "Grenada": "GD",
        "Guadeloupe": "GP",
        "Guam": "GU",
        "Guatemala": "GT",
        "Guernsey": "GG",
        "Guinea": "GN",
        "Guinea-Bissau": "GW",
        "Guyana": "GY",
        "Haiti": "HT",
        "Heard Island and McDonald Islands": "HM",
        "Vatican City": "VA",
        "Honduras": "HN",
        "Hong Kong": "HK",
        "Hungary": "HU",
        "Iceland": "IS",
        "India": "IN",
        "Indonesia": "ID",
        "Iran": "IR",
        "Iraq": "IQ",
        "Ireland": "IE",
        "Isle of Man": "IM",
        "Israel": "IL",
        "Italy": "IT",
        "Jamaica": "JM",
        "Japan": "JP",
        "Jersey": "JE",
        "Jordan": "JO",
        "Kazakhstan": "KZ",
        "Kenya": "KE",
        "Kiribati": "KI",
        "Korea, Democratic People's Republic of": "KP",
        "S. Korea": "KR",
        "Kuwait": "KW",
        "Kyrgyzstan": "KG",
        "Laos": "LA",
        "Latvia": "LV",
        "Lebanon": "LB",
        "Lesotho": "LS",
        "Liberia": "LR",
        "Libya": "LY",
        "Liechtenstein": "LI",
        "Lithuania": "LT",
        "Luxembourg": "LU",
        "Macao": "MO",
        "North Macedonia": "MK",
        "Madagascar": "MG",
        "Malawi": "MW",
        "Malaysia": "MY",
        "Maldives": "MV",
        "Mali": "ML",
        "Malta": "MT",
        "Marshall Islands": "MH",
        "Martinique": "MQ",
        "Mauritania": "MR",
        "Mauritius": "MU",
        "Mayotte": "YT",
        "Mexico": "MX",
        "Micronesia, Federated States of": "FM",
        "Moldova": "MD",
        "Monaco": "MC",
        "Mongolia": "MN",
        "Montenegro": "ME",
        "Montserrat": "MS",
        "Morocco": "MA",
        "Mozambique": "MZ",
        "Myanmar": "MM",
        "Namibia": "NA",
        "Nauru": "NR",
        "Nepal": "NP",
        "Netherlands": "NL",
        "New Caledonia": "NC",
        "New Zealand": "NZ",
        "Nicaragua": "NI",
        "Niger": "NE",
        "Nigeria": "NG",
        "Niue": "NU",
        "Norfolk Island": "NF",
        "Northern Mariana Islands": "MP",
        "Norway": "NO",
        "Oman": "OM",
        "Pakistan": "PK",
        "Palau": "PW",
        "Palestine": "PS",
        "Panama": "PA",
        "Papua New Guinea": "PG",
        "Paraguay": "PY",
        "Peru": "PE",
        "Philippines": "PH",
        "Pitcairn": "PN",
        "Poland": "PL",
        "Portugal": "PT",
        "Puerto Rico": "PR",
        "Qatar": "QA",
        "R\u00e9union": "RE",
        "Romania": "RO",
        "Russia": "RU",
        "Rwanda": "RW",
        "St. Barth": "BL",
        "Saint Helena, Ascension and Tristan da Cunha": "SH",
        "Saint Kitts and Nevis": "KN",
        "Saint Lucia": "LC",
        "Saint Martin": "MF",
        "Saint Pierre and Miquelon": "PM",
        "St. Vincent Grenadines": "VC",
        "Samoa": "WS",
        "San Marino": "SM",
        "Sao Tome and Principe": "ST",
        "Saudi Arabia": "SA",
        "Senegal": "SN",
        "Serbia": "RS",
        "Seychelles": "SC",
        "Sierra Leone": "SL",
        "Singapore": "SG",
        "Sint Maarten": "SX",
        "Slovakia": "SK",
        "Slovenia": "SI",
        "Solomon Islands": "SB",
        "Somalia": "SO",
        "South Africa": "ZA",
        "South Georgia and the South Sandwich Islands": "GS",
        "South Sudan": "SS",
        "Spain": "ES",
        "Sri Lanka": "LK",
        "Sudan": "SD",
        "Suriname": "SR",
        "Svalbard and Jan Mayen": "SJ",
        "Eswatini": "SZ",
        "Sweden": "SE",
        "Switzerland": "CH",
        "Syria": "SY",
        "Taiwan": "TW",
        "Tajikistan": "TJ",
        "Tanzania": "TZ",
        "Thailand": "TH",
        "Timor-Leste": "TL",
        "Togo": "TG",
        "Tokelau": "TK",
        "Tonga": "TO",
        "Trinidad and Tobago": "TT",
        "Tunisia": "TN",
        "Turkey": "TR",
        "Turkmenistan": "TM",
        "Turks and Caicos": "TC",
        "Tuvalu": "TV",
        "Uganda": "UG",
        "Ukraine": "UA",
        "UAE": "AE",
        "UK": "GB",
        "USA": "US",
        "United States Minor Outlying Islands": "UM",
        "Uruguay": "UY",
        "Uzbekistan": "UZ",
        "Vanuatu": "VU",
        "Venezuela": "VE",
        "Vietnam": "VN",
        "British Virgin Islands": "VG",
        "Virgin Islands, U.S.": "VI",
        "Wallis and Futuna": "WF",
        "Western Sahara": "EH",
        "Yemen": "YE",
        "Zambia": "ZM",
        "Zimbabwe": "ZW",
        "Diamond Princess": "DIAPR"
}
