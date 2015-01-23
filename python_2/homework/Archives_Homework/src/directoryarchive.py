import zipfile
import os
import glob

def zip_dir(path):
    """ Function to zip contents (files only) path passed as argument. """
    # Get our root directory
    root = os.path.basename(path)
    # Get our list of files from the path
    files = glob.glob(os.path.join(path, "*"))
    # Create an empty list for actual files
    files_to_archive = []
    # Loop through the files to check if all are actually files
    for fn in files:
        # If it's a file, add to the list
        if os.path.isfile(fn):
            files_to_archive.append(fn)
    # Create our zipfile
    archive_fn = os.path.join(path, 'archive.zip')
    # Open the zip for writing
    zf = zipfile.ZipFile(archive_fn, 'w')
    # Zip files in our directory, using that directory as the base
    for fn_to_archive in files_to_archive:
        zf.write(fn_to_archive, arcname=os.path.join(root, os.path.basename(fn_to_archive)), compress_type=zipfile.ZIP_DEFLATED)
    zf.close()
