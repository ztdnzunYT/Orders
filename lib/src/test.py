import dearpygui.dearpygui as dpg

# Initialize Dear PyGui context
dpg.create_context()

# Callback function to highlight the selected cell
def highlight_cell(sender, app_data, user_data):
    cell = app_data
    row, column = cell // 5, cell % 5  # Assuming 5 columns
    for i in range(10):  # Assuming 10 rows
        for j in range(5):
            if (i, j) == (row, column):
                dpg.set_item_color((i * 5 + j), dpg.mvThemeCol_Text, [255, 255, 255, 255])  # Selected cell color
                dpg.set_item_color((i * 5 + j), dpg.mvThemeCol_FrameBg, [100, 149, 237, 255])  # Selected cell background color
            else:
                dpg.set_item_color((i * 5 + j), dpg.mvThemeCol_Text, [0, 0, 0, 255])  # Default text color
                dpg.set_item_color((i * 5 + j), dpg.mvThemeCol_FrameBg, [255, 255, 255, 255])  # Default background color

# Main window
with dpg.window(label="Table Example", width=800, height=600):
    with dpg.table(header_row=True, resizable=True, policy=dpg.mvTable_SizingStretchProp,
                   borders_innerV=True, borders_outerV=True, borders_innerH=True, borders_outerH=True):
        # Adding columns
        dpg.add_table_column(label="Column 1")
        dpg.add_table_column(label="Column 2")
        dpg.add_table_column(label="Column 3")
        dpg.add_table_column(label="Column 4")
        dpg.add_table_column(label="Column 5")

        # Adding rows and cells
        for i in range(10):
            with dpg.table_row():
                for j in range(5):
                    dpg.add_text(f"Cell {i + 1},{j + 1}", tag=i * 5 + j)

# Set up cell selection callback
with dpg.handler_registry():
    dpg.add_item_clicked_handler(callback=highlight_cell)

# Show the viewport
dpg.create_viewport(title='Table Example', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()

# Start the Dear PyGui event loop
dpg.start_dearpygui()
dpg.destroy_context()
