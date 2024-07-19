import dearpygui.dearpygui as dpg
from stores_info import stores
from store_inventory import shoes

class globals:
    WIDTH = 1000
    HEIGHT = 600

dpg.create_context()
dpg.create_viewport(title=" ",width=globals.WIDTH, height=globals.HEIGHT,decorated=True,resizable=False)

class Windows: 
    with dpg.window(label="background_window", tag="background_window") as background_window:
        dpg.create_context()
        
    with dpg.window(label="side_menu",tag="side_menu",pos=(10,10),width=200,height=globals.HEIGHT-60,no_resize=True,
        no_title_bar=True,no_move=True,indent=1) as side_menu_window:
        dpg.create_context()
       
        Orders_title = dpg.add_button(label="ORDERS",width=dpg.get_item_width("side_menu")-15)
        dpg.add_spacer(height=1)
        #dpg.add_spacer(height=100)

        with dpg.child_window(width=185,height=100,border=True,tag="child_background_window") as profile_background:
            pfp = dpg.load_image("lib\\assets\\profile-icon-9.png")
            pfp_width,pfp_height,pfp_channels,pfp_data = pfp
            
            with dpg.texture_registry():
                dpg.add_static_texture(pfp_width,pfp_height,pfp_data,tag="pfp")

            with dpg.group(horizontal=True):
                dpg.add_image("pfp",width=60,height=63,pos=(0,2),indent=3)
                dpg.add_text(f"\nHub Name\n------\nHub Rating")
            dpg.add_text(f"Name")

        class Window_manager: 
            def window_management(sender,app_data,user_data):
                for window in Windows.main_menu_windows:
                    dpg.hide_item(window)
                dpg.show_item(user_data)
                    
        dpg.add_spacer(height=1) 
        store_info_button = dpg.add_button(label="Store Info",tag="store_info_button",callback=Window_manager.window_management,user_data="store_info_window")
        dpg.add_spacer(height=1)
        inventory_button = dpg.add_button(label="Store Inventory",tag="inventory_button",callback=Window_manager.window_management,user_data="store_inventory_window")
        dpg.add_spacer(height=1)
        incoming_orders_button = dpg.add_button(label="Incoming Orders",tag="incoming_orders_button",callback=Window_manager.window_management,user_data="incoming_orders_window")
        dpg.add_spacer(height=1)
        recieve_shipment_button = dpg.add_button(label="Recieve Shipment",tag="recieve_shipment_button",callback=Window_manager.window_management,user_data="recieve_shipment_window")
        dpg.add_spacer(height=1)
        sales_analytics_button = dpg.add_button(label="Sales Analytics",tag="sales_analytics_button",callback=Window_manager.window_management,user_data="sales_analytics_window")
        dpg.add_spacer(height=1)
        dpg.add_text(f"Sales: ---- ")
        dpg.add_text(f"Revenue: $----")
        dpg.add_spacer(height=.5)
        with dpg.plot(width=185,height=125,crosshairs=True,equal_aspects=True,tracked=True):
            x_data = [0,1,2,3,4,5,6,7,8,9,100]   
            y_data = [0,5,10,10,20,25,5,35,40]   
            dpg.add_plot_axis(dpg.mvXAxis)
            dpg.add_plot_axis(dpg.mvYAxis)
            #dpg.set_axis_limits(dpg.last_item(), 0,50)
            # Add line series to the y axis
            dpg.add_line_series(x_data, y_data, label="Parabola", parent=dpg.last_item())
        dpg.add_spacer(height=15)
        with dpg.group(horizontal=True):
            Help_button = dpg.add_button(label="?")
            dpg.add_text("HELP")
        with dpg.group(horizontal=True):
            Settings_button = dpg.add_button(label="*")
            dpg.add_text("SETTINGS")

    with dpg.window(label="store_info_window",tag="store_info_window", pos=(225,10),width=500,
        height=globals.HEIGHT/1.8,no_close=True,no_move=True,no_title_bar=True,no_resize=True, show=True) as store_info_window:
        with dpg.child_window(border=False,height=150,horizontal_scrollbar=True) as store_info_cw:
            with dpg.theme() as scrollbar_size:
                with dpg.theme_component(dpg.mvChildWindow):
                    dpg.add_theme_style(dpg.mvStyleVar_ScrollbarSize,10,category=dpg.mvStyleVar_Alpha)
                
            with dpg.table(header_row=True,borders_innerH=True,borders_innerV=True,borders_outerH=True,borders_outerV=True,
                row_background=True,resizable=True,width=600):
                for col_name in stores[0].keys():
                    dpg.add_table_column(label=f"{col_name}",width_fixed=True)
                for store in stores:
                    with dpg.table_row():
                        for value in store.values():
                            dpg.add_text(f"{value}")

        with dpg.child_window():
            with dpg.plot(label="District orders",width=450,height=160):
                dpg.add_plot_axis(axis=dpg.mvXAxis)
                dpg.add_plot_axis(axis=dpg.mvYAxis,label="Orders")
        
        with dpg.group(horizontal=True,horizontal_spacing=50): 
            dpg.add_text(f"Most Ordered : ")
            dpg.add_text(f"Total Orders: ",wrap=200)

    def test(sender,app_data,user_data):
        print(f"{app_data}")
        
    with dpg.window(label="store_inventory_window",tag="store_inventory_window", pos=(225,10),width=500,height=globals.HEIGHT/1.8,no_close=True,no_move=True,
        no_title_bar=True,no_resize=True, show=False) as store_inventory_window:
        dpg.add_combo(items=["Shoes","Shirts","Pants/Shorts","Accessories","Clearance"],tag="category_list",default_value="Shoes",callback=test)
        dpg.add_spacer(height=3)
        with dpg.table(header_row=True,borders_innerH=True,borders_innerV=True,borders_outerH=True,borders_outerV=True,
            row_background=True,resizable=True):
            for col_name in shoes[0]:
                dpg.add_table_column(label=f"{col_name}") 
            for shoe in shoes:
                with dpg.table_row():
                    for category in shoes[0]:
                        print(shoe[category])
                        if isinstance(shoe[category],float):
                            dpg.add_selectable(label=f"${shoe[category]:.2f}",span_columns=True,height=100)
                        else:
                            dpg.add_text(f"{shoe[category]}",wrap=100)
                   
            
    with dpg.window(label="incoming_orders_window",tag="incoming_orders_window", pos=(225,10),width=500,
        height=globals.HEIGHT/1.8,no_close=True,no_move=True,no_title_bar=True,no_resize=True, show=False) as incoming_orders_window:
        dpg.create_context()
        dpg.add_text("incoming orders")

    with dpg.window(label="recieve_shipment_window",tag="recieve_shipment_window", pos=(225,10),width=500,
        height=globals.HEIGHT/1.8,no_close=True,no_move=True,no_title_bar=True,no_resize=True, show=False) as recieve_shipment_window:
        dpg.create_context()
        dpg.add_text("recieve shipment")
    
    with dpg.window(label="sales_analytics_window",tag="sales_analytics_window", pos=(225,10),width=500,
        height=globals.HEIGHT/1.8,no_close=True,no_move=True,no_title_bar=True,no_resize=True, show=False) as sales_analytics_window:
        dpg.create_context()
        dpg.add_text("sales analytics")

    
    #may be able to do a login window


    with dpg.window(label="customer_window",tag="customer_window", pos=(740,10),width=235,height=globals.HEIGHT/3.8,no_close=True,
        no_move=True,no_title_bar=True,no_resize=True) as customer_window:
        dpg.create_context()
        

    with dpg.window(label="phone_window",tag="phone_window", pos=(740,180),width=235,height=globals.HEIGHT/3.67,no_close=True,
        no_move=True,no_title_bar=True,no_resize=True) as phone_window:
        dpg.create_context()

    with dpg.window(label="checkout_window",tag="checkout_window", pos=(225,355),width=750,height=globals.HEIGHT/3.07,no_close=True,
        no_move=True,no_title_bar=True,no_resize=True) as checkout_window:
        dpg.create_context()

    menu_bg_windows = (side_menu_window,)
    main_menu_windows = (store_info_window,store_inventory_window,incoming_orders_window,recieve_shipment_window,sales_analytics_window)

    class Theme:
        with dpg.theme() as background_theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (30, 30, 30),category=dpg.mvThemeCat_Core)

        with dpg.theme() as window_theme:
            with dpg.theme_component(dpg.mvStyleVar_Alpha):
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (15, 15, 15),category=dpg.mvThemeCat_Core)

        with dpg.theme() as child_window_theme:
            with dpg.theme_component(dpg.mvChildWindow):
                dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (15, 15, 15),category=dpg.mvThemeCat_Core)
                

dpg.bind_item_theme(Windows.background_window,Windows.Theme.background_theme)

dpg.bind_item_theme(Windows.side_menu_window,Windows.Theme.window_theme)
dpg.bind_item_theme(Windows.store_info_window,Windows.Theme.window_theme)
dpg.bind_item_theme(Windows.customer_window,Windows.Theme.window_theme)
dpg.bind_item_theme(Windows.phone_window,Windows.Theme.window_theme)
dpg.bind_item_theme(Windows.checkout_window,Windows.Theme.window_theme)
dpg.bind_item_theme(Windows.profile_background,Windows.Theme.child_window_theme)
dpg.bind_item_theme(Windows.store_info_cw,Windows.scrollbar_size)
for window in Windows.main_menu_windows:
    dpg.bind_item_theme(window,Windows.Theme.window_theme)



dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("background_window", True)
dpg.start_dearpygui()
dpg.destroy_context()