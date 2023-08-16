import os
import json
import argparse

""" 
Convert Vertex AI object detection labels into YOLO format.
"""


def get_args_parser(add_help=True):
    """Usage: args = get_args_parser()"""
    parser = argparse.ArgumentParser(description="Video Resizer", add_help=add_help)
    parser.add_argument(
        "--jsonpath",
        type=str,
        default="./datasets/vertex_dataset/basketball_datasetv1/labels/data-00001-of-00001.jsonl",
        help="the path to jsonl file from gcp.",
    )
    parser.add_argument(
        "--dest",
        type=str,
        default="./datasets/vertex_dataset/basketball_datasetv1/labels/yolo_labels/",
        help="the path to save yolo labels.",
    )
    args = parser.parse_args()
    return args


def convert_bbox_to_yolo(xmin, xmax, ymin, ymax, img_width=1280, img_height=720):

    # Un-normalize coordinates
    xmin = xmin * img_width
    ymin = ymin * img_height
    xmax = xmax * img_width
    ymax = ymax * img_height

    # Calculate center point of bounding box
    x_center = (xmin + xmax) / 2.0
    y_center = (ymin + ymax) / 2.0

    # Calculate width and height of bounding box
    width = xmax - xmin
    height = ymax - ymin

    # Normalize values by image width and height
    x_center /= img_width
    y_center /= img_height
    width /= img_width
    height /= img_height

    x_center = round(x_center, 6)
    y_center = round(y_center, 6)
    width = round(width, 6)
    height = round(height, 6)

    return x_center, y_center, width, height


if __name__ == "__main__":

    args = get_args_parser()

    # Make folder for labels
    if not os.path.exists(f"{args.dest}"):
        os.makedirs(f"{args.dest}")

    # Map values to int and reverse
    label2int = {"rim": 0, "basketball": 1, "person": 2}

    # Convert to YOLO format
    with open(args.jsonpath, "r") as json_file:
        json_list = list(json_file)

    # read json contents
    for json_str in json_list[:]:
        result = json.loads(json_str)

        # read img path, obj name and labels
        img_path = result["imageGcsUri"]
        labels_list = []  # class name, bbox coordinates
        annots = result["boundingBoxAnnotations"]
        for annot in annots:
            cls_name = label2int[annot["displayName"]]

            # yolo format
            center_x, center_y, bbox_width, bbox_height = convert_bbox_to_yolo(
                annot["xMin"], annot["xMax"], annot["yMin"], annot["yMax"]
            )
            labels_list.append([cls_name, center_x, center_y, bbox_width, bbox_height])

            # Make YOLO labels
            fn = img_path.split("/")[-1][:-4]
            with open(f"{args.dest}/{fn}.txt", "w") as f:
                for item in labels_list:
                    f.write(f"{item[0]} {item[1]} {item[2]} {item[3]} {item[4]}\n")

            # Make classes.txt
            with open(f"{args.dest}/classes.txt", "w") as f:
                for item in list(label2int.keys()):
                    f.write(f"{item}\n")
