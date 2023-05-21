import json
import os

def restructure_dataset(input_file, output_file):
    with open(input_file, 'r') as file:
        dataset = json.load(file)

    restructured_dataset = []
    for image in dataset["images"]: #your initial structure can vary
        restructured_image = {
            "filename": image["filename"], #edit the parameters and indentation for your liking in this block
            "title": image["title"],
            "sentences": [{"tokens": image["sentences"][0]["tokens"]}],
            "image_url": image["image_url"],
            "split": image["split"]
        }
        restructured_dataset.append(restructured_image)

    with open(output_file, 'w') as file:
        json.dump(restructured_dataset, file, indent=2)

# Example usage
desktop_path = os.path.expanduser("~/Desktop") #place file on desktop or edit "~/Desktop" to your current file location
input_file = os.path.join(desktop_path, 'your_dataset.json')
output_file = os.path.join(desktop_path, 'restructured_dataset.json')
restructure_dataset(input_file, output_file)
