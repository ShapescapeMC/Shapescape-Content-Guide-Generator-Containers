(installation)=
# Installation

## Steps

### 1. Install the filter
Use the following command
```
regolith install shapescape_cgg_containers
```

You can alternatively use this command:
```
regolith install github.com/ShapescapeMC/Shapescape-Content-Guide-Generator-Containers/shapescape_cgg_containers
```

### 2. Add filter to a profile
Add the filter to the `filters` list in the `config.json` file of the Regolith project and add the settings:

```json
{
  "filter": "shapescape_cgg_containers"
}
```