import dearpygui.dearpygui as dpg
from stores_info import stores
from store_inventory import shoes,shirts,pants,accessories,inventory
from customer_info import first_names,last_names


import time
import random

class globals:
    WIDTH = 1000
    HEIGHT = 600

dpg.create_context()
dpg.create_viewport(title=" ",width=globals.WIDTH, height=globals.HEIGHT,decorated=True,resizable=False)


class Window_manager: 
                        
            def window_manager(sender,app_data,user_data):
                for window in Windows.main_menu_windows:
                    dpg.hide_item(window)
                dpg.show_item(user_data)
        
            def store_inventory_table_manager(sender,app_data,user_data):
                for window in Windows.store_inventory_tables:
                    dpg.hide_item(window)
                #dpg.show_item(str(app_data.lower()+"_table"))
                print(app_data)
                dpg.show_item(app_data.lower()+"_table")
            
            def add_recipt_item(sender,app_data,user_data):
                print(f"{sender,app_data}")
                category = list(user_data)[0]
                cost = "Price"
                user_data = dpg.get_item_user_data(sender)
                print(user_data[category])
                if app_data == True:
                    with dpg.table_row(parent="customer_table",height=20):
                        dpg.add_text(user_data[category],wrap=70)
                        dpg.add_text(f"${user_data[cost]:.2f}")
                Windows.Customer_window.items_added_value +=1
                dpg.set_value(Windows.Customer_window.items_added,Windows.Customer_window.items_added_value)
                    
            def clear_items():
                for item in Windows.Main_Window.selectables:
                    dpg.set_value(item,False)  
                print("Cart Order Cleared")
                for row in dpg.get_item_children(Windows.Customer_window.customer_table,slot=1):
                    dpg.delete_item(row)
                Windows.Customer_window.items_added_value = 0
                dpg.set_value(Windows.Customer_window.items_added,0)
                
                

class Windows: 
    
    class Side_menu:


        with dpg.window(label="background_window", tag="background_window") as background_window:
            dpg.create_context()
            
        with dpg.window(label="side_menu",tag="side_menu",pos=(10,10),width=200,height=globals.HEIGHT-60,no_resize=True,
            no_title_bar=True,no_move=True,indent=1) as side_menu_window:
            dpg.create_context()

            Orders_title = dpg.add_button(label="ORDERS",width=dpg.get_item_width("side_menu")-15)
            dpg.add_spacer(height=1)
            #dpg.add_spacer(height=100)

           
            with dpg.child_window(width=185,height=100,border=True,tag="child_background_window") as profile_background:
                
                with dpg.group(horizontal=True):
                    
                    dpg.add_text(f"\nHub Name\n------\nHub Rating")
                dpg.add_text(f"Name")


            dpg.add_spacer(height=1) 
            store_info_button = dpg.add_button(label="Store Info",tag="store_info_button",callback=Window_manager.window_manager,user_data="store_info_window")
            dpg.add_spacer(height=1)
            inventory_button = dpg.add_button(label="Store Inventory",tag="inventory_button",callback=Window_manager.window_manager,user_data="store_inventory_window")
            dpg.add_spacer(height=1)
            incoming_orders_button = dpg.add_button(label="Incoming Orders",tag="incoming_orders_button",callback=Window_manager.window_manager,user_data="incoming_orders_window")
            dpg.add_spacer(height=1)
            recieve_shipment_button = dpg.add_button(label="Recieve Shipment",tag="recieve_shipment_button",callback=Window_manager.window_manager,user_data="recieve_shipment_window")
            dpg.add_spacer(height=1)
            sales_analytics_button = dpg.add_button(label="Sales Analytics",tag="sales_analytics_button",callback=Window_manager.window_manager,user_data="sales_analytics_window")
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


    class Main_Window:
    
        with dpg.window(label="store_info_window",tag="store_info_window", pos=(225,10),width=500,
            height=globals.HEIGHT/1.8,no_close=True,no_move=True,no_title_bar=True,no_resize=True, show=True) as store_info_window:
            with dpg.child_window(border=False,height=150,horizontal_scrollbar=True) as store_info_cw:
                with dpg.theme() as scrollbar_size:
                    with dpg.theme_component(dpg.mvChildWindow):
                        dpg.add_theme_style(dpg.mvStyleVar_ScrollbarSize,10,category=dpg.mvStyleVar_Alpha)
                    
                with dpg.table(header_row=True,borders_innerH=True,borders_innerV=True,borders_outerH=True,borders_outerV=True,
                    row_background=True,resizable=False):
                    for col_name in stores[0].keys():
                        dpg.add_table_column(label=f"{col_name}",width_fixed=True)
                    for store in stores:
                        with dpg.table_row():
                            for value in store.values():
                                dpg.add_text(f"{value}",wrap=90)

            with dpg.child_window():
                with dpg.plot(label="District orders",width=450,height=160):
                    dpg.add_plot_axis(axis=dpg.mvXAxis)
                    dpg.add_plot_axis(axis=dpg.mvYAxis,label="Orders")
            
            with dpg.group(horizontal=True,horizontal_spacing=50): 
                dpg.add_text(f"Most Ordered : ")
                dpg.add_text(f"Total Orders: ",wrap=200)
        
        selectables = []

        with dpg.window(label="store_inventory_window",tag="store_inventory_window", pos=(225,10),width=500,
            height=globals.HEIGHT/1.8,no_close=True,no_move=True,
            no_title_bar=True,no_resize=True, show=False) as store_inventory_window:
            with dpg.group(horizontal=True):
                category_list = dpg.add_combo(items=["Shoes","Shirts","Pants","Accessories","Clearance"],
                    default_value="Shoes",callback=Window_manager.store_inventory_table_manager)
                dpg.add_button(label="Clear Items",callback=Window_manager.clear_items)
            dpg.add_spacer(height=3)

            with dpg.table(tag="shoes_table",header_row=True,borders_innerH=True,borders_innerV=True,borders_outerH=True,borders_outerV=True,
                row_background=False,resizable=False,show=True) as shoes_table:
                for col_name in shoes[0]:
                    dpg.add_table_column(label=f"{col_name}",width_fixed=True) 
                for shoe in shoes:
                    with dpg.table_row():
                        for category in shoes[0]:
                            if category == "Shoe Name":
                                dpg.add_text(shoe[category],wrap=170)
                            elif category == "Description":
                                dpg.add_text(f"{shoe[category]}",wrap=170)
                            elif category == "Price":
                                dpg.add_text(f"${shoe[category]:.2f}")
                            else:
                                selectables.append(dpg.add_selectable(label=shoe[category],callback=Window_manager.add_recipt_item,span_columns=True,height=45,user_data=shoe,filter_key=""))

            with dpg.table(tag="shirts_table",header_row=True,borders_innerH=True,borders_innerV=True,borders_outerH=True,borders_outerV=True,
                row_background=False,resizable=False,show=False) as shirts_table:
                for col_name in shirts[0]:
                    dpg.add_table_column(label=f"{col_name}",width_fixed=True) 
                for shirt in shirts:
                    with dpg.table_row():
                        for category in shirts[0]:
                            if category == "Shirt Name":
                                dpg.add_text(f"{shirt[category]}",wrap=200)
                            elif category == "Price":
                                dpg.add_text(f"${shirt[category]:.2f}")
                            else:
                                selectables.append(dpg.add_selectable(label=shirt[category],callback=Window_manager.add_recipt_item,span_columns=True,height=45,user_data=shirt))
            
            with dpg.table(tag="pants_table",header_row=True,borders_innerH=True,borders_innerV=True,borders_outerH=True,borders_outerV=True,
                row_background=False,resizable=False,show=False) as pants_table:
                for col_name in pants[0]:
                    dpg.add_table_column(label=f"{col_name}",width_fixed=True) 
                for pant in pants:
                    with dpg.table_row():
                        for category in pants[0]:
                            if category == "Pants Name":
                                dpg.add_text(f"{pant[category]}",wrap=200)
                            elif category == "Price":
                                dpg.add_text(f"${pant[category]:.2f}")
                            else:
                                selectables.append(dpg.add_selectable(label=pant[category],callback=Window_manager.add_recipt_item,span_columns=True,height=45,user_data=pant))

            with dpg.table(tag="accessories_table",header_row=True,borders_innerH=True,borders_innerV=True,borders_outerH=True,borders_outerV=True,
                row_background=False,resizable=False,show=False) as accessories_table:
                for col_name in accessories[0]:
                    dpg.add_table_column(label=f"{col_name}",width_fixed=True) 
                for accessory in accessories:
                    with dpg.table_row():
                        for category in accessories[0]:
                            if category == "Accessory Name":
                                dpg.add_text(f"{accessory[category]}",wrap=200)
                            elif category == "Price":
                                dpg.add_text(f"${accessory[category]:.2f}")
                            else:
                                selectables.append(dpg.add_selectable(label=accessory[category],callback=Window_manager.add_recipt_item,span_columns=True,height=45,user_data=accessory))
        
        class New_order:
            def __init__(self,name,store,status,items):
                self.name = name
                self.store = store
                self.status = status
                self.items = items
                
            def input_data(self):
                return self.name,self.store,self.status,self.items

            def show_data(sender,app_data,user_data):
                order_items = dpg.get_item_children("incoming_order_list",1)
                for item in order_items:
                    dpg.delete_item(item)
                name = 0
                dpg.add_button(label=f"{user_data[name]}",parent="incoming_order_list")
                dpg.add_separator(parent="incoming_order_list")
                store_name = 1
                dpg.set_value(Windows.Customer_window.recipt_store_name,f"Store Name: {user_data[store_name]}")
                items = 3
                for item in user_data[items]:
                    dpg.add_text(f"{item}",parent="incoming_order_list",wrap=170)
                    dpg.add_separator(parent="incoming_order_list")

            def input_items():
                item_list = []
                for num in range(random.randint(1,6)): #max of items each order can have 
                    category = random.randint(0,3)
                    item_list.append(list((inventory[category])[random.randrange(0,len(inventory[category]))].values())[0])
                    print(item_list)
                return item_list

            
            def create_order():
                order_items = dpg.get_item_children("incoming_order_list",1)
                for item in order_items:
                    dpg.delete_item(item)

                for order in Windows.new_order_list:
                    dpg.delete_item(order)
                Windows.new_order_list.clear()

                for i in range(random.randint(0,8)):
                    order_data = Windows.Main_Window.New_order(f"{first_names[random.randrange(0,len(first_names))]} {last_names[random.randrange(0,len(last_names))]}",
                        stores[random.randrange(0,len(stores))]["Store Name"],False,Windows.Main_Window.New_order.input_items())
                    with dpg.child_window(parent=Windows.incoming_orders,height=55,border=False) as new_order:
                        with dpg.group(horizontal=True,horizontal_spacing=10):
                            dpg.add_text(f"#{i+1}")
                            dpg.add_text(f"| {order_data.name}")
                        with dpg.group(horizontal=True):
                            dpg.add_text("Status")
                            dpg.add_checkbox(default_value=False) 
                            dpg.add_button(label="View Order",user_data=(order_data.input_data()),callback=Windows.Main_Window.New_order.show_data)
                        dpg.add_separator()
                    Windows.new_order_list.append(new_order)
                print(Windows.new_order_list)
          
 
    with dpg.window(label="incoming_orders_window",tag="incoming_orders_window", pos=(225,10),width=500,
        height=globals.HEIGHT/1.8,no_close=True,no_move=True,no_title_bar=True,no_resize=True, show=False) as incoming_orders_window:
        dpg.create_context()
        with dpg.group(horizontal=True):
            dpg.add_text("incoming orders")
            dpg.add_button(label="Refresh Orders",tag="refresh_orders",callback=Main_Window.New_order.create_order)
            new_order_list = []

        with dpg.group(horizontal=True):
            with dpg.child_window(tag="incomming_orders",width=dpg.get_item_width(incoming_orders_window)//2.5) as incoming_orders:
                pass
        
            with dpg.child_window(tag="incoming_order_list") as incoming_order_list:
                pass

    with dpg.window(label="recieve_shipment_window",tag="recieve_shipment_window", pos=(225,10),width=500,
        height=globals.HEIGHT/1.8,no_close=True,no_move=True,no_title_bar=True,no_resize=True, show=False) as recieve_shipment_window:
        dpg.create_context()
        dpg.add_text("recieve shipment")
    
    with dpg.window(label="sales_analytics_window",tag="sales_analytics_window", pos=(225,10),width=500,
        height=globals.HEIGHT/1.8,no_close=True,no_move=True,no_title_bar=True,no_resize=True, show=False) as sales_analytics_window:
        dpg.create_context()
        dpg.add_text("sales analytics")

    
    #may be able to do a login window
    
    class Customer_window:
        with dpg.window(label="customer_window",tag="customer_window", pos=(740,10),width=235,height=globals.HEIGHT/3.8,no_close=True,
            no_move=True,no_title_bar=True,no_resize=True) as customer_window:
            dpg.add_text("Recipt") 
            dpg.add_separator()
            recipt_store_name = dpg.add_text("Store Name :")
            items_added_value = 0
            items_added = dpg.add_input_text(label="Items Added",width=22,readonly=True,default_value=items_added_value,use_internal_label=True)
            dpg.add_spacer(height=2)

            with dpg.table(header_row=True,borders_innerH=True,borders_innerV=True,borders_outerH=True,borders_outerV=True,tag="customer_table") as customer_table:
                dpg.add_table_column(label="Item")
                dpg.add_table_column(label="Cost") 
                recipt_row = dpg.table_row() 
            dpg.add_text("Total :")
        
    
    class Phone_window:
        with dpg.window(label="phone_window",tag="phone_window", pos=(740,180),width=235,height=globals.HEIGHT/3.67,no_close=True,
            no_move=True,no_title_bar=True,no_resize=True) as phone_window:
            dpg.add_button(label="Department Phone",width=dpg.get_item_width("phone_window")-15,height=30)
            dpg.add_text("ORDER SELECTED :")
            with dpg.group(horizontal=True):
                dpg.add_input_text(hint="Input store number",tag="input_store_number")
                with dpg.tooltip("input_store_number"):
                    dpg.add_text("*Call store to place selected order")
                dpg.add_button(label="Call")

    with dpg.window(label="checkout_window",tag="checkout_window", pos=(225,355),width=750,height=globals.HEIGHT/3.07,no_close=True,
        no_move=True,no_title_bar=True,no_resize=True) as checkout_window:
        dpg.create_context()

    menu_bg_windows = (Side_menu.side_menu_window,Main_Window.store_info_window)
    main_menu_windows = (Main_Window.store_info_window,Main_Window.store_inventory_window,incoming_orders_window,recieve_shipment_window,sales_analytics_window)
    store_inventory_tables = [Main_Window.shoes_table,Main_Window.shirts_table,Main_Window.pants_table,Main_Window.accessories_table]

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
                
class Binded_themes:
    dpg.bind_item_theme(Windows.Side_menu.background_window,Theme.background_theme)
    dpg.bind_item_theme(Windows.Side_menu.side_menu_window,Theme.window_theme)
    dpg.bind_item_theme(Windows.Main_Window.store_info_window,Theme.window_theme)
    dpg.bind_item_theme(Windows.Customer_window.customer_window,Theme.window_theme)
    dpg.bind_item_theme(Windows.Phone_window.phone_window,Theme.window_theme)
    dpg.bind_item_theme(Windows.checkout_window,Theme.window_theme)
    dpg.bind_item_theme(Windows.Side_menu.profile_background,Theme.child_window_theme)
    dpg.bind_item_theme(Windows.Main_Window.store_info_cw,Windows.Main_Window.scrollbar_size) 
    for window in Windows.main_menu_windows: 
        dpg.bind_item_theme(window,Theme.window_theme)



dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("background_window", True)
dpg.start_dearpygui()
dpg.destroy_context()