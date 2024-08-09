import dearpygui.dearpygui as dpg

# Initialize Dear PyGui context
dpg.create_context()

# Create a window
dpg.show_imgui_demo()

# Show the viewport
dpg.create_viewport(title='Basic Table Example', width=400, height=300)
dpg.setup_dearpygui()
dpg.show_viewport()

# Start the Dear PyGui event loop
dpg.start_dearpygui()

# Destroy context after the event loop ends
dpg.destroy_context()
