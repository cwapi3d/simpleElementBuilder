import sys
import cadwork
import utility_controller as uc

import csv
import logging

plugin_directory = uc.get_plugin_path()
sys.path.append(plugin_directory)

import model.attributeRecord
import model.elementType
import model.geometryRecord

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def read_geometry_data(csv_file):
    records: dict = {}
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            try:
                record = model.geometryRecord.GeometryRecord(
                    id=int(row['id']),
                    element_type=model.elementType.ElementType(int(row['element_type'])),
                    width=float(row['width']),
                    height=float(row['height']),
                    length=float(row['length'])
                )
                records[record.id] = record
                logger.debug(f"Read geometry record: {record}")
            except KeyError as e:
                logger.error(f"Missing data for key: {e} in row: {row}")
            except ValueError as e:
                logger.error(f"Invalid data format: {e} in row: {row}")
    return records


def read_attribute_data(csv_file):
    records: dict = {}
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                record = model.attributeRecord.AttributeRecord(
                    id=int(row['id']),
                    name=row['name'],
                    color=int(row['color']),
                    user1=row['user1']
                )
                records[record.id] = record
                logger.debug(f"Read attribute record: {record}")
            except KeyError as e:
                logger.error(f"Missing data for key: {e} in row: {row}")
            except ValueError as e:
                logger.error(f"Invalid data format: {e} in row: {row}")
    return records