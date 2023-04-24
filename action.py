import csv
import argparse
import openpyxl

def calculate_action_man_hours(input_csv_file):
    joint_action_man_hours = []

    with open(input_csv_file, 'r') as f:
        csv_reader = csv.reader(f, delimiter=';')
        for row in csv_reader:
            if not row:
                continue

            human_data = []
            for human_str in row:
                human_parts = human_str.strip().split("BodyPart:")
                human_parts.pop(0)  # Remove the empty string before the first "BodyPart:"
                human_dict = {}
                for part_str in human_parts:
                    part_id, part_coords = part_str.split('-', 1)
                    coords_str = part_coords.split(')')[0].strip('(').split(',')
                    coords = (float(coords_str[0]), float(coords_str[1]))
                    human_dict[int(part_id)] = coords
                human_data.append(human_dict)

            squared_deviations = [0] * 18
            for human in human_data:
                for part_id, coords in human.items():
                    squared_deviations[part_id] += coords[0] ** 2 + coords[1] ** 2

            joint_action_man_hours.append(squared_deviations)

    return joint_action_man_hours


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate action man-hours from CSV file")
    parser.add_argument("input_csv_file", type=str, help="Input CSV file with human joint data")
    parser.add_argument("output_xlsx_file", type=str, help="Output XLSX file with action man-hours data")
    args = parser.parse_args()

    input_csv_file = args.input_csv_file
    output_xlsx_file = args.output_xlsx_file

    action_man_hours = calculate_action_man_hours(input_csv_file)

    wb = openpyxl.Workbook()
    ws = wb.active

    for amh in action_man_hours:
        ws.append(amh)

    wb.save(output_xlsx_file)

    print(f"Action man-hours data has been saved to {output_xlsx_file}.")
