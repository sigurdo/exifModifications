import argparse
import exif
import os
import datetime

parser = argparse.ArgumentParser(description="Modify the datetime of a set of images filtered on an the value of an EXIF attribute")
parser.add_argument("--delete-first", action="store_true", help="Deletes all images in images_out before saving new ones")
parser.add_argument("--filter-extensions", type=str, metavar="ACCEPTED_EXTENSIONS", nargs="*", help="Specify file extensions to perform modification on. If not given, all file extensions will be accepted")
parser.add_argument("timedelta", type=int, help="Minutes to add (use a - to subtract)")
parser.add_argument("filter_attribute", type=str, help="EXIF attribute to filter which images to modify")
parser.add_argument("filter_value", type=str, help="Value of filter_attribute of images to modify")

args = parser.parse_args()

if not os.path.exists("images_out"): os.mkdir("images_out")
if args.delete_first:
    for filename in os.listdir("images_out"):
        if filename != ".gitkeep":
            os.remove(os.path.join("images_out", filename))

def add_minutes(image, minutes):
    time_format = "%Y:%m:%d %H:%M:%S"
    time = datetime.datetime.strptime(image.datetime_original, time_format)
    new_time = time + datetime.timedelta(minutes=minutes)
    image.datetime = datetime.datetime.strftime(new_time, time_format)
    image.datetime_original = datetime.datetime.strftime(new_time, time_format)
    image.datetime_digitalized = datetime.datetime.strftime(new_time, time_format)

for root, dirs, files in os.walk("images_in", topdown=False):
    for filename in files:
        if filename == ".gitkeep": continue
        if args.filter_extensions == None or os.path.splitext(filename)[1] in args.filter_extensions:
            with open(os.path.join(root, filename), "rb") as image_file:
                image = exif.Image(image_file)
            if image.get(args.filter_attribute) == args.filter_value:
                add_minutes(image, args.timedelta)
                with open(os.path.join("images_out", filename), "wb") as image_file:
                    image_file.write(image.get_file())
