#!/usr/bin/python3
# Script to rename image files, adding prefix dd_ which ensures sorting by image-taken date.
# Copyright 2026 Patrick Lam
# Released under BSD 3-clause license

from os import listdir
from os.path import isfile, join
from pathlib import Path
#from PIL import Image
import exifread

import time
from datetime import datetime
import pathlib
import re
import sys, time, subprocess
import os
import requests
import urllib
import re
import argparse

BASE_URL = "https://gallery.patricklam.ca/"
WEBPAGE_IMAGE_ARCHIVE = "webpage-image-archive"
TWO_DIGITS_FIRST_RE = re.compile(r"\d\d_.*")

# used to have imgDate() here from https://orthallelous.wordpress.com/2015/04/19/extracting-date-and-time-from-images-with-python/

class PiwigoConnector(object):
    def __init__(self, base_url, user, password, docker_container="piwigo"):
        self.base_url = base_url

    def fetch_image_id(self, filename_fragment):
        shorter_fragment = os.path.splitext(filename_fragment)[0].split('-')
        payload = [('format', 'json'), ('method', 'pwg.images.search'), ('query', shorter_fragment[0])]
        response = requests.get(self.base_url, params=payload)
        result = response.json()['result']
        if len(result['images']) == 1:
            return result['images'][0]['id']
        print ("img search failed: {}".format(filename_fragment))
        return None
        #raise UserWarning("wrong number of search results (not 1)")

    def fetch_first_category(self, id):
        payload = [('format', 'json'), ('method', 'pwg.images.getInfo'), ('image_id', id)]
        response = requests.get(self.base_url, params=payload)
        result = response.json()['result']
        if len(result['categories']) == 1:
            return result['categories'][0]['id']
        print ("categories search failed: {}".format(filename_fragment))
        return "YYY"
        #raise UserWarning("wrong number of categories (not 1)")

def main():
    args = sys.argv[1:]

    parser = argparse.ArgumentParser(
        prog='RenameByDate',
        description='rename image files to add dd_ prefix by date taken & lookup gallery links')
    parser.add_argument('-o', '--offline', action=argparse.BooleanOptionalAction, help='do not make Piwigo requests to create CSV')
    parser.add_argument('-p', '--preserve-names', action=argparse.BooleanOptionalAction, help='do not rename')
    parsed_args, remaining_args = parser.parse_known_args(args)

    target_dir = '.'
    if len(remaining_args) > 1:
        print ('too many args; can only accept one target dir')
    elif len(remaining_args) == 1:
        target_dir = remaining_args[0]
    target_dir_path = Path(target_dir)

    target_dir_actual_name = target_dir_path.resolve().name
    target_dir_parent_name = target_dir_path.resolve().parent.name
    archive_equivalent_location = pathlib.Path.home() / WEBPAGE_IMAGE_ARCHIVE / target_dir_parent_name / target_dir_actual_name
    csv_path = (target_dir_path.resolve().parent / target_dir_actual_name).with_suffix(".csv")

    renamings = dict([(f,f.name) for f in target_dir_path.iterdir() if f.is_file()])

    file_dates = {}
    for oldf, newn in renamings.items():
        file_date = datetime.fromtimestamp(oldf.lstat().st_mtime)
        oldf_stem = oldf.stem
        if TWO_DIGITS_FIRST_RE.match(oldf_stem):
            oldf_stem = oldf_stem[3:]
        archive_equivalent_f = (archive_equivalent_location / oldf_stem).with_suffix(".JPG")
        if not archive_equivalent_f.exists():
            archive_equivalent_f = (archive_equivalent_location / oldf_stem).with_suffix(".jpg")
        if not archive_equivalent_f.exists():
            archive_equivalent_f = (archive_equivalent_location / oldf_stem).with_suffix(".jpeg")
        #print (archive_equivalent_f)
        if archive_equivalent_f.exists():
            with open(archive_equivalent_f, 'rb') as image_file:
                tags = exifread.process_file(image_file)
                try:
                    file_date = tags["EXIF DateTimeOriginal"].values
                except:
                    file_date = datetime.fromtimestamp(archive_equivalent_f.lstat().st_mtime).strftime('%Y:%m:%d %H:%M:%S')
            #print ("AE file {} date {}".format(archive_equivalent_f, file_date))
        else:
            print ("can't find archive equivalent file {}".format(oldf))
            #fd = imgDate(oldf)
            #if fd is not None:
            #    file_date = fd
        
        file_dates[oldf] = file_date
        #print ("file {} date {}".format(oldf, file_dates[oldf]))
    files = [f[0] for f in renamings.items()]
    files.sort(key=lambda f: file_dates[f])
    #print (files)
    #print (file_dates)

    # strip first two digits if filename starts like dd_
    for oldf, newn in renamings.items():
        if not parsed_args.preserve_names and TWO_DIGITS_FIRST_RE.match(newn):
            renamings[oldf] = newn[3:]

    # fetch piwigo ids
    if not parsed_args.offline:
        pc = PiwigoConnector(BASE_URL + 'ws.php', '', '')
        piwigo_widget = {}
        for oldf, newn in renamings.items():
            # maybe we are not doing renamings...
            if TWO_DIGITS_FIRST_RE.match(newn):
                newn = newn[3:]
            id = pc.fetch_image_id(newn)
            if id is not None:
                cat_id = pc.fetch_first_category(id)
            else:
                cat_id = "YYY"

            piwigo_widget[oldf] = '?/{}/category/{}'.format(id, cat_id)

    for oldf, newn in renamings.items():
        new_index = files.index(oldf)*2
        new_name = newn
        if not parsed_args.preserve_names:
            new_name = "{:02d}_{}".format(new_index, newn)
            os.rename(oldf.name, new_name)

    with open(csv_path, "w") as csv:
        for oldf, newn in renamings.items():
            new_index = files.index(oldf)*2
            new_name = newn
            if not parsed_args.preserve_names:
                new_name = "{:02d}_{}".format(new_index, newn)
            if not parsed_args.offline:
                csv.write ("{},{}\n".format(new_name, piwigo_widget[oldf]))

if __name__ == '__main__':
    main()
