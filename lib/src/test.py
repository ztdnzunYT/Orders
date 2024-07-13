import dearpygui.dearpygui as dpg

# Initialize the Dear PyGui context
dpg.create_context()

# Sample data for the line graph
x_data = [0, 1, 2, 3, 4, 5]
y_data = [0, 1, 4, 9, 2, 17,25,34,13,29,56]

# Create the main window
with dpg.window(tag="Line Graph Example", width=600, height=400):
    with dpg.plot(label="Line Graph", height=-1, width=-1,crosshairs=True):
        # Add x and y axes
        dpg.add_plot_axis(dpg.mvXAxis, label="X Axis")
        dpg.add_plot_axis(dpg.mvYAxis, label="Y Axis")
        
        # Add line series to the y axis
        dpg.add_line_series(x_data, y_data, label="Parabola", parent=dpg.last_item())

# Show the viewport
dpg.create_viewport(title='Line Graph Example', width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Line Graph Example", True)

# Start the Dear PyGui event loop
dpg.start_dearpygui()
dpg.destroy_context()
