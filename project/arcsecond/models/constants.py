
NOT_A_SCIENTIFIC_NUMBER = -9999999999999
J2000 = 2000

bibcode_regex = "[0-9]{4}[A-Za-z&]+[\.]*[0-9]+[A-Za-z]?[\.]*[0-9]+[A-Z]"
eso_programme_id_regex = "[0-9]{2,3}\.[A-Fa-f]{1}-[0-9]{4}\([A-Za-z]{1}\)" # NOTE THE ABSENCE OF ^
times_regex = "([-+]?([0-9]*\.?[0-9]+)|([\d]{4}-[\d]{2}-[\d]{2}T[\d]{2}:[\d]{2}:[\d]{2}([A-Z]|\+[\d]{2}:[\d]{2}))"
time_formats_regex = 'byear|byear_str|cxcsec|datetime|decimalyear|gps|iso|isot|jd|jyear|jyear_str|mjd|plot_date|unix|yday'

ESO_INSTRUMENTS = {
    "HARPS": {"name": "HARPS",  "site": "La Silla", "telescope": "3.6m"},
    "SOFI":  {"name": "SOFI",   "site": "La Silla", "telescope": "New Technology Telescope"},
    "EFOSC": {"name": "EFOSC2", "site": "La Silla", "telescope": "New Technology Telescope"},
    "WFI":   {"name": "WFI",    "site": "La Silla", "telescope": "ESO 2.2m"},
    "FEROS": {"name": "FEROS",  "site": "La Silla", "telescope": "ESO 2.2m"},
    "GROND": {"name": "GROND",  "site": "La Silla", "telescope": "ESO 2.2m"},

    "NACO":  {"name": "NAOS-CONICA", "site": "Paranal", "telescope": "Unit Telescope 1"},
    "FORS2": {"name": "FORS2", "site": "Paranal", "telescope": "Unit Telescope 1"},
    "KMOS":  {"name": "KMOS", "site": "Paranal", "telescope": "Unit Telescope 1"},

    "FLAME": {"name": "FLAMES", "site": "Paranal", "telescope": "Unit Telescope 2"},
    "GIRAF": {"name": "GIRAFFE", "site": "Paranal", "telescope": "Unit Telescope 2"},
    "XSHOO": {"name": "XSHOOTER", "site": "Paranal", "telescope": "Unit Telescope 2"},
    "UVES":  {"name": "UVES", "site": "Paranal", "telescope": "Unit Telescope 2"},

    "SPHER": {"name": "SPHERE", "site": "Paranal", "telescope": "Unit Telescope 3"},
    "VISIR": {"name": "VISIR", "site": "Paranal", "telescope": "Unit Telescope 3"},
    "VIMOS": {"name": "VIMOS", "site": "Paranal", "telescope": "Unit Telescope 3"},

    "HAWKI": {"name": "HAWK-I", "site": "Paranal", "telescope": "Unit Telescope 4"},
    "SINFO": {"name": "SINFONI", "site": "Paranal", "telescope": "Unit Telescope 4"},
    "MUSE":  {"name": "MUSE", "site": "Paranal", "telescope": "Unit Telescope 4"},

    "PIONI": {"name": "PIONIER", "site": "Paranal", "telescope": "VLTI"},

    "VCAM":  {"name": "VIRCAM", "site": "Paranal", "telescope": "VISTA"},
    "OMEGA": {"name": "OmegaCam", "site": "Paranal", "telescope": "VST"},

    # Decomissionned

    "FORS1": {"name": "FORS1", "site": "Paranal", "telescope": "Unit Telescope 1"},
    "ISAAC": {"name": "ISAAC", "site": "Paranal", "telescope": "Unit Telescope 3"},
}