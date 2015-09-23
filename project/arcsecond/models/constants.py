
NOT_A_SCIENTIFIC_NUMBER = -9999999999999
J2000 = 2000

bibcode_regex = "[0-9]{4}[A-Za-z&]+[\.]*[0-9]+[A-Za-z]?[\.]*[0-9]+[A-Z]"
eso_programme_id_regex = "[0-9]{2,3}\.[A-Fa-f]{1}-[0-9]{4}\([A-Za-z]{1}\)" # NOTE THE ABSENCE OF ^
times_regex = "([-+]?([0-9]*\.?[0-9]+)|([\d]{4}-[\d]{2}-[\d]{2}T[\d]{2}:[\d]{2}:[\d]{2}([A-Z]|\+[\d]{2}:[\d]{2}))"
time_formats_regex = 'byear|byear_str|cxcsec|datetime|decimalyear|gps|iso|isot|jd|jyear|jyear_str|mjd|plot_date|unix|yday'

ESO_INSTRUMENTS = {
    "HARPS":  {"site": "La Silla", "telescope": "3.6m"},
    "SOFI":   {"site": "La Silla", "telescope": "New Technology Telescope"},
    "EFOSC2": {"site": "La Silla", "telescope": "New Technology Telescope"},
    "WFI":    {"site": "La Silla", "telescope": "2.2m"},
    "FEROS":  {"site": "La Silla", "telescope": "2.2m"},
    "GROND":  {"site": "La Silla", "telescope": "2.2m"},

    "NACO":  {"site": "Paranal", "telescope": "Unit Telescope 1"},
    "FORS2": {"site": "Paranal", "telescope": "Unit Telescope 1"},
    "KMOS":  {"site": "Paranal", "telescope": "Unit Telescope 1"},

    "FLAMES":   {"site": "Paranal", "telescope": "Unit Telescope 2"},
    "XSHOOTER": {"site": "Paranal", "telescope": "Unit Telescope 2"},
    "UVES":     {"site": "Paranal", "telescope": "Unit Telescope 2"},

    "SPHERE": {"site": "Paranal", "telescope": "Unit Telescope 3"},
    "VISIR":  {"site": "Paranal", "telescope": "Unit Telescope 3"},
    "VIMOS":  {"site": "Paranal", "telescope": "Unit Telescope 3"},

    "HAWK-I":  {"site": "Paranal", "telescope": "Unit Telescope 4"},
    "SINFONI": {"site": "Paranal", "telescope": "Unit Telescope 4"},
    "MUSE":    {"site": "Paranal", "telescope": "Unit Telescope 4"},

    "VIRCAM":   {"site": "Paranal", "telescope": "VISTA"},
    "OmegaCAM": {"site": "Paranal", "telescope": "VST"},

    # Decomissionned

    "FORS1": {"site": "Paranal", "telescope": "Unit Telescope 1"},
    "ISAAC": {"site": "Paranal", "telescope": "Unit Telescope 3"},
}