# Usage

A filter reads all containers of a level and prints them in a content guide generator template file. This is made for projects using haze.

The tool creates up to 3 files:

../regolith/filters_data/shapescape_content_guide_generator/templates/containers
../regolith/filters_data/shapescape_content_guide_generator/templates/internal_containers
../regolith/filters_data/shapescape_content_guide_generator/cg_containers_debug

- The container file could look like this:
  This file is used in the content guide. It only shows the containers that are required to be filled.
  ``` markdown
  ### Overworld
  - **Chest** at (-176 86 -72) with items:
  	 - 5x minecraft:pumpkin_seeds
  	 - 15x minecraft:potato
	   - 4x minecraft:iron_nugget
  	 - 5x minecraft:bread
  
  ### The Nether
  - No containers in this dimenstion
  
  ### The End
  - **Chest** at (-275 112 -125) with items:
  	 - Container is empty!
  ```

- The internal_containers could look like this:
  It is only visible to us and shows what still has to be done, and also shows non mandatory containers that are optional to be filled. 
  ✔️ Means the container has content.
  🟡 Container is empty but is not required to be filled.
  ❌ Container is empty and needs to be filled. 

  ``` markdown
  ### Overworld
  - ✔️**Chest** at (-275, 112, -125) with items:
  	 - 7x minecraft:spruce_log
  	 - 4x minecraft:bread
  	 - 3x minecraft:pumpkin_seeds
  	 - 4x minecraft:potato

  ### The Nether
  - 🟡**Furnace** at (-166, 75, -80) with items:
  	 - Container is empty!

  ### The End
  - ❌**Chest** at (-248, 101, -134) with items:
  	 - 35x minecraft:white_wool
  ```

## Optimizing the tool
The is generally quite slow as it has to go through every chunk in the world. Optimizing the world for the tool can have a big impact on speed. To optimize it, we reuploaded the bedrock world to chunker and pruned all unnecessary chunks, getting the number down to 4.000 chunks which speed up the tool to roughly 4 minute load time. Pruning in general is good, as it will reduce the file size of the world and thus players with low bandwith will have a faster download of the map.

## Good to know
The way containers work in Minecraft work is that each block in the world that has a container has their individual container. That means for double chests, one chests container in code is the top half and one is the bottom. If you do not have an item in either top or bottom, the tool will say the chest is empty, as from a code perspective it is. So just make sure that there are items in the top and bottom half for doubled chests to avoid the filter saying that the chest is empty.

