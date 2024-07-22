import cadwork
import attribute_controller as ac
import element_controller as ec
import utility_controller as uc
import visualization_controller as vc
import sys
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

plugin_directory = uc.get_plugin_path()
sys.path.append(plugin_directory)

import model.attributeRecord
import model.elementType
import model.geometryRecord
import dataReader.elementDataReader

USER_ATTRIBUTE_1 : int = 1

def build_element(geometry_data: model.geometryRecord.GeometryRecord, start_point: cadwork.point_3d, direction_vector: cadwork.point_3d, height_vector: cadwork.point_3d) -> int:
    if geometry_data.element_type == model.elementType.ElementType.BEAM:
        return ec.create_rectangular_beam_vectors(geometry_data.width, geometry_data.height, geometry_data.length, start_point, direction_vector, height_vector)
    if geometry_data.element_type == model.elementType.ElementType.PANEL:
        return ec.create_rectangular_panel_vectors(geometry_data.width, geometry_data.height, geometry_data.length, start_point, direction_vector, height_vector)
    raise ValueError('Unknown element type')


def assign_attributes(element_id: int, attribute_data: model.attributeRecord.AttributeRecord) -> None:
    ac.set_name([element_id], attribute_data.name)
    ac.set_user_attribute([element_id], USER_ATTRIBUTE_1, attribute_data.user1)
    vc.set_color([element_id], attribute_data.color)




def plugin_main():
    
    geometry_data = dataReader.elementDataReader.read_geometry_data(fr'{plugin_directory}/data/test_data_geometry.csv')
    logger.info(f"Read geometry data: {geometry_data}")
    attribute_data = dataReader.elementDataReader.read_attribute_data(fr'{plugin_directory}/data/test_data_attributes.csv')
    logger.info(f"Read attribute data: {attribute_data}")

    distance_between_elements = 0
    for element_primary_key, values in geometry_data.items():
        logger.info(f"Building element {element_primary_key}")
        element_id = build_element(values, cadwork.point_3d(0, distance_between_elements, 0), cadwork.point_3d(1, 0, 0), cadwork.point_3d(0, 1, 0))
        logger.info(f"""Assigning attributes to created 
                    {"BEAM" if values.element_type == model.elementType.ElementType.BEAM else "PANEL"} element {element_id}""")
        assign_attributes(element_id, attribute_data[element_primary_key])
        distance_between_elements += values.height + 1_000


if __name__ == '__main__':
    plugin_main()