import dearpygui.dearpygui as dpg

# Initialize Dear PyGui context
dpg.create_context()

# Callback to print the selected combo value
def combo_callback(sender, app_data, user_data):
    print(f"Selected value: {app_data}")

# Create the main window
with dpg.window(label="Combo Example", width=400, height=300):
    # Create a combo box
    dpg.add_combo(label="Select an option", items=["Option 1", "Option 2", "Option 3"], callback=combo_callback)

# Show the viewport
dpg.create_viewport(title='Combo Example', width=400, height=300)
dpg.setup_dearpygui()
dpg.show_viewport()

# Start the Dear PyGui event loop
dpg.start_dearpygui()
dpg.destroy_context()
