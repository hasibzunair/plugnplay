import os

"""
Convert YOLO labels to Vertex AI format. Sample data is 
available in https://github.com/hasibzunair/my-lfs/releases/tag/v1-datasets.
"""


def yolo_to_vertices(yolo_label_path, img_width=1280, img_height=720):
    with open(yolo_label_path, "r") as f:
        lines = f.readlines()

    vertices_list = []
    for line in lines:
        line = line.strip().split()
        class_id = int(line[0])
        x_center = float(line[1])
        y_center = float(line[2])
        width = float(line[3])
        height = float(line[4])

        # Convert YOLO format to vertices
        x_min = int((x_center - width / 2) * img_width)
        y_min = int((y_center - height / 2) * img_height)
        x_max = int((x_center + width / 2) * img_width)
        y_max = int((y_center + height / 2) * img_height)

        # Normalize coordinates
        x_min = x_min / img_width
        y_min = y_min / img_height
        x_max = x_max / img_width
        y_max = y_max / img_height

        # x_min, y_min, x_max, y_max = min_max_normalize([x_min, y_min, x_max, y_max])

        vertices_list.append((class_id, x_min, y_min, x_max, y_max))

    return vertices_list


# Map values to int and reverse
label2int = {"rim": 0, "basketball": 1, "person": 2}
int2label = {value: key for key, value in label2int.items()}

# read text file label
# convert to desired format
# make string for each class object
# save in txt file

file = open("../datasets/vertex_labels.csv", "w")

for i in range(12):
    norm_vertices = yolo_to_vertices(f"../datasets/labels/{i}.txt")
    for j in range(len(norm_vertices)):
        output = f"gs://ai-canada-datasets/data/basketball_datasetv1/{i}.jpg,{int2label[norm_vertices[j][0]]},{norm_vertices[j][1]},{norm_vertices[j][2]},,,{norm_vertices[j][3]},{norm_vertices[j][4]},,\n"
        print(output)
        file.write(output)

file.close()

# gs://ai-canada-datasets/data/basketball_datasetv1/0.jpg,2,0.3515625,0.3402777777777778,,,0.453125,0.9333333333333333,,
# gs://ai-canada-datasets/data/basketball_datasetv1/0.jpg,1,0.45546875,0.5305555555555556,,,0.50234375,0.625,,
# gs://ai-canada-datasets/data/basketball_datasetv1/0.jpg,0,0.1046875,0.18194444444444444,,,0.1609375,0.2972222222222222,,
