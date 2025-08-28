# Population-Weighted Spatial Distribution Tool

## Overview

This ArcGIS Pro tool solves a common problem in spatial analysis: **messy address data that gets clustered at zip code centroids**. When addresses are incomplete, geocoders often default to placing points at the zip code's center, creating misleading 'superclusters' that completely hide the true spatial distribution of the data.

## The Problem


When addresses are incomplete, geocoders often default to placing a point at the zipcode's center. This creates misleading 'superclusters' on the map and completely hides the true spatial distribution of the data. (In this example: 30 points in a zip code centroid)

## The Solution: Population-Weighted Distribution

Instead of piling points onto a single centroid, this process redistributes them using census block data to place each point in a location that reflects where people probably live within that zip code. If a neighborhood is more populated, it has a higher chance of receiving a point.

## How It Works

The workflow uses the "Create Spatial Sampling Location" tool, configured for stratified sampling proportional to a population field. A Python script automates the process by:

1. **Counting** the number of faulty geocodes
2. **Telling** the tool how many new points to generate
3. **Transferring** the original attributes to these new, more realistic locations


## The Result


We go from 30 points stacked on one meaningless centroid to 30 points distributed realistically across the area, providing a much more accurate foundation for analysis.

## Features

- **Dual Data Source Support**: Works with both local census layers and web services
- **Precise Intersection**: Uses a robust "filter locally" pattern for web service queries to ensure high precision
- **Attribute Preservation**: Maintains all original data attributes while redistributing spatial locations
- **Automated Workflow**: Streamlines the entire process from input to output
- **Background Processing**: Can run in the background for large datasets

## Requirements

- ArcGIS Pro 2.8 or later
- Python 3.x
- `arcgis` Python package
- Internet connection (for web service option)

## Installation

1. Download the `IntelligentDistribution_v2.pyt` file
2. Place it in your ArcGIS Pro toolbox directory or any accessible location
3. Add the toolbox to ArcGIS Pro:
   - Open ArcGIS Pro
   - Go to the Geoprocessing pane
   - Click on "Toolboxes" tab
   - Right-click and select "Add Toolbox"
   - Navigate to and select the `.pyt` file

## Usage

### Input Parameters

1. **Points to Distribute**: Your clustered point layer (e.g., geocoded addresses)
2. **Area of Interest (AOI)**: The boundary within which to distribute points
3. **Output Distributed Points**: Where to save the redistributed points
4. **Census Data Source**: Choose between local layer or web service
5. **Local Census Layer**: Your local census data (if using local option)
6. **Census Web Service URL**: URL for web-based census data (if using web service)
7. **Population Field**: Field name containing population data (default: "P0010001")

### Workflow Steps

1. **Prepare Census Study Area**: Intersects census data with your AOI
2. **Count Input Records**: Determines how many points need redistribution
3. **Create New Locations**: Generates spatially distributed points based on population density
4. **Transfer Attributes**: Preserves all original data attributes
5. **Cleanup**: Removes temporary files and fields

## Technical Details

The tool implements a sophisticated workflow that:

- **Queries web services efficiently** by extent first, then performs precise local intersection
- **Handles both shapefiles and geodatabases** with automatic OID field detection
- **Preserves data integrity** through careful field management and cleanup
- **Provides detailed progress messages** for monitoring and debugging

## Use Cases

- **Address Data Cleaning**: Redistribute clustered geocoded addresses
- **Demographic Analysis**: Create realistic population-weighted samples
- **Service Planning**: Distribute service locations based on population density
- **Research Studies**: Generate spatially representative samples for analysis

## Contributing

This tool addresses a universal issue that needs an out-of-the-box solution. We welcome feedback, improvements, and contributions from the GIS community.

### Potential Improvements

- Support for additional census data sources
- Integration with other geocoding services
- Batch processing capabilities
- Custom weighting schemes beyond population

## Author

**Jhonatan Garrido-Lecca**

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or contributions, please open an issue on this GitHub repository.

---

*This tool transforms clustered, meaningless point data into spatially representative distributions that accurately reflect real-world population patterns.*
