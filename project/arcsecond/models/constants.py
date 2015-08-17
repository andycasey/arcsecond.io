
NOT_A_SCIENTIFIC_NUMBER = -9999999999999
J2000 = 2000

bibcode_regex = "[0-9]{4}[A-Za-z&]+[\.]*[0-9]+[A-Za-z]?[\.]*[0-9]+[A-Z]"
eso_programme_id_regex = "[0-9]{2,3}\.[A-Fa-f]{1}-[0-9]{4}\([A-Za-z]{1}\)" # NOTE THE ABSENCE OF ^
times_regex = "([-+]?([0-9]*\.?[0-9]+)|([\d]{4}-[\d]{2}-[\d]{2}T[\d]{2}:[\d]{2}:[\d]{2}([A-Z]|\+[\d]{2}:[\d]{2}))"
time_formats_regex = 'byear|byear_str|cxcsec|datetime|decimalyear|gps|iso|isot|jd|jyear|jyear_str|mjd|plot_date|unix|yday'
