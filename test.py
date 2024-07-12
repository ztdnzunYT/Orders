import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.theme() as table_theme:
    with dpg.theme_component(dpg.mvTable):
        # dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (255, 0, 0, 100), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, (0, 0, 0, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Header, (0, 0, 0, 0), category=dpg.mvThemeCat_Core)

def clb_selectable(sender, app_data, user_data):
    print(f"Row {user_data}")

with dpg.window(tag="table"):
    with dpg.table(tag="rows",header_row=True,borders_innerH=True,borders_innerV=True,borders_outerH=True,borders_outerV=True,row_background=True) as selectablerows:
        dpg.add_table_column(label="First")
        dpg.add_table_column(label="Second")
        dpg.add_table_column(label="Third")

        for i in range(15):
            with dpg.table_row(height=20):
                for j in range(3):
                    dpg.add_selectable(label=f"Row{i} Column{j}", span_columns=True, callback=clb_selectable, user_data=i)

    dpg.bind_item_theme(selectablerows, table_theme)


dpg.create_viewport(width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()