import json
from glob import glob
from time import sleep
from typing import Any, cast

import pytest
from pages.configs.operation_types import OperationType
from pytest import FixtureRequest


# TODO: decide weather to abstract out a base test class
class TestReceipt:
    @pytest.fixture(scope='class')
    def page(self, request: FixtureRequest):
        """ Selenium driver with scraper """
        environment: str = request.config.getoption('--environment')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        driver_arg: str = request.config.getoption('--window')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        page: OperationType
        if driver_arg:
            page = OperationType(driver_arg)
        else:
            page = OperationType()

        if environment == 'staging':
            page.login_staging()

        if environment == 'production':
            page.login_prod()

        if environment == 'uat':
            page.login_uat()
        return page

    @pytest.fixture(
        scope='class',
        params=glob(
            'testcases_json/configs/operation_types/receipt/*.json'
        )
    )
    def data(self, request: FixtureRequest, page: OperationType, environment: str) -> dict[str, Any]:  # noqa: E501
        """Paramitize for multiple json test cases"""
        fp: str = cast(str, request.param)
        with open(fp, 'r') as file:
            data: dict[str, Any] = json.load(file)
            if environment == 'staging':
                page.navigate(cast(str, data['staging_url']))

            if environment == 'production':
                page.navigate(cast(str, data['production_url']))

            if environment == 'uat':
                page.navigate(cast(str, data['uat_url']))

            sleep(0.5)
            return data

# ============ Tests ============ #
    def test_name(self, page: OperationType, data: dict[str, Any]):
        correct_val: str = data['name']
        val: str | None = page.get_name()
        assert val == correct_val, 'Name is not configured correctly'

    # ============ General Tab ============ #
    def test_type_opt(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['type_of_operation']
        val: str = page.get_type_opt()
        assert val == correct_val, (
            f'Type of operation is incorrect: {data['name']}'
        )

    def test_seq_prefix(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['sequence_prefix']
        val: str | None = page.get_seq_prefix()
        assert val == correct_val, (
            f'Sequence prefix is incorrect {data['name']}'
        )

    def test_barcode(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['barcode']
        val: str | None = page.get_barcode()
        assert val == correct_val, f'Barcode is incorrect: {data['name']}'

    def test_returns_type(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['returns_type']
        val: str | None = page.get_returns_type()
        assert val == correct_val, f'Retruns type is incorrect: {data['name']}'

    def test_create_backorder(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str | None = data['create_backorder']
        val: str = page.get_create_backorder()
        assert val == correct_val, (
            f'Create backorder is incorrect: {data['name']}'
        )

    def test_move_e_package(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['move_entire_packages']
        val: str = str(page.get_move_e_package())
        assert val == correct_val, (
            f'Move entire packages is incorrect: {data['name']}'
        )

    def test_default_src_location(
            self,
            page: OperationType,
            data: dict[str, Any]
    ):

        page.nav_gen_tab()
        correct_val: str = data['default_source_location']
        val: str | None = page.get_def_src()
        assert val == correct_val, (
            f'Def src location is incorrect: {data['name']}'
        )

    def test_default_dest_location(
            self,
            page: OperationType,
            data: dict[str, Any]
    ):

        page.nav_gen_tab()
        correct_val: str = data['default_destination_location']
        val: str | None = page.get_def_des()
        assert val == correct_val, (
            f'Def dest location is incorrect: {data['name']}'
        )

    def test_batch_transfer(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['automatic_batches']
        val: str = str(page.get_auto_batch())
        assert val == correct_val, f'Auto batch is incorrect: {data['name']}'

    # ============ Hardware Tab ============ #

    def test_delivery_slip(self, page: OperationType, data: dict[str, Any]):
        page.nav_hardware_tab()
        correct_val: str = data['delivery_slip']
        val: str = str(page.get_delivery_slip())
        assert val == correct_val, (
                f'Delivery slip is incorrect: {data['name']}'
        )

    def test_return_slip(self, page: OperationType, data: dict[str, Any]):
        page.nav_hardware_tab()
        correct_val: str = data['return_slip']
        val: str = str(page.get_return_slip())
        assert val == correct_val, (
                f'Return slip is incorrect: {data['name']}'
        )

    def test_product_labels(self, page: OperationType, data: dict[str, Any]):
        page.nav_hardware_tab()
        correct_val: str = data['product_labels']
        val: str = str(page.get_product_labels())
        assert val == correct_val, (
                f'Product labels is incorrect: {data['name']}'
        )

    def test_package_content(self, page: OperationType, data: dict[str, Any]):
        page.nav_hardware_tab()
        correct_val: str = data['package_content']
        val: str = str(page.get_package_content())
        assert val == correct_val, (
                f'Package content is incorrect: {data['name']}'
        )

    def test_package_label(self, page: OperationType, data: dict[str, Any]):
        page.nav_hardware_tab()
        correct_val: str = data['package_label']
        val: str = str(page.get_package_label())
        assert val == correct_val, (
                f'Package label is incorrect: {data['name']}'
        )

    # ============ Barcode Tab ============ #

    def test_product(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: str = data['product']
        val: str = str(page.get_product())
        assert val == correct_val, f'Product is incorrect: {data['name']}'

    def test_put_in_pack(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: str = data['put_in_pack']
        val: str = page.get_in_pack()
        assert val == correct_val, (
            f'Put in pack is incorrect: {data['name']}'
        )

    def test_dest_location(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: str = data['destination_location']
        val: str = page.get_des()
        assert val == correct_val, (
            f'Destination location is incorrect: {data['name']}'
        )

    def test_allow_full_picking(
            self,
            page: OperationType,
            data: dict[str, Any]
    ):

        page.nav_bar_tab()
        correct_val: str = data['allow_full_picking_validation']
        val: str = str(page.get_full_pick_validation())
        assert val == correct_val, (
            f'Full picking validation is incorrect: {data['name']}'
        )

    def test_full_categories(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: list[str] = data['picking_categories']
        val: list[str] = page.get_categories()
        assert val == correct_val, (
            f'Picking categories is incorrect: {data['name']}'
        )

    def test_pick_restricted(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: str = data['is_picking_restricted']
        val: str = str(page.get_pick_restricted())
        assert val == correct_val, (
            f'Is picking restricted is incorrect: {data['name']}'
        )

    def test_force_packed(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: str = data['force_all_products']
        val: str = str(page.get_force_pack())
        assert val == correct_val, (
            f'Force all products to be packed is incorrect: {data['name']}'
        )

    def test_force_dest(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: str = data['force_destination']
        val: str = str(page.get_force_des_all())
        assert val == correct_val, (
            f'Force a destinion on all products is incorrect: {data['name']}'
        )


class TestInternalTransfer:
    @pytest.fixture(scope='class')
    def page(self, request: FixtureRequest):
        """ Selenium driver with scraper """
        environment: str = request.config.getoption('--environment')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        driver_arg: str = request.config.getoption('--window')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        page: OperationType
        if driver_arg:
            page = OperationType(driver_arg)
        else:
            page = OperationType()

        if environment == 'staging':
            page.login_staging()

        if environment == 'production':
            page.login_prod()

        if environment == 'uat':
            page.login_uat()
        return page

    @pytest.fixture(
        scope='class',
        params=glob(
            'testcases_json/configs/operation_types/internal_transfer/*.json'
        )
    )
    def data(self,
             request: FixtureRequest,
             page: OperationType,
             environment: str
             ) -> dict[str, Any]:
        """Paramitize for multiple json test cases"""
        fp = cast(str, request.param)
        with open(fp, 'r') as file:
            data: dict[str, Any] = json.load(file)
            if environment == 'staging':
                page.navigate(cast(str, data['staging_url']))

            if environment == 'production':
                page.navigate(cast(str, data['production_url']))

            if environment == 'uat':
                page.navigate(cast(str, data['uat_url']))

            sleep(0.5)
            return data

# ============ Tests ============ #

    def test_name(self, page: OperationType, data: dict[str, Any]):
        correct_val: str = data['name']
        val: str | None = page.get_name()
        assert val == correct_val, 'Name is not configured correctly'

    # ============ General Tab ============ #

    def test_type_opt(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['type_of_operation']
        val: str = page.get_type_opt()
        assert val == correct_val, (
            f'Type of operation is incorrect: {data['name']}'
        )

    def test_seq_prefix(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['sequence_prefix']
        val: str | None = page.get_seq_prefix()
        assert val == correct_val, (
            f'Sequence prefix is incorrect {data['name']}'
        )

    def test_print_label(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['print_label']
        val: str = str(page.get_print_label())
        assert val == correct_val, f'Print label is incorrect {data['name']}'

    def test_barcode(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['barcode']
        val: str | None = page.get_barcode()
        assert val == correct_val, f'Barcode is incorrect: {data['name']}'

    def test_res_method(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['reservation_method']
        val: str | None = page.get_res_method()
        assert val == correct_val, (
            f'Reservation method is incorrect: {data['name']}'
        )

    def test_move_e_package(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['move_entire_packages']
        val: str = str(page.get_move_e_package())
        assert val == correct_val, (
            f'Move entire packages is incorrect: {data['name']}'
        )

    def test_create_backorder(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['create_backorder']
        val: str = page.get_create_backorder()
        assert val == correct_val, (
            f'Create backorder is incorrect: {data['name']}'
        )

    def test_default_src_location(self,
                                  page: OperationType,
                                  data: dict[str, Any]
                                  ):
        page.nav_gen_tab()
        correct_val: str = data['default_source_location']
        val: str | None = page.get_def_src()
        assert val == correct_val, (
            f'Def src location is incorrect: {data['name']}'
        )

    def test_default_dest_location(self,
                                   page: OperationType,
                                   data: dict[str, Any]
                                   ):
        page.nav_gen_tab()
        correct_val: str = data['default_destination_location']
        val: str | None = page.get_def_des()
        assert val == correct_val, (
            f'Def dest location is incorrect: {data['name']}'
        )

    def test_batch_transfer(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['automatic_batches']
        val: str = str(page.get_auto_batch())
        assert val == correct_val, f'Auto batch is incorrect: {data['name']}'

    # ============ Hardware Tab ============ #

    def test_delivery_slip(self, page: OperationType, data: dict[str, Any]):
        page.nav_hardware_tab()
        correct_val: str = data['delivery_slip']
        val: str = str(page.get_delivery_slip())
        assert val == correct_val, (
                f'Delivery slip is incorrect: {data['name']}'
        )

    def test_return_slip(self, page: OperationType, data: dict[str, Any]):
        page.nav_hardware_tab()
        correct_val: str = data['return_slip']
        val: str = str(page.get_return_slip())
        assert val == correct_val, (
                f'Return slip is incorrect: {data['name']}'
        )

    def test_product_labels(self, page: OperationType, data: dict[str, Any]):
        page.nav_hardware_tab()
        correct_val: str = data['product_labels']
        val: str = str(page.get_product_labels())
        assert val == correct_val, (
                f'Product labels is incorrect: {data['name']}'
        )

    def test_package_content(self, page: OperationType, data: dict[str, Any]):
        page.nav_hardware_tab()
        correct_val: str = data['package_content']
        val: str = str(page.get_package_content())
        assert val == correct_val, (
                f'Package content is incorrect: {data['name']}'
        )

    def test_package_label(self, page: OperationType, data: dict[str, Any]):
        page.nav_hardware_tab()
        correct_val: str = data['package_label']
        val: str = str(page.get_package_label())
        assert val == correct_val, (
                f'Package label is incorrect: {data['name']}'
        )

    # ============ Barcode Tab ============ #

    def test_source_location(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: str = data['source_location']
        val: str = page.get_src_location()
        assert val == correct_val, f'src location is incorrect: {data['name']}'

    def test_product(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: str = data['product']
        val: str = str(page.get_product())
        assert val == correct_val, f'Product is incorrect: {data['name']}'

    def test_put_in_pack(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: str = data['put_in_pack']
        val: str = page.get_in_pack()
        assert val == correct_val, (
            f'Put in pack is incorrect: {data['name']}'
        )

    def test_dest_location(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: str = data['destination_location']
        val: str = page.get_des()
        assert val == correct_val, (
            f'Destination location is incorrect: {data['name']}'
        )

    def test_full_categories(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: list[str] = data['picking_categories']
        val: list[str] = page.get_categories()
        assert val == correct_val, (
            f'Picking categories is incorrect: {data['name']}'
        )

    def test_pick_restricted(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: str = data['is_picking_restricted']
        val: str = str(page.get_pick_restricted())
        assert val == correct_val, (
            f'Is picking restricted is incorrect: {data['name']}'
        )

    def test_force_packed(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: str = data['force_all_products']
        val: str = str(page.get_force_pack())
        assert val == correct_val, (
            f'Force all products to be packed is incorrect: {data['name']}'
        )


class TestDeleivery:
    @pytest.fixture(scope='class')
    def page(self, request: FixtureRequest):
        """ Selenium driver with scraper """
        environment: str = request.config.getoption('--environment')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        driver_arg: str = request.config.getoption('--window')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        page: OperationType
        if driver_arg:
            page = OperationType(driver_arg)
        else:
            page = OperationType()

        if environment == 'staging':
            page.login_staging()

        if environment == 'production':
            page.login_prod()

        if environment == 'uat':
            page.login_uat()
        return page

    @pytest.fixture(
        scope='class',
        params=glob(
            'testcases_json/configs/operation_types/delivery/*.json'
        )
    )
    def data(self,
             request: FixtureRequest,
             page: OperationType,
             environment: str
             ) -> dict[str, Any]:
        """Paramitize for multiple json test cases"""
        fp = cast(str, request.param)
        with open(fp, 'r') as file:
            data: dict[str, Any] = json.load(file)
            if environment == 'staging':
                page.navigate(cast(str, data['staging_url']))

            if environment == 'production':
                page.navigate(cast(str, data['production_url']))

            if environment == 'uat':
                page.navigate(cast(str, data['uat_url']))

            sleep(0.5)
            return data

# ============ Tests ============ #
    def test_name(self, page: OperationType, data: dict[str, Any]):
        correct_val: str = data['name']
        val: str | None = page.get_name()
        assert val == correct_val, 'Name is not configured correctly'

    # ============ General Tab ============ #

    def test_type_opt(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['type_of_operation']
        val: str = page.get_type_opt()
        assert val == correct_val, (
            f'Type of operation is incorrect: {data['name']}'
        )

    def test_seq_prefix(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['sequence_prefix']
        val: str | None = page.get_seq_prefix()
        assert val == correct_val, (
            f'Sequence prefix is incorrect {data['name']}'
        )

    def test_print_label(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['print_label']
        val: str = str(page.get_print_label())
        assert val == correct_val, f'Print label is incorrect {data['name']}'

    def test_barcode(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['barcode']
        val: str | None = page.get_barcode()
        assert val == correct_val, f'Barcode is incorrect: {data['name']}'

    def test_res_method(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['reservation_method']
        val: str | None = page.get_res_method()
        assert val == correct_val, (
            f'Reservation method is incorrect: {data['name']}'
        )

    def test_move_e_package(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['move_entire_packages']
        val: str = str(page.get_move_e_package())
        assert val == correct_val, (
            f'Move entire packages is incorrect: {data['name']}'
        )

    def test_create_backorder(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['create_backorder']
        val: str = page.get_create_backorder()
        assert val == correct_val, (
            f'Create backorder is incorrect: {data['name']}'
        )

    def test_default_src_location(self,
                                  page: OperationType,
                                  data: dict[str, Any]
                                  ):
        page.nav_gen_tab()
        correct_val: str = data['default_source_location']
        val: str | None = page.get_def_src()
        assert val == correct_val, (
            f'Def src location is incorrect: {data['name']}'
        )

    def test_default_dest_location(self,
                                   page: OperationType,
                                   data: dict[str, Any]
                                   ):
        page.nav_gen_tab()
        correct_val: str = data['default_destination_location']
        val: str | None = page.get_def_des()
        assert val == correct_val, (
            f'Def dest location is incorrect: {data['name']}'
        )

    def test_batch_transfer(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['automatic_batches']
        val: str = str(page.get_auto_batch())
        assert val == correct_val, f'Auto batch is incorrect: {data['name']}'

    # ============ Hardware Tab ============ #

    def test_delivery_slip(self, page: OperationType, data: dict[str, Any]):
        page.nav_hardware_tab()
        correct_val: str = data['delivery_slip']
        val: str = str(page.get_delivery_slip())
        assert val == correct_val, (
                f'Delivery slip is incorrect: {data['name']}'
        )

    def test_return_slip(self, page: OperationType, data: dict[str, Any]):
        page.nav_hardware_tab()
        correct_val: str = data['return_slip']
        val: str = str(page.get_return_slip())
        assert val == correct_val, (
                f'Return slip is incorrect: {data['name']}'
        )

    def test_product_labels(self, page: OperationType, data: dict[str, Any]):
        page.nav_hardware_tab()
        correct_val: str = data['product_labels']
        val: str = str(page.get_product_labels())
        assert val == correct_val, (
                f'Product labels is incorrect: {data['name']}'
        )

    def test_package_content(self, page: OperationType, data: dict[str, Any]):
        page.nav_hardware_tab()
        correct_val: str = data['package_content']
        val: str = str(page.get_package_content())
        assert val == correct_val, (
                f'Package content is incorrect: {data['name']}'
        )

    def test_package_label(self, page: OperationType, data: dict[str, Any]):
        page.nav_hardware_tab()
        correct_val: str = data['package_label']
        val: str = str(page.get_package_label())
        assert val == correct_val, (
                f'Package label is incorrect: {data['name']}'
        )

    # ============ Barcode Tab ============ #

    def test_source_location(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: str = data['source_location']
        val: str = page.get_src_location()
        assert val == correct_val, f'src location is incorrect: {data['name']}'

    def test_product(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: str = data['product']
        val: str = str(page.get_product())
        assert val == correct_val, f'Product is incorrect: {data['name']}'

    def test_put_in_pack(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: str = data['put_in_pack']
        val: str = page.get_in_pack()
        assert val == correct_val, (
            f'Put in pack is incorrect: {data['name']}'
        )

    def test_full_categories(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: list[str] = data['picking_categories']
        val: list[str] = page.get_categories()
        assert val == correct_val, (
            f'Picking categories is incorrect: {data['name']}'
        )

    def test_pick_restricted(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: str = data['is_picking_restricted']
        val: str = str(page.get_pick_restricted())
        assert val == correct_val, (
            f'Is picking restricted is incorrect: {data['name']}'
        )

    def test_force_packed(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: str = data['force_all_products']
        val: str = str(page.get_force_pack())
        assert val == correct_val, (
            f'Force all products to be packed is incorrect: {data['name']}'
        )


class TestManufacturing:
    @pytest.fixture(scope='class')
    def page(self, request: FixtureRequest):
        """ Selenium driver with scraper """
        environment: str = request.config.getoption('--environment')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        driver_arg: str = request.config.getoption('--window')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        page: OperationType

        if driver_arg:
            page = OperationType(driver_arg)
        else:
            page = OperationType()

        if environment == 'staging':
            page.login_staging()

        if environment == 'production':
            page.login_prod()

        if environment == 'uat':
            page.login_uat()
        return page

    @pytest.fixture(
        scope='class',
        params=glob(
            'testcases_json/configs/operation_types/manufacturing/*.json'
        )
    )
    def data(self,
             request: FixtureRequest,
             page: OperationType,
             environment: str
             ) -> dict[str, Any]:
        """Paramitize for multiple json test cases"""
        fp = cast(str, request.param)
        with open(fp, 'r') as file:
            data: dict[str, Any] = json.load(file)
            if environment == 'staging':
                page.navigate(cast(str, data['staging_url']))

            if environment == 'production':
                page.navigate(cast(str, data['production_url']))

            if environment == 'uat':
                page.navigate(cast(str, data['uat_url']))

            sleep(0.5)
            return data

# ============ Tests ============ #
    def test_name(self, page: OperationType, data: dict[str, Any]):
        correct_val: str = data['name']
        val: str | None = page.get_name()
        assert val == correct_val, 'Name is not configured correctly'

    # ============ General Tab ============ #

    def test_type_opt(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['type_of_operation']
        val: str = page.get_type_opt()
        assert val == correct_val, (
            f'Type of operation is incorrect: {data['name']}'
        )

    def test_seq_prefix(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['sequence_prefix']
        val: str | None = page.get_seq_prefix()
        assert val == correct_val, (
            f'Sequence prefix is incorrect {data['name']}'
        )

    def test_barcode(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['barcode']
        val: str | None = page.get_barcode()
        assert val == correct_val, f'Barcode is incorrect: {data['name']}'

    def test_res_method(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['reservation_method']
        val: str | None = page.get_res_method()
        assert val == correct_val, (
            f'Reservation method is incorrect: {data['name']}'
        )

    def test_create_backorder(self, page: OperationType, data: dict[str, Any]):
        page.nav_gen_tab()
        correct_val: str = data['create_backorder']
        val: str = page.get_create_backorder()
        assert val == correct_val, (
            f'Create backorder is incorrect: {data['name']}'
        )

    def test_default_src_location(self,
                                  page: OperationType,
                                  data: dict[str, Any]
                                  ):
        page.nav_gen_tab()
        correct_val: str = data['default_source_location']
        val: str | None = page.get_def_src()
        assert val == correct_val, (
            f'Def src location is incorrect: {data['name']}'
        )

    def test_default_dest_location(self,
                                   page: OperationType,
                                   data: dict[str, Any]
                                   ):
        page.nav_gen_tab()
        correct_val: str = data['default_destination_location']
        val: str | None = page.get_def_des()
        assert val == correct_val, (
            f'Def dest location is incorrect: {data['name']}'
        )

    # ============ Hardware Tab ============ #

    def test_mrp_order(self, page: OperationType, data: dict[str, Any]):
        page.nav_mrp_hardware_tab()
        correct_val: str = data['mrp_production_order']
        val: str = str(page.get_mrp_production_order())
        assert val == correct_val, f'Prod order is incorrect: {data['name']}'

    def test_mrp_labels(self, page: OperationType, data: dict[str, Any]):
        page.nav_mrp_hardware_tab()
        correct_val: str = data['mrp_product_labels']
        val: str = str(page.get_mrp_labels())
        assert val == correct_val, f'Prod labels is incorrect: {data['name']}'

    # ============ Barcode Tab ============ #k

    def test_source_location(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: str = data['source_location']
        val: str = page.get_src_location()
        assert val == correct_val, f'src location is incorrect: {data['name']}'

    def test_product(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: str = data['product']
        val: str = str(page.get_product())
        assert val == correct_val, f'Product is incorrect: {data['name']}'

    def test_dest_location(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: str = data['destination_location']
        val: str = page.get_des()
        assert val == correct_val, (
            f'Destination location is incorrect: {data['name']}'
        )

    def test_full_order_validation(self,
                                   page: OperationType,
                                   data: dict[str, Any]
                                   ):
        page.nav_bar_tab()
        correct_val: str = data['full_order_validation']
        val: str = str(page.get_mrp_full_order())
        assert val == correct_val, (
            f'Allow full order validation is incorrect: {data['name']}'
        )

    def test_full_categories(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: list[str] = data['picking_categories']
        val: list[str] = page.get_categories()
        assert val == correct_val, (
            f'Picking categories is incorrect: {data['name']}'
        )

    def test_pick_restricted(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: str = data['is_picking_restricted']
        val: str = str(page.get_pick_restricted())
        assert val == correct_val, (
            f'Is picking restricted is incorrect: {data['name']}'
        )

    def test_force_dest(self, page: OperationType, data: dict[str, Any]):
        page.nav_bar_tab()
        correct_val: str = data['force_all_products']
        val: str = str(page.get_force_des_all())
        assert val == correct_val, (
            f'Force dest on all products is incorrect: {data['name']}'
        )
