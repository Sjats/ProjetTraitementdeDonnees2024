domaine_a_pays = {
    ".us": "United States",    # United States
    ".uk": "United Kingdom",    # United Kingdom
    ".fr": "France",    # France
    ".de": "Germany",    # Germany
    ".es": "Spain",    # Spain
    ".it": "Italy",    # Italy
    ".jp": "Japan",    # Japan
    ".cn": "China",    # China
    ".ca": "Canada",    # Canada
    ".au": "Australia",    # Australia
    ".ch": "Switzerland",    # Switzerland
    ".ae": "United Arab Emirates",    # United Arab Emirates
    ".at": "Austria",    # Austria
    ".be": "Belgium",    # Belgium
    ".nl": "Netherlands",    # Netherlands
    ".pt": "Portugal",    # Portugal
    ".se": "Sweden",    # Sweden
    ".fi": "Finland",    # Finland
    ".dk": "Denmark",    # Denmark
    ".no": "Norway",    # Norway
    ".gr": "Greece",    # Greece
    ".cz": "Czech Republic",    # Czech Republic
    ".pl": "Poland",    # Poland
    ".hu": "Hungary",    # Hungary
    ".ro": "Romania",    # Romania
    ".bg": "Bulgaria",    # Bulgaria
    ".sk": "Slovakia",    # Slovakia
    ".si": "Slovenia",    # Slovenia
    ".hr": "Croatia",    # Croatia
    ".lt": "Lithuania",    # Lithuania
    ".lv": "Latvia",    # Latvia
    ".ee": "Estonia",    # Estonia
    ".ru": "Russia",    # Russia
    ".br": "Brazil",    # Brazil
    ".in": "India",    # India
    ".mx": "Mexico",    # Mexico
    ".za": "South Africa",    # South Africa
    ".kr": "South Korea",    # South Korea
    ".tr": "Turkey",    # Turkey
    ".id": "Indonesia",    # Indonesia
    ".th": "Thailand",    # Thailand
    ".my": "Malaysia",    # Malaysia
    ".sg": "Singapore",    # Singapore
    ".ng": "Nigeria",    # Nigeria
    ".cl": "Chile",    # Chile
    ".ar": "Argentina",    # Argentina
    ".co": "Colombia",    # Colombia
    ".vn": "Vietnam",    # Vietnam
    ".ph": "Philippines",    # Philippines
    ".ua": "Ukraine",    # Ukraine
    ".kz": "Kazakhstan",    # Kazakhstan
    ".uz": "Uzbekistan",    # Uzbekistan
    ".bd": "Bangladesh",    # Bangladesh
    ".ir": "Iran",    # Iran
    ".iq": "Iraq",    # Iraq
    ".sa": "Saudi Arabia",    # Saudi Arabia
    ".ae": "United Arab Emirates",    # United Arab Emirates
    ".eg": "Egypt",    # Egypt
    ".dz": "Algeria",    # Algeria
    ".ma": "Morocco",    # Morocco
    ".tn": "Tunisia",    # Tunisia
    ".ke": "Kenya",    # Kenya
    ".et": "Ethiopia",    # Ethiopia
    ".gh": "Ghana",    # Ghana
    ".ug": "Uganda",    # Uganda
    ".zw": "Zimbabwe",    # Zimbabwe
    ".cd": "Democratic Republic of the Congo",    # DR of the Congo
    ".tz": "Tanzania",    # Tanzania
    ".cm": "Cameroon",    # Cameroon
    ".ci": "Ivory Coast",    # Ivory Coast
    ".sn": "Senegal",    # Senegal
    ".ml": "Mali",    # Mali
    ".ne": "Niger",    # Niger
    ".bf": "Burkina Faso",    # Burkina Faso
    ".bj": "Benin",    # Benin
    ".tg": "Togo",    # Togo
    ".gh": "Ghana",    # Ghana
    ".gn": "Guinea",    # Guinea
    ".gw": "Guinea-Bissau",    # Guinea-Bissau
    ".lr": "Liberia",    # Liberia
    ".sl": "Sierra Leone",    # Sierra Leone
    ".mw": "Malawi",    # Malawi
    ".mz": "Mozambique",    # Mozambique
    ".zm": "Zambia",    # Zambia
    ".bw": "Botswana",    # Botswana
    ".na": "Namibia",    # Namibia
    ".sz": "Eswatini",    # Eswatini
    ".ls": "Lesotho",    # Lesotho
    ".ao": "Angola",    # Angola
    ".gq": "Equatorial Guinea",    # Equatorial Guinea
    ".cf": "Central African Republic",    # Central African Republic
    ".td": "Chad",    # Chad
    ".cg": "Republic of the Congo",    # Republic of the Congo
    ".ga": "Gabon",    # Gabon
    ".st": "Sao Tome and Principe",    # Sao Tome and Principe
    ".cv": "Cape Verde",    # Cape Verde
    ".dj": "Djibouti",    # Djibouti
    ".er": "Eritrea",    # Eritrea
    ".so": "Somalia",    # Somalia
    ".sd": "Sudan",    # Sudan
    ".ss": "South Sudan",    # South Sudan
    ".bi": "Burundi",    # Burundi
    ".rw": "Rwanda",    # Rwanda
    ".ug": "Uganda",    # Uganda
    ".et": "Ethiopia",    # Ethiopia
    ".ke": "Kenya",    # Kenya
    ".tz": "Tanzania",    # Tanzania
    ".mg": "Madagascar",    # Madagascar
    ".mu": "Mauritius",    # Mauritius
    ".mw": "Malawi",    # Malawi
    ".mz": "Mozambique",    # Mozambique
    ".sc": "Seychelles",    # Seychelles
    ".zm": "Zambia",    # Zambia
    ".zw": "Zimbabwe",    # Zimbabwe
    ".bw": "Botswana",    # Botswana
    ".sz": "Eswatini",    # Eswatini
    ".na": "Namibia",    # Namibia
    ".ls": "Lesotho",    # Lesotho
    ".za": "South Africa",    # South Africa
    ".ao": "Angola",    # Angola
    ".gq": "Equatorial Guinea",    # Equatorial Guinea
    ".ga": "Gabon",    # Gabon
    ".cg": "Republic of the Congo",    # Republic of the Congo
    ".cd": "Democratic Republic of the Congo",    # DR of the Congo
    ".cf": "Central African Republic",    # Central African Republic
    ".td": "Chad",    # Chad
    ".cm": "Cameroon",    # Cameroon
    ".bj": "Benin",    # Benin
    ".bf": "Burkina Faso",    # Burkina Faso
    ".ci": "Ivory Coast",    # Ivory Coast
    ".gn": "Guinea",    # Guinea
    ".gw": "Guinea-Bissau",    # Guinea-Bissau
    ".lr": "Liberia",    # Liberia
    ".ml": "Mali",    # Mali
    ".mr": "Mauritania",    # Mauritania
    ".ne": "Niger",    # Niger
    ".ng": "Nigeria",    # Nigeria
    ".sn": "Senegal",    # Senegal
    ".sl": "Sierra Leone",    # Sierra Leone
    ".tg": "Togo",    # Togo
    ".com": "United States"    # United States
}


def DomainePays(domain):
    domain = domain.lower()[-3:]
    return domaine_a_pays[domain]
