import dearpygui.dearpygui as dpg

# Initialize Dear PyGui context
dpg.create_context()

# Create a window
with dpg.window(label="Vertical Line Separator Example", width=300, height=200):

    # Create a horizontal group for items
    with dpg.group(horizontal=True):
        dpg.add_button(label="Button 1")

        # Create a vertical line separator using a drawing canvas
        with dpg.drawlist(width=5, height=100):
            dpg.draw_line((2, 0), (2, 100), color=(0, 0, 0, 255), thickness=1)

        dpg.add_button(label="Button 2")

# Show the viewport
dpg.create_viewport(title='Vertical Line Separator Example', width=400, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()

# Start the Dear PyGui event loop
dpg.start_dearpygui()

# Destroy context after the event loop ends
dpg.destroy_context()
