from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

from pages.base import BasePage


class OperationType(BasePage):
    def __init__(self, *args: str):
        super().__init__(*args)
        self.driver.implicitly_wait(5)

    def nav_gen_tab(self):
        tab_elem: WebElement = self.driver.find_element(By.NAME, 'general')
        tab_elem.click()

    def nav_hardware_tab(self):
        tab_elem: WebElement = self.driver.find_element(By.NAME, 'hardware')
        tab_elem.click()

    def nav_mrp_hardware_tab(self):
        tab_elem: WebElement = self.driver.find_element(
            By.NAME,
            'mrp_hardware'
        )
        tab_elem.click()

    def nav_bar_tab(self):
        tab_elem: WebElement = self.driver.find_element(By.NAME, 'barcode_app')
        tab_elem.click()

    def get_name(self) -> str | None:
        name_elem: WebElement = self.driver.find_element(By.ID, 'name_0')
        name: str | None = name_elem.get_attribute('value')
        return name

    # ============ General Tab ============ #
    def get_type_opt(self) -> str:
        type_elem: WebElement = self.driver.find_element(By.ID, 'code_0')
        opt: str = Select(type_elem).first_selected_option.text
        return opt

    def get_seq_prefix(self) -> str | None:
        pre_elem: WebElement = self.driver.find_element(
            By.ID,
            'sequence_code_0'
        )
        pre: str | None = pre_elem.get_attribute('value')
        return pre

    def get_barcode(self) -> str | None:
        bar_elem: WebElement = self.driver.find_element(By.ID, 'barcode_0')
        bar: str | None = bar_elem.get_attribute('value')
        return bar

    def get_returns_type(self) -> str | None:
        ret_elem: WebElement = self.driver.find_element(
            By.ID,
            'return_picking_type_id_0'
        )
        ret: str | None = ret_elem.get_attribute('value')
        return ret

    def get_def_return(self) -> str | None:
        ret_elem: WebElement = self.driver.find_element(
            By.ID,
            'default_location_return_id_0'
        )
        ret: str | None = ret_elem.get_attribute('value')
        return ret

    def get_create_backorder(self) -> str:
        back_elem: WebElement = self.driver.find_element(
            By.ID,
            'create_backorder_0'
        )
        back: str = Select(back_elem).first_selected_option.text
        return back

    def get_move_e_package(self) -> bool:
        move_elem: WebElement = self.driver.find_element(
            By.ID,
            'show_entire_packs_0'
        )
        move: bool = move_elem.is_selected()
        return move

    def get_def_src(self) -> str | None:
        src_elem: WebElement = self.driver.find_element(
            By.ID,
            'default_location_src_id_0'
        )
        src: str | None = src_elem.get_attribute('value')
        return src

    def get_def_des(self) -> str | None:
        des_elem: WebElement = self.driver.find_element(
            By.ID,
            'default_location_dest_id_0'
        )
        des: str | None = des_elem.get_attribute('value')
        return des

    def get_auto_batch(self) -> bool:
        batch_elem: WebElement = self.driver.find_element(
            By.ID,
            'auto_batch_0'
        )
        batch: bool = batch_elem.is_selected()
        return batch

    def get_print_label(self) -> bool:
        print_elem: WebElement = self.driver.find_element(
            By.ID,
            'print_label_0'
        )
        print_bool: bool = print_elem.is_selected()
        return print_bool

    # ============ Hardware Tab ============ #

    def get_delivery_slip(self) -> bool:
        slip_elem: WebElement = self.driver.find_element(
            By.ID,
            'auto_print_delivery_slip_0'
        )
        slip: bool = slip_elem.is_selected()
        return slip

    def get_return_slip(self) -> bool:
        slip_elem: WebElement = self.driver.find_element(
            By.ID,
            'auto_print_return_slip_0'
        )
        slip: bool = slip_elem.is_selected()
        return slip

    def get_product_labels(self) -> bool:
        label_elem: WebElement = self.driver.find_element(
            By.ID,
            'auto_print_product_labels_0'
        )
        label: bool = label_elem.is_selected()
        return label

    def get_package_content(self) -> bool:
        content_elem: WebElement = self.driver.find_element(
            By.ID,
            'auto_print_packages_0'
        )
        content: bool = content_elem.is_selected()
        return content

    def get_package_label(self) -> bool:
        label_elem: WebElement = self.driver.find_element(
            By.ID,
            'auto_print_package_label_0'
        )
        label: bool = label_elem.is_selected()
        return label

    def get_mrp_production_order(self) -> bool:
        mrp_elem: WebElement = self.driver.find_element(
            By.ID,
            'auto_print_done_production_order_0'
        )
        mrp: bool = mrp_elem.is_selected()
        return mrp

    def get_mrp_labels(self) -> bool:
        mrp_elem: WebElement = self.driver.find_element(
            By.ID,
            'auto_print_done_mrp_product_labels_0'
        )
        mrp: bool = mrp_elem.is_selected()
        return mrp

    # ============ Barcode Tab ============ #

    def get_product(self) -> bool:
        pro_elem: WebElement = self.driver.find_element(
            By.ID,
            'restrict_scan_product_0'
        )
        pro: bool = pro_elem.is_selected()
        return pro

    def get_in_pack(self) -> str:
        pack_elem: WebElement = self.driver.find_element(
            By.ID,
            'restrict_put_in_pack_0'
        )
        pack: str = Select(pack_elem).first_selected_option.text
        return pack

    def get_des(self) -> str:
        des_elem: WebElement = self.driver.find_element(
            By.ID,
            'restrict_scan_dest_location_0'
        )
        des: str = Select(des_elem).first_selected_option.text
        return des

    def get_full_pick_validation(self) -> bool:
        val_elem: WebElement = self.driver.find_element(
            By.ID,
            'barcode_validation_full_0'
        )
        val: bool = val_elem.is_selected()
        return val

    def get_categories(self) -> list[str]:
        cats: list[str] = []
        container_elem: WebElement = self.driver.find_element(
            By.NAME,
            'full_scan_allowed_categories_ids'
        )
        spans: list[WebElement] = container_elem.find_elements(
            By.TAG_NAME,
            'span'
        )

        for span in spans:
            if span.text != '':
                cats.append(span.text)
        return cats

    def get_pick_restricted(self) -> bool:
        pick_elem: WebElement = self.driver.find_element(
            By.ID,
            'is_picking_restricted_0'
        )
        pick: bool = pick_elem.is_selected()
        return pick

    def get_force_pack(self) -> bool:
        force_elem: WebElement = self.driver.find_element(
            By.ID,
            'barcode_validation_all_product_packed_0'
        )
        force: bool = force_elem.is_selected()
        return force

    def get_force_des_all(self) -> bool:
        des_elem: WebElement = self.driver.find_element(
            By.ID,
            'barcode_validation_after_dest_location_0'
        )
        des: bool = des_elem.is_selected()
        return des

    def get_src_location(self) -> str:
        src_elem: WebElement = self.driver.find_element(
            By.ID,
            'restrict_scan_source_location_0'
        )
        src: str = Select(src_elem).first_selected_option.text
        return src

    def get_res_method(self) -> str | None:

        div: WebElement = self.driver.find_element(
            By.NAME,
            'reservation_method'
        )
        radio_divs: list[WebElement] = div.find_elements(
            By.CLASS_NAME,
            'o_radio_item'
        )
        for radio_div in radio_divs:
            radio: WebElement = radio_div.find_element(By.TAG_NAME, 'input')
            if radio.is_selected():
                label: WebElement = radio_div.find_element(
                    By.TAG_NAME,
                    'label'
                )
                return label.text

    def get_mrp_full_order(self) -> bool:
        val_elem: WebElement = self.driver.find_element(
            By.ID,
            'barcode_validation_full_1'
        )
        val: bool = val_elem.is_selected()
        return val

    def get_allow_more_qty(self) -> bool:
        val_elem: WebElement = self.driver.find_element(
            By.ID, 'allow_more_qty_0'
        )
        val: bool =val_elem.is_selected()
        return val
