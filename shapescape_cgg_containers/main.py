import amulet
from collections import defaultdict
from amulet.api.block_entity import BlockEntity
from amulet.api.level import World
from amulet.api.errors import ChunkLoadError, ChunkDoesNotExist
from pathlib import Path
import time
import sys
import os
import json

DIMENSIONS = ["minecraft:overworld", "minecraft:the_nether", "minecraft:the_end"]
ROOT_PATH = "../"
CGG_CONTAINERS_PATH = "data/shapescape_content_guide_generator/templates/containers.md"
CGG_INTERNAL_CONTAINERS_PATH = (
    "data/shapescape_content_guide_generator/templates/interal_containers.md"
)
CGG_DEBUG_PATH = "data/shapescape_content_guide_generator/cg_containers_debug.md"

IRRELEVANT_BLOCK_ENTITIES = [
    "sign",
    "banner",
    "bell",
    "spawner",
    "chiseled_bookshelf",
    "decorated_pot",
    "flower_pot",
    "beehive",
    "cauldron",
    "command_block",
    "head",
    "piston",
    "brewing_stand",
    "bed",
    "brushable_block",
    "enchanting_table",
]

containers = {}
all_containers = {}

unknown_block_entity_types = []


class CGContainersError(Exception):
    pass


def print_red(text: str):
    """Prints text in red."""
    for t in text.split("\n"):
        print("\033[91m {}\033[00m".format(t))


def get_items_from_container(block_entity: BlockEntity) -> dict | str:
    items = defaultdict(lambda: 0)
    if "Items" in block_entity.nbt.tag.py_dict["utags"].py_dict:
        for slot in block_entity.nbt.tag.py_dict["utags"].py_dict["Items"].py_list:
            items[slot.py_dict["Name"].py_str] += slot.py_dict["Count"].py_int
    else:
        items = "undefined"
    return items


def read_containers(level: World, dimension: str):
    local_containers = []
    all_local_containers = []
    total_chunks = len(level.all_chunk_coords(dimension))
    print()
    print(f"INFO - Starting to load {total_chunks} chunks in {dimension} dimension.")
    for c, chunk_coordinate in enumerate(level.all_chunk_coords(dimension)):
        # read a chunk
        if c % 100 == 0:
            print(f"INFO - Loaded {c}/{total_chunks} chunks in {dimension} dimension.")
        try:
            chunk = level.get_chunk(chunk_coordinate[0], chunk_coordinate[1], dimension)
        except ChunkDoesNotExist:
            # if a chunk is accessed that does not exist this code will be run.
            print("Chunk does not exist")
        except ChunkLoadError:
            # if a chunk is corrupt, is in an unsupported format or
            # just did not load for some reason this code will run.
            # This error would also catch ChunkDoesNotExist if the previous except block did not exist.
            print("Chunk load error")
        else:
            # if no errors occurred.
            block_entities = chunk.block_entities
            for block_entity in block_entities:
                if block_entity.namespace == "universal_minecraft":
                    if block_entity.base_name == "chest":
                        local_containers.append(
                            {
                                "type": block_entity.base_name,
                                "coordinates": block_entity.location,
                                "chunk": chunk_coordinate,
                                "items": get_items_from_container(block_entity),
                            }
                        )
                        all_local_containers.append(
                            {
                                "type": block_entity.base_name,
                                "coordinates": block_entity.location,
                                "chunk": chunk_coordinate,
                                "items": get_items_from_container(block_entity),
                            }
                        )
                    elif block_entity.base_name == "barrel":
                        local_containers.append(
                            {
                                "type": block_entity.base_name,
                                "coordinates": block_entity.location,
                                "chunk": chunk_coordinate,
                                "items": get_items_from_container(block_entity),
                            }
                        )
                        all_local_containers.append(
                            {
                                "type": block_entity.base_name,
                                "coordinates": block_entity.location,
                                "chunk": chunk_coordinate,
                                "items": get_items_from_container(block_entity),
                            }
                        )
                    elif block_entity.base_name == "shulker_box":
                        local_containers.append(
                            {
                                "type": block_entity.base_name,
                                "coordinates": block_entity.location,
                                "chunk": chunk_coordinate,
                                "items": get_items_from_container(block_entity),
                            }
                        )
                        all_local_containers.append(
                            {
                                "type": block_entity.base_name,
                                "coordinates": block_entity.location,
                                "chunk": chunk_coordinate,
                                "items": get_items_from_container(block_entity),
                            }
                        )
                    elif block_entity.base_name == "trapped_chest":
                        local_containers.append(
                            {
                                "type": block_entity.base_name,
                                "coordinates": block_entity.location,
                                "chunk": chunk_coordinate,
                                "items": get_items_from_container(block_entity),
                            }
                        )
                        all_local_containers.append(
                            {
                                "type": block_entity.base_name,
                                "coordinates": block_entity.location,
                                "chunk": chunk_coordinate,
                                "items": get_items_from_container(block_entity),
                            }
                        )
                    elif block_entity.base_name == "furnace":
                        all_local_containers.append(
                            {
                                "type": block_entity.base_name,
                                "coordinates": block_entity.location,
                                "chunk": chunk_coordinate,
                                "items": get_items_from_container(block_entity),
                            }
                        )
                    elif block_entity.base_name == "dropper":
                        all_local_containers.append(
                            {
                                "type": block_entity.base_name,
                                "coordinates": block_entity.location,
                                "chunk": chunk_coordinate,
                                "items": get_items_from_container(block_entity),
                            }
                        )
                    elif block_entity.base_name == "hopper":
                        all_local_containers.append(
                            {
                                "type": block_entity.base_name,
                                "coordinates": block_entity.location,
                                "chunk": chunk_coordinate,
                                "items": get_items_from_container(block_entity),
                            }
                        )
                    elif block_entity.base_name == "dispenser":
                        all_local_containers.append(
                            {
                                "type": block_entity.base_name,
                                "coordinates": block_entity.location,
                                "chunk": chunk_coordinate,
                                "items": get_items_from_container(block_entity),
                            }
                        )
                    elif block_entity.base_name == "smoker":
                        all_local_containers.append(
                            {
                                "type": block_entity.base_name,
                                "coordinates": block_entity.location,
                                "chunk": chunk_coordinate,
                                "items": get_items_from_container(block_entity),
                            }
                        )
                    elif block_entity.base_name == "blast_furnace":
                        all_local_containers.append(
                            {
                                "type": block_entity.base_name,
                                "coordinates": block_entity.location,
                                "chunk": chunk_coordinate,
                                "items": get_items_from_container(block_entity),
                            }
                        )
                    elif block_entity.base_name in IRRELEVANT_BLOCK_ENTITIES:
                        continue
                    else:
                        unknown_block_entity_types.append(block_entity.base_name)
                        continue
                else:
                    print("Non vanilla block entities are currently not supported.")
    print(
        f"INFO - Loaded {total_chunks}/{total_chunks} chunks in {dimension} dimension."
    )
    containers[dimension] = local_containers
    all_containers[dimension] = all_local_containers


def format_all_containers(dimension: str, container_dict=dict) -> list[str]:
    data = []
    data.append(
        "### " + str(dimension.replace("minecraft:", "").replace("_", " ").title())
    )
    if len(container_dict) == 0:
        data.append("- No containers in this dimenstion")
    else:
        for container in container_dict:
            if container["items"] == "loot_table":
                continue
            if (
                container["type"] in ["chest", "trapped_chest", "shulker_box", "barrel"]
                and len(container["items"]) == 0
            ):
                item_description = (
                    "- ❌**"
                    + container["type"].replace("_", " ").title()
                    + "** at "
                    + str(container["coordinates"]).replace(",", "")
                    + " with items:"
                )
            elif len(container["items"]) == 0:
                item_description = (
                    "- 🟡**"
                    + container["type"].replace("_", " ").title()
                    + "** at "
                    + str(container["coordinates"])
                    + " with items:"
                )
            else:
                item_description = (
                    "- ✔️**"
                    + container["type"].replace("_", " ").title()
                    + "** at "
                    + str(container["coordinates"])
                    + " with items:"
                )
            data.append(item_description)

            if container["items"] == "undefined":
                (
                    print(
                        "WARN: " + container["type"].title() + " at ("
                        ", ".join(map(str, container["coordinates"])) + ") is empty!"
                    )
                )
                data.append("\t - Container is empty!")
            elif len(container["items"]) == 0:
                data.append("\t - Container is empty!")
            else:
                # print(type(container["items"]))
                # print(dict(container["items"]))
                items = dict(container["items"])
                for item, count in items.items():
                    data.append("\t - " + str(count) + "x " + item)
        data.append("")
    return data


def format_containers(dimension: str, container_dict=dict) -> list[str]:
    data = []
    data.append(
        "### " + str(dimension.replace("minecraft:", "").replace("_", " ").title())
    )
    if len(container_dict) == 0:
        data.append("- No containers in this dimenstion")
    else:
        for container in container_dict:
            if container["items"] == "loot_table":
                continue
            item_description = (
                "- **"
                + container["type"].replace("_", " ").title()
                + "** at "
                + str(container["coordinates"]).replace(",", "")
                + " with items:"
            )

            data.append(item_description)
            if container["items"] == "undefined":
                (
                    print(
                        "WARN: " + container["type"].title() + " at ("
                        ", ".join(map(str, container["coordinates"])) + ") is empty!"
                    )
                )
                data.append("\t - Container is empty!")
            elif len(container["items"]) == 0:
                data.append("\t - Container is empty!")
            else:
                items = dict(container["items"])
                for item, count in items.items():
                    data.append("\t - " + str(count) + "x " + item)
        data.append("")
    return data


def write_containers_file():
    with open(CGG_CONTAINERS_PATH, "w", encoding="utf-8") as file:
        for containers_k, containers_v in containers.items():
            for line in format_containers(containers_k, containers_v):
                file.write(line + "\n")


def write_local_containers_file():
    with open(CGG_INTERNAL_CONTAINERS_PATH, "w", encoding="utf-8") as file:
        for containers_k, containers_v in all_containers.items():
            for line in format_all_containers(containers_k, containers_v):
                file.write(line + "\n")


def write_debug_file():
    with open(CGG_DEBUG_PATH, "w", encoding="utf-8") as file:
        file.write(
            "This Project has block_entity types that are unknown to the CG_Containers filter.\nPlease send this file to lars_rickert@shapescape.com l.\n\n"
        )
        for item in unknown_block_entity_types:
            file.write(item + "\n")


def main():
    start_time = time.time()

    try:
        root_dir = Path(os.environ["ROOT_DIR"])
    except KeyError:
        raise CGContainersError("Failed to load 'ROOT_DIR' from environment variables.")

    exported_world = None

    # Open file that sits in root_dir / "packs/release_config.json" and extract the exported_world variable
    try:
        with open(root_dir / ROOT_PATH / "pack/release_config.json", "r") as file:
            release_config = json.load(file)
            exported_world = release_config["exported_world"]
    except FileNotFoundError:
        raise CGContainersError("Failed to load 'pack/release_config.json' file.")
    except KeyError:
        raise CGContainersError(
            "Failed to load 'exported_world' from 'packs/release_config.json' file."
        )
    if exported_world != None:
        # load the level
        level: World = amulet.load_level(
            root_dir / ROOT_PATH / "regolith/worlds" / exported_world
        )

        # read data from each dimension
        for dimension in DIMENSIONS:
            read_containers(level=level, dimension=dimension)

        # close the world
        level.close()

        write_local_containers_file()

        write_containers_file()

        if len(unknown_block_entity_types) > 0:
            write_debug_file()

        # print the time
        print(
            "Total execution time: "
            + str(round((time.time() - start_time), 2))
            + " seconds."
        )
    else:
        raise CGContainersError("Failed to load 'exported_world' from release_config.")


if __name__ == "__main__":
    try:
        main()
    except CGContainersError as e:
        print_red(str(e))
        sys.exit(1)
