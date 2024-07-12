import dearpygui.dearpygui as dpg

class globals:
    WIDTH = 1000
    HEIGHT = 600

dpg.create_context()
dpg.create_viewport(title=" ",width=globals.WIDTH, height=globals.HEIGHT,decorated=True,resizable=False)

class Windows: 
    with dpg.window(label="background_window", tag="background_window") as background_window:
        dpg.create_context()
        
    with dpg.window(label="side_menu",tag="side_menu",pos=(10,10),width=200,height=globals.HEIGHT-60,no_resize=True,no_title_bar=True,no_move=True,indent=1) as side_menu:
        dpg.create_context()
       
        Orders_text = dpg.add_button(label="ORDERS",width=dpg.get_item_width("side_menu")-15)
        dpg.add_spacer(height=100)
        Store_info = dpg.add_button(label="Store Info")
        dpg.add_spacer(height=1)
        Inventory_button = dpg.add_button(label="Store Inventory")
        dpg.add_spacer(height=1)
        Incoming_orders_button = dpg.add_button(label="Incoming Orders")
        dpg.add_spacer(height=1)
        Recieve_shipment_button = dpg.add_button(label="Recieve Shipment")
        dpg.add_spacer(height= dpg.get_item_height("side_menu")/2.25)
        Help_button = dpg.add_button(label="?")
        dpg.add_same_line()
        dpg.add_text("HELP")
        Settings_button = dpg.add_button(label="*")
        dpg.add_same_line()
        dpg.add_text("SETTINGS")
    
    
    with dpg.window(label="main_window",tag="main_window", pos=(225,10),width=500,height=globals.HEIGHT/1.8,no_close=True,no_move=True,no_title_bar=True,no_resize=True, show=True) as main_window:
        dpg.create_context()

    with dpg.window(label="customer_window",tag="customer_window", pos=(740,10),width=235,height=globals.HEIGHT/3.8,no_close=True,no_move=True,no_title_bar=True,no_resize=True) as customer_window:
        dpg.create_context()

    with dpg.window(label="phone_window",tag="phone_window", pos=(740,180),width=235,height=globals.HEIGHT/3.67,no_close=True,no_move=True,no_title_bar=True,no_resize=True) as phone_window:
        dpg.create_context()

    with dpg.window(label="checkout_window",tag="checkout_window", pos=(225,355),width=750,height=globals.HEIGHT/3.07,no_close=True,no_move=True,no_title_bar=True,no_resize=True) as checkout_window:
        dpg.create_context()

    class Theme:
        with dpg.theme() as background_theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (30, 30, 30),category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 1,category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_WindowRounding,0,category=dpg.mvThemeCat_Core)

        with dpg.theme() as window_theme:
            with dpg.theme_component(dpg.mvStyleVar_Alpha):
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (15, 15, 15),category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 1,category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_ButtonTextAlign,1/2,category=dpg.mvThemeCat_Core)
        



dpg.bind_item_theme(Windows.background_window,Windows.Theme.background_theme)
dpg.bind_item_theme(Windows.side_menu,Windows.Theme.window_theme)
dpg.bind_item_theme(Windows.main_window,Windows.Theme.window_theme)
dpg.bind_item_theme(Windows.customer_window,Windows.Theme.window_theme)
dpg.bind_item_theme(Windows.phone_window,Windows.Theme.window_theme)
dpg.bind_item_theme(Windows.checkout_window,Windows.Theme.window_theme)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("background_window", True)
dpg.start_dearpygui()
dpg.destroy_context()