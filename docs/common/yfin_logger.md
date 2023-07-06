# Global Logger Format

The Global Logger Format is a Python configuration that sets up logging for a project using the `logging` module. It reads a YAML configuration file to determine the logging settings such as log file name, log level, and log format. The configuration allows for easy customization and centralized logging across multiple modules.

## Prerequisites

Before using the Global Logger Format, ensure that you have the following dependencies installed:

- logging: This module is included in Python's standard library.
- yaml: `pip install pyyaml`

## Usage

To use the Global Logger Format, follow these steps:

1. Import the necessary modules:

```python
import logging
import yaml
```

2. Loading the logging configuration from a YAML file:
```python
with open('configs/yfin_etl.yaml', 'r', encoding='utf-8') as file:
    config = yaml.safe_load(file)
```

3. Reading the variables from the configuration:
```python
FILE_NAME = config['logging']['file']['filename']
ROOT_LEVEL = config['logging']['root']['level']
LOG_FORMAT = config['logging']['formatters']['yfin']['format']
```

4. Set up the logging configuration using basicConfig:
```python
logging.basicConfig(
    level=ROOT_LEVEL,
    filename=FILE_NAME,
    filemode='a',
    format=LOG_FORMAT
)
```

5. This configures the root logger with the specified log level, log file name, log file mode, and log format.

Get a logger instance for a specific module:
```python
logger = logging.getLogger(__name__)
```
This logger can be used within the module to log messages.

## Configuration
- The Global Logger Format relies on a YAML configuration file to specify the logging settings. The file should have the following structure:

```yaml
logging:
  file:
    filename: 'path/to/logfile.log'
  root:
    level: 'INFO'
  formatters:
    yfin:
      format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
```

- filename: Specifies the path and name of the log file.
- level: Sets the root log level (e.g., 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
- format: Defines the log message format using placeholders for various log record attributes.

Adjust the YAML configuration file according to your project's requirements.

## Logging Messages
To log messages using the configured logger, use the logger instance obtained 
```python
from logging.getLogger(__name__). For example:
```

## License
This project is licensed under the MIT License.