import os
from dataclasses import field
from typing import Optional

import marshmallow_dataclass

from starkware.starkware_utils.config_base import Config
from starkware.starkware_utils.marshmallow_dataclass_fields import additional_metadata
from starkware.storage.adversarial_gated_storage_types import AdversarialParams

GENERAL_STORAGE_CONFIG_FILE_NAME = "general_storage_config.yml"
DOCKER_GENERAL_STORAGE_CONFIG_PATH = os.path.join("/", GENERAL_STORAGE_CONFIG_FILE_NAME)


@marshmallow_dataclass.dataclass
class GeneralStorageConfig(Config):
    adversarial_gated_storage_params: Optional[AdversarialParams] = field(
        metadata=additional_metadata(
            description=(
                "Parameters for the AdversarialGatedStorage, which simulates adversarial failures "
                "on set operations."
            ),
        ),
        default=None,
    )
