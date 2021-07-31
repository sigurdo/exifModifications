# EXIF modification

A collection of scripts for modifying EXIF data on a set of images

## `modify_datetime.py`
Modify the datetime of a set of images filtered on an the value of an EXIF attribute.

First, put the images you want to modify in `images_in`. Output will be put in `images_out`.

### Basic example of usage:
```
python modify_datetime.py -41 model "Canon EOS 1100D"
```
The following command will reduce the datetime of all images with model set to "Canon EOS 1100D" by 41 minutes. It will delete all files in images_out before producing any output. It will also only take in images with a `.jpg` extension.

### Optional arguments:
- `--delete-first`
    - If provided, all files in images_out will be deleted before running the algorithm.
- `--filter-extensions`
    - If provided, only images with one of the provided file extensions will be modified.
    - Example:
        ```
        --filter-extensions .jpg .png
        ```
        will only modify `.jpg` and `.png` images. This is case sensitive.