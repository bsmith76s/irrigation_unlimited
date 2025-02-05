"""Test irrigation_unlimited user configurations. Not exactly a test
   but a place to check if configuration files are valid and possibly
   debug them."""
import pytest
from datetime import timedelta, datetime
import json
import homeassistant.core as ha
from homeassistant.config import (
    load_yaml_config_file,
    async_process_ha_core_config,
)
from homeassistant.setup import async_setup_component

from custom_components.irrigation_unlimited.irrigation_unlimited import (
    IUCoordinator,
)
from custom_components.irrigation_unlimited.const import (
    DOMAIN,
    COORDINATOR,
    SERVICE_TIME_ADJUST,
)
from custom_components.irrigation_unlimited.__init__ import CONFIG_SCHEMA
from tests.iu_test_support import (
    begin_test,
    check_summary,
    finish_test,
    no_check,
    quiet_mode,
    run_for,
    run_until,
    test_config_dir,
)

quiet_mode()


@pytest.mark.skip
async def test_config(hass: ha.HomeAssistant, skip_dependencies, skip_history):
    """Test loading of a config."""

    """Prevent checking results. Helpful for just outputting results"""
    # no_check()

    full_path = test_config_dir + "test_config.yaml"
    config = CONFIG_SCHEMA(load_yaml_config_file(full_path))
    if ha.DOMAIN in config:
        await async_process_ha_core_config(hass, config[ha.DOMAIN])
    await async_setup_component(hass, DOMAIN, config)
    await hass.async_block_till_done()
    coordinator: IUCoordinator = hass.data[DOMAIN][COORDINATOR]

    """Run a single test"""
    # start_time = await begin_test(1, coordinator)
    # print(json.dumps(coordinator.as_dict(), default=str))
    # await finish_test(hass, coordinator, start_time, True)

    """Run all tests"""
    # for t in range(coordinator.tester.total_tests):
    #     start_time = await begin_test(t + 1, coordinator)
    #     await finish_test(hass, coordinator, start_time, True)

    """Run a test with a service call"""
    # start_time = await begin_test(1, coordinator)
    # await hass.services.async_call(
    #     DOMAIN,
    #     SERVICE_TIME_ADJUST,
    #     {
    #         "entity_id": "binary_sensor.irrigation_unlimited_c1_m",
    #         "sequence_id": 1,
    #         "zones": 0,
    #         "actual": "00:10",
    #     },
    #     True,
    # )
    # await finish_test(hass, coordinator, start_time, True)

    """Run to a point in time"""
    # start_time = await begin_test(1, coordinator)
    # next_time = await run_until(
    #     hass,
    #     coordinator,
    #     start_time,
    #     datetime.fromisoformat("2021-01-04 06:02:00+00:00"),
    #     True,
    # )
    # await finish_test(hass, coordinator, next_time, True)

    """Run for a period of time"""
    # start_time = await begin_test(1, coordinator)
    # next_time = await run_for(
    #     hass, coordinator, start_time, timedelta(minutes=15), True
    # )
    # await finish_test(hass, coordinator, next_time, True)

    check_summary(full_path, coordinator)
