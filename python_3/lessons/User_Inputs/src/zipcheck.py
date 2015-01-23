"""
zipcheck.py: validation function for US zip codes
"""

def zip_errors(z):
    """
    Validate z as either NNNN or NNNNN-NNNN.
    """
    l = len(z)
    if l not in (5, 10):
        return "Zip codes should be 5 or 10 characters long"
    if (not z[:5].isdigit() or
        (len(z) == 10 and not z[6:].isdigit())):
        return "Zip code has non-numeric characters"
    if l == 10 and z[5] != "-":
        return "Ten-digit zips must have a dash between the two parts"
    return
