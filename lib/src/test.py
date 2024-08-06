import dearpygui.dearpygui as dpg

# Initialize Dear PyGui context
dpg.create_context()

# Create a window
with dpg.window(label="Basic Table Example", width=400, height=300):
    
    # Create a table with 3 columns
    with dpg.table(header_row=False, resizable=True, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
        
        # Add table headers
        dpg.add_table_column(label="Column 1")
        dpg.add_table_column(label="Column 2")
        dpg.add_table_column(label="Column 3")
        
        # Add rows with data
        with dpg.table_row():
            dpg.add_text("Row 1, Col 1")
            dpg.add_text("Row 1, Col 2")
            dpg.add_text("Row 1, Col 3")
        
        with dpg.table_row():
            dpg.add_text("Row 2, Col 1")
            dpg.add_text("Row 2, Col 2")
            dpg.add_text("Row 2, Col 3")
        
        with dpg.table_row():
            dpg.add_text("Row 3, Col 1")
            dpg.add_text("Row 3, Col 2")
            dpg.add_text("Row 3, Col 3")

# Show the viewport
dpg.create_viewport(title='Basic Table Example', width=400, height=300)
dpg.setup_dearpygui()
dpg.show_viewport()

# Start the Dear PyGui event loop
dpg.start_dearpygui()

# Destroy context after the event loop ends
dpg.destroy_context()
