import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=600)


# Callback function to add a new row to the table
def add_row_callback(sender, app_data, user_data):
    dpg.add_table_row(parent="table", before=0)
    dpg.add_text("New Row Text", parent=dpg.last_item())

# Creating a context
with dpg.window(label="Table Example"):
    
    # Creating a button that will add new rows when clicked
    dpg.add_button(label="Add Row", callback=add_row_callback)
    
    # Creating a table
    with dpg.table(header_row=True, resizable=True, policy=dpg.mvTable_SizingStretchProp, borders_outerH=True, borders_innerV=True, borders_innerH=True, borders_outerV=True, row_background=True, no_host_extendX=False, delay_search=True, parent=dpg.last_item(), id="table"):
        
        # Adding columns to the table
        dpg.add_table_column(label="Column 1")
        dpg.add_table_column(label="Column 2")

# Starting the Dear PyGui application



dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()